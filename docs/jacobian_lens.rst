.. _jacobian-lens:

Jacobian Lens Program
=====================

The Jacobian Lens maps vocabulary directions back through a model's local
Jacobian. For layer :math:`\ell` and token :math:`t`, a J-lens vector has the
form

.. math::

   v_t = J_\ell^\top W_U[:, t].

My contribution series builds an analysis and intervention stack around these
vectors: first recover sparse coordinates, then characterize the recovered
space, test it in a reproducible notebook, and finally edit coordinates both
offline and during a live forward pass.

Program map
-----------

.. list-table::
   :widths: 13 19 47 21
   :header-rows: 1

   * - Date
     - Record
     - Capability
     - Status
   * - 14 Aug 2026
     - `PR #1596 <https://github.com/TransformerLensOrg/TransformerLens/pull/1596>`_
     - J-space sparse decomposition
     - :status-merged:`Merged`
   * - 19 Aug 2026
     - `PR #1676 <https://github.com/TransformerLensOrg/TransformerLens/pull/1676>`_
     - Occupancy and fraction-of-variance profiling
     - :status-merged:`Merged`
   * - 3 Sep 2026
     - `PR #1738 <https://github.com/TransformerLensOrg/TransformerLens/pull/1738>`_
     - Executed sparse-decomposition demo
     - :status-merged:`Merged`
   * - 4 Sep 2026
     - `PR #1741 <https://github.com/TransformerLensOrg/TransformerLens/pull/1741>`_
     - Anchored offline coordinate patching
     - :status-merged:`Merged`
   * - Opened 5 Sep 2026
     - `PR #1749 <https://github.com/TransformerLensOrg/TransformerLens/pull/1749>`_
     - Dynamic coordinate-patch hooks
     - :status-open:`Open`

Sparse decomposition
--------------------

`PR #1596 <https://github.com/TransformerLensOrg/TransformerLens/pull/1596>`_
introduced a model-free sparse solver and a TransformerBridge wrapper. Given an
activation :math:`x` and the full-vocabulary J-lens dictionary :math:`B`, it
finds a small nonnegative coordinate vector :math:`c` such that

.. math::

   x = Bc + r,

where :math:`r` is the component not reconstructed by the selected atoms.

What shipped
^^^^^^^^^^^^

* ``get_sparse_decomposition`` and the detached ``JSpaceDecomposition`` result;
* ``JacobianLens.lens_vector_dictionary`` for cached layer dictionaries;
* ``JacobianLens.decompose`` for raw activations or prompt positions;
* nonnegative orthogonal matching pursuit with exact Lawson-Hanson NNLS on the
  selected support, plus gradient pursuit for alignment with the source paper;
* separate ``coordinates``, ``reconstruction``, ``j_space_component``, and
  ``non_j_space_component`` outputs so constrained reconstruction is not
  confused with orthogonal span projection.

The correctness work included an independent KKT validation of NNLS, explicit
active-versus-selected support semantics, model-free unit tests, real GPT-2 and
Gemma integration tests, type checks, documentation builds, and the repository's
full pull-request test surface. The merged PR contained 1,613 additions across 7
files and 9 commits.

Occupancy and explained variance
--------------------------------

`PR #1676 <https://github.com/TransformerLensOrg/TransformerLens/pull/1676>`_
added two ways to characterize a fitted J-space.

**Occupancy** compares cumulative variance captured by greedily selected J-lens
atoms against random unit-norm control dictionaries. The reported occupancy is
the point of maximum separation between the real and mean control curves. This
replaced a calibration-sensitive quantile rule with a deterministic,
threshold-free contract.

**Fraction of variance** measures the selected-support projection, not the
nonnegative reconstruction:

.. math::

   \operatorname{FoV}(x) =
   \frac{\lVert \operatorname{Proj}_{\operatorname{span}(B_S)} x \rVert_2^2}
        {\lVert x \rVert_2^2}.

The API reports both the median position-level ratio and the pooled
sum-of-squares ratio across prompts. Empty sampling regions produce a documented
``NaN`` result rather than a misleading zero. The focused unit, integration, and
docstring run reported 246 passing tests.

Reproducible empirical notebook
-------------------------------

`PR #1738 <https://github.com/TransformerLensOrg/TransformerLens/pull/1738>`_
added an executed GPT-2 notebook covering six experiments: local sparse
coordinates, selected-span variance, control-calibrated occupancy, support
overlap with J-lens and Logit Lens rankings, NNOMP versus gradient-pursuit
runtime, and causal removal against equal-dimensional random J-space controls.

The saved run reported median selected-span variance of 1.94--2.80%, occupancy
of 1 across eight prompt/layer trials, and low support overlap with both ranking
baselines. In its causal experiment, the exactly norm-matched selected-minus-
random target-logit effect was -4.8814 with a 95% bootstrap interval of
[-8.2973, -2.0723]. The notebook explicitly labels that experiment as
underpowered and does not claim that J-space is privileged over matched
non-J-space representations.

Validation included a fresh-kernel 19-cell execution with no error output,
cross-cell consistency assertions, 19 passing notebook tests, and 251 focused
Jacobian Lens tests.

Anchored coordinate patching
----------------------------

Sparse decomposition identifies active coordinates; `PR #1741
<https://github.com/TransformerLensOrg/TransformerLens/pull/1741>`_ made those
coordinates editable. The offline primitive keeps the original residual and all
unedited coordinates fixed:

.. math::

   x' = r + Bc'.

``substitute`` moves a source coordinate to a target and zeros the source;
``swap`` exchanges source and target; and ``alpha`` interpolates the edit, with
``alpha=0`` guaranteed to be an exact no-op. An absent target is appended with a
zero starting coordinate.

The important design choice is that the patch never recomputes
:math:`B^\dagger x`. It uses the anchored decomposition chart, avoiding silent
movement in every coordinate when the basis changes. Conditioning and
near-parallel diagnostics warn but do not block the inversion-free edit.

The PR also added an Apple Silicon fallback for float64 NNLS work, detached
report-only result objects, strict validation for reused decompositions, and
model-free, wrapper, GPT-2 integration, and MPS tests. All 25 GitHub checks
passed before merge.

Dynamic hooks
-------------

`PR #1749 <https://github.com/TransformerLensOrg/TransformerLens/pull/1749>`_
is the active follow-up. It proposes ``coordinate_patch_hooks`` for applying an
anchored edit inside ``run_with_hooks`` or ``generate``.

The implementation handles each ``(batch, position)`` pair independently,
requires callers to name positions so vocabulary-scale solves are never hidden,
and accepts a caller-owned decomposition cache keyed by layer, batch item, and
position. It fails atomically when a requested source coordinate is inactive,
rather than returning a partially patched batch.

At the snapshot date, focused validation reported 157 unit tests, one real GPT-2
integration test, and a clean type check across 397 source files. Because this
PR is open, its API and outcome remain subject to maintainer review.

Research basis
--------------

This work implements and extends ideas from Gurnee et al. (2026), `Verbalizable
Representations Form a Global Workspace in Language Models
<https://transformer-circuits.pub/2026/jacobian-lens/index.html>`_. The
implementation deliberately distinguishes results reproduced on open-weight
models from quantitative findings reported on closed models.