.. _engineering:

Engineering and Reliability
===========================

Interpretability results are only useful when the model adapter, numerical
contracts, and evaluation split are trustworthy. These contributions focus on
failure modes that can otherwise produce plausible but incorrect analyses.

BERT Bridge-to-Hugging-Face parity
----------------------------------

:status-merged:`Merged 1 September 2026` | :pr:`1735` | upstream `issue #1665
<https://github.com/TransformerLensOrg/TransformerLens/issues/1665>`_

The BERT ``TransformerBridge`` had no direct numerical parity suite against its
underlying Hugging Face model. :pr:`1735` added CPU-fp32 comparisons against an
independent eager Hugging Face reference for:

* final logits;
* five Bridge-native activation-cache points; and
* padded attention-mask behavior.

All three focused parity tests passed locally, and all 22 applicable fork checks
passed before merge. The change is intentionally compact -- 114 additions in
one file and one commit -- because the independent comparison, not test volume,
is the value.

NeoX and Pythia unembedding compatibility
-----------------------------------------

:status-open:`Open as of 7 September 2026` | :issue:`1751` | :pr:`1752`

While generalizing Backward Lens to dense-MLP model families, every
GPT-NeoX/Pythia checkpoint failed during ``TransformerBridge`` boot. The adapter
resolved the unembedding as ``embed_out``, but current Transformers releases use
``lm_head``. The repository's lock file was already on the new layout.

The fix keeps the Bridge adapter and ``HookedTransformer`` weight-conversion
path aligned and evolved during development to support both ``embed_out`` and
``lm_head`` layouts. A model-free regression resolves the component against the
new module shape, and component-mapping validation now happens before unembedding
lookup.

Validation reported:

* 23 passing NeoX adapter tests under Transformers 5.15.1;
* an end-to-end ``EleutherAI/pythia-70m`` Bridge boot and forward pass;
* exact Backward Lens reconstruction at layers 0, 3, and 5;
* a sibling ``EleutherAI/gpt-neo-125M`` boot and reconstruction check; and
* restored coverage for existing Pythia integration paths.

The open PR contains 165 additions and 3 deletions across 4 files and 4 commits.
Its final compatibility policy remains subject to maintainer review.

Leakage-safe sparse probing
---------------------------

:status-open:`Open proposal and collaborative implementation` | :issue:`1728`
| :pr:`1729`

My proposal defines a model-free, dependency-free binary sparse-probing API for
activation tensors. The central risk is test leakage: splitting after feature
selection or normalization silently allows held-out information into the probe.
The proposed contract therefore splits first and learns every statistic from the
training partition only.

Proposal design
^^^^^^^^^^^^^^^

* deterministic stratified train/test splitting before learned statistics;
* train-only absolute mean-difference coordinate selection;
* optional train-only standardization with metadata carried into the result;
* balanced binary logistic fitting with Torch LBFGS on CPU float64;
* held-out accuracy, precision, recall, and primary F1 reporting;
* fixed-split sweeps over :math:`k`, with deterministic random-coordinate and
  shuffled-training-label controls;
* explicit claim boundaries: decodability is not causal use, and a curve shape
  alone is not evidence of superposition.

The validation plan names independent selector calculations, planted sparse and
distributed synthetic features, held-out-only perturbations, deterministic
controls, analytic objective/gradient checks, forced non-convergence, and input
policy tests.

Collaborative implementation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another contributor opened :pr:`1729` while I was independently implementing
the accepted proposal. I paused the overlapping branch, reviewed the gap between
the implementations, and prepared `commit cc6470f
<https://github.com/janmenjayap/TransformerLens/commit/cc6470f9425beccafd191b066c0e36f8642a8d0b>`_
directly on that PR's then-current head for cherry-picking.

The focused commit adds MPS-safe CPU-first indexing and conversion, actual LBFGS
iteration reporting, aligned convergence thresholds, frozen typed result
contracts, optimization metadata, and stronger held-out leakage and real-MPS
tests. Its validation included 8 focused sparse-probing tests, repeated real-MPS
fit and sweep checks, 5,316 unit tests, type checking, formatting, and a docs
build.

At the snapshot date, the commit had been shared and the PR author had agreed to
integrate it, but it was not yet present in the upstream PR history. This site
therefore records it as a **collaborative contribution**, not an authored PR or
merged change.

Reliability as part of the feature
----------------------------------

Across these changes, validation is treated as part of the user-facing design:

* parity tests compare independent implementations rather than two wrappers over
  the same path;
* result objects carry diagnostics instead of collapsing uncertainty to one
  score;
* error and warning policies are documented and tested;
* CPU, CUDA-facing CI, and Apple Silicon paths are considered separately; and
* unsupported scope fails explicitly instead of silently approximating a result.