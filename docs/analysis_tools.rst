.. _analysis-tools:

Analysis Tools
==============

These contributions ask three different questions about transformer internals:
what parameter gradients mean in vocabulary space, how attention-head weight
subspaces align, and which forward-pass components matter to a behavior. Each
tool makes its mathematical convention and correctness oracle part of the API.

Backward Lens
-------------

:status-merged:`Merged 4 September 2026` | :issue:`1686` | :pr:`1723`

TransformerLens already supported forward vocabulary readouts, but it lacked a
maintained way to interpret parameter gradients in the same vocabulary-facing
frame. Backward Lens fills that gap for raw GPT-2 models loaded through
``TransformerBridge`` without training an auxiliary model, applying an optimizer
step, or depending on unlicensed reference code.

Factorization contract
^^^^^^^^^^^^^^^^^^^^^^

For each selected GPT-2 MLP layer, the implementation captures aligned
position-wise factors and verifies that they reconstruct gradients obtained
independently with ``torch.autograd.grad``:

.. math::

  \nabla W_{in} = \sum_i x_i \otimes \nabla pre_i,

.. math::

  \nabla W_{out} = \sum_i hidden_i \otimes \nabla out_i.

This outer-product identity is the central correctness invariant. The tool
reports absolute and relative reconstruction errors and numerical ranks rather
than asking users to trust a visualization alone.

Vocabulary readout
^^^^^^^^^^^^^^^^^^

Residual-width factors are projected through the model's live final
normalization and unembedding. Normalization statistics are recomputed for every
factor, avoiding the invalid assumption that one residual vector's statistics
can be reused for another. The result exposes signed top and bottom token
directions, target-token ranks, factor norms, and explicit exact-zero markers.

Both raw and opt-in Normalized Logit Lens projections are available. The docs
also distinguish the gradient direction from the *negative* update direction
used by gradient descent, a sign convention that is easy to invert in manual
analysis.

State and scope
^^^^^^^^^^^^^^^

The analysis uses one forward pass and one ``torch.autograd.grad`` call. It does
not call ``backward()``, write parameter ``.grad`` fields, freeze parameters, or
leave temporary hooks installed. Tests cover preservation of weights, gradients,
``requires_grad`` flags, training mode, RNG state, and existing hooks on both
successful and failing calls.

The first release deliberately supports one unbatched prompt, one single-token
next-token target, selected layers, and dense GPT-2 MLPs. Gated MLPs, additional
model families, batched prompts, and model editing were left for follow-up work.

Validation and outcome
^^^^^^^^^^^^^^^^^^^^^^

The PR reported 38 unit tests, 23 integration tests, and 10 notebook tests. Its
executed demo covers reconstruction, rank, per-position vocabulary directions,
raw versus normalized projections, sign semantics, zero-signal handling, and
contribution-sorted cumulative reconstruction. During review, the factorization
was also checked against finite differences independently of autograd and the
paper result was reproduced from the contributed notebook.

The merged change contains 4,125 additions across 9 files and 18 commits. It was
slated for TransformerLens 3.9.0.

Projection Kernel
-----------------

:status-merged:`Merged 28 August 2026` | :issue:`1720` | :pr:`1721`

Projection Kernel provides a basis-invariant measure of affinity between the
weight subspaces associated with attention heads. For orthonormal bases
:math:`Q_A` and :math:`Q_B`, the raw score is

.. math::

   K(A, B) = \operatorname{tr}(P_A P_B)
     = \lVert Q_A^\top Q_B \rVert_F^2
     = \sum_i \cos^2 \theta_i,

where :math:`\theta_i` are principal angles. This lets an analysis compare
subspaces without depending on an arbitrary choice of basis.

What shipped
^^^^^^^^^^^^

* model-independent reduced-SVD basis extraction, principal angles, raw and
  normalized projection-kernel scores, numerical-rank metadata, and expected
  random-subspace moments;
* ``TransformerBridge`` wrappers for OQ, OK, and OV head-weight comparisons;
* native grouped-query-attention KV-head identity and hybrid-layer indexing;
* forward and all-layer masks, bounded-memory tiled scoring, and ranked output;
* fp16/bf16 promotion to fp32 for stable SVDs while preserving float64 input;
* documentation of orientation, rank semantics, scaling limits, GQA behavior,
  and the distinction from attention-head Composition Score.

Malformed and rank-deficient inputs report role, layer, and head context. Model
weights are detached from autograd. The focused suite reported 67 passing tests,
and all applicable GitHub compatibility, coverage, formatting, typing,
documentation, benchmark, and notebook checks passed before merge.

The merged change contains 1,620 additions across 8 files and 4 commits.

Attribution patching substrate
------------------------------

:status-open:`Open as of 7 September 2026` | :issue:`1742` | :pr:`1750`

Activation patching can require one forward pass per intervention. Attribution
patching replaces those repeated interventions with a first-order estimate from
a clean activation, a corrupt activation, and one corrupt-run gradient:

.. math::

   \operatorname{effect}(node)
   = (a_{clean} - a_{corrupt}) \cdot
     \frac{\partial metric}{\partial a_{corrupt}}.

The proposed first slice targets ``TransformerBridge`` and node-level
attribution. It includes a names-filtered gradient-cache substrate, a typed
``Node`` model for embedding, attention-head-output, and MLP-output nodes,
``EdgeAttributionConfig``, ``AttributionResult``, and the public
``attribution_patch`` entry point. Scores are averaged across clean/corrupt pairs
before ranking.

Correctness design
^^^^^^^^^^^^^^^^^^

The sign convention is pinned to denoising: positive means that moving the
corrupt node toward its clean activation increases the metric. Clean and corrupt
tokenizations must have equal length, and absent required hook points raise
instead of silently reducing coverage.

The key oracle uses a deliberately linear ``TransformerBridge`` configuration.
With a linear metric, fixed attention patterns, identity MLP activation, and
constant LayerNorm scale, summed node attributions must exactly reconstruct
:math:`metric(clean) - metric(corrupt)`. The tests explicitly state that this
identity is exact for the constructed linear network, not for an arbitrary
nonlinear model.

The public configuration reserves ``granularity="edge"`` and ``ig_steps > 1``
but raises ``NotImplementedError`` for them in this PR. Edge Attribution
Patching, EAP-IG, ablate-outside faithfulness, oracle parity, and the demo are
named follow-ups, preserving a stable API without presenting unimplemented work
as complete.

At the snapshot date, the open PR contains 1,029 additions across 3 files and 7
commits. Its final shape and merge outcome remain subject to review.

Comparison
----------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Tool
     - Object of study
     - Primary oracle
     - Outcome
   * - Backward Lens
     - MLP weight-gradient factors
     - Exact outer-product reconstruction
     - Merged
   * - Projection Kernel
     - Attention-head weight subspaces
     - Basis invariance and principal-angle identities
     - Merged
   * - Attribution patching
     - Residual-stream computational nodes
     - Exact reconstruction on a linear Bridge
     - Open