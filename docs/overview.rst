.. _overview:

Overview
========

.. raw:: html

    <hr/>
    <div style="max-width: 100%;">
        <table style="width: 100%; border-collapse: collapse; font-family: Georgia, serif; margin-bottom: 10px; table-layout: fixed; word-wrap: break-word;">
            <thead>
            <tr style="background-color: #6ab0de; border: 2px solid #000;">
                <th style="padding: 10px; border: 2px solid #000; text-align: left; width: 22%; color: black;">Parameter</th>
                <th style="padding: 10px; border: 2px solid #000; text-align: left; width: 78%; color: black;">Value</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">Project name</td>
                <td style="padding: 10px; border: 2px solid #000; word-break: break-word;"><a href="https://github.com/TransformerLensOrg/TransformerLens" target="_blank" rel="noopener">TransformerLens Contributions</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">Organization</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg" target="_blank" rel="noopener">TransformerLensOrg</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">Contributor</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/janmenjayap" target="_blank" rel="noopener">Janmenjaya Panda</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">Mentor</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/jlarson4" target="_blank" rel="noopener">Jonah Larson</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">Contribution period</td>
                <td style="padding: 10px; border: 2px solid #000;">July 2026 - present</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">Technologies</td>
                <td style="padding: 10px; border: 2px solid #000;">Python, PyTorch, TransformerLens, Hugging Face Transformers, Sphinx</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">Topics</td>
                <td style="padding: 10px; border: 2px solid #000;">Mechanistic interpretability, Jacobian Lens, J-space decomposition, gradient interpretation, subspace geometry, attribution patching, sparse probing, and model-bridge reliability</td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000; vertical-align: top;">Statistics<br/><em>(as of 09/07/2026)</em></td>
                <td style="padding: 10px; border: 2px solid #000; line-height: 1.5;">
                    <strong>10 authored pull requests:</strong> 7 merged and 3 open.<br/>
                    <strong>7 authored issues:</strong> 3 completed and 4 open.<br/>
                    <strong>Merged authored work:</strong> 11,202 additions, 38 deletions, 49 commits, and 46 changed-file entries.<br/>
                    <strong>Open authored work:</strong> 2,074 additions and 247 deletions across 3 pull requests.
                </td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000; vertical-align: top;">Project details</td>
                <td style="padding: 10px; border: 2px solid #000; text-align: justify; line-height: 1.5; word-wrap: break-word;">This work turns recent mechanistic-interpretability ideas into tested TransformerLens APIs. It covers sparse Jacobian-space analysis and intervention, vocabulary-facing gradient interpretation, attention-head subspace comparison, first-order attribution, independent numerical parity, and cross-model compatibility. Each contribution pairs an explicit mathematical contract with focused tests, documentation, and reproducible examples.</td>
            </tr>
            </tbody>
        </table>
    </div>
    <hr/>

The line, file, and commit totals are GitHub-reported snapshot metrics. They
include source, tests, documentation, and notebooks; changed-file counts are
summed per pull request and are not counts of unique repository paths.

Detailed Overview
-----------------

The contributions form a connected research and engineering program: define a
mathematical object, expose it through a maintainable API, validate it against
an independent numerical oracle, and document exactly what the result does and
does not establish.

Jacobian Lens and J-space
^^^^^^^^^^^^^^^^^^^^^^^^^

The Jacobian Lens maps a vocabulary direction backward through the model's local
Jacobian. For layer :math:`\ell` and vocabulary token :math:`t`, the J-lens
vector is

.. math::

    v_t = J_\ell^\top W_U[:, t],

where :math:`W_U[:, t]` is the token's unembedding direction. The **J-space** at
that layer is the span of these vocabulary-derived vectors. Collecting them as
dictionary columns gives :math:`B = [v_1, \ldots, v_{|V|}]`.

:pr:`1596` implemented sparse J-space decomposition. For an activation
:math:`x`, it finds a small nonnegative coordinate vector by solving

.. math::

    c^* = \underset{c \ge 0,\, \lVert c \rVert_0 \le k}{\operatorname{argmin}}
    \lVert x - Bc \rVert_2^2,

and reports the anchored decomposition

.. math::

    x = Bc^* + r.

The implementation includes nonnegative orthogonal matching pursuit, exact
Lawson-Hanson nonnegative least squares on the selected support, gradient
pursuit, cached layer dictionaries, typed result objects, and independent KKT
checks for the NNLS solution.

Occupancy and fraction of variance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:pr:`1676` made the recovered space measurable. **Occupancy** compares the
cumulative variance captured by greedily selected J-lens atoms with random
unit-norm control dictionaries and reports the point of maximum separation.
For selected support :math:`S`, fraction of variance uses orthogonal projection
onto the selected span:

.. math::

    \operatorname{FoV}(x) =
    \frac{\lVert \operatorname{Proj}_{\operatorname{span}(B_S)} x \rVert_2^2}
          {\lVert x \rVert_2^2}.

This deliberately measures the span rather than conflating it with the
nonnegative reconstruction. :pr:`1738` added a reproducible GPT-2 notebook for
sparse coordinates, selected-span variance, occupancy, ranking overlap, solver
runtime, and causal removal against norm-matched random controls.

Anchored J-space interventions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:pr:`1741` implemented coordinate substitution and swapping while preserving
the original residual and every unedited coordinate:

.. math::

    x' = r + Bc'.

The edit uses the existing decomposition chart rather than recomputing
:math:`B^\dagger x`, so changing one coordinate cannot silently move all the
others. The interpolation parameter :math:`\alpha=0` is an exact no-op, and
conditioning diagnostics expose near-parallel directions. :pr:`1749` extends
the same anchored edit into live ``run_with_hooks`` and ``generate`` calls; it
is open at the snapshot date.

Backward Lens
^^^^^^^^^^^^^

:pr:`1723` implemented a vocabulary-facing interpretation of GPT-2 MLP
parameter gradients. It captures position-wise factors whose outer products
must independently reconstruct the parameter gradients:

.. math::

    \nabla W_{in} = \sum_i x_i \otimes \nabla pre_i,

.. math::

    \nabla W_{out} = \sum_i hidden_i \otimes \nabla out_i.

Residual-width factors are projected through the model's live final
normalization and unembedding. The API reports signed token directions,
target-token ranks, factor norms, numerical ranks, and absolute and relative
reconstruction errors without mutating model parameters or ``.grad`` fields.

Attention-head subspace geometry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:pr:`1721` implemented the Projection Kernel, a basis-invariant affinity between
attention-head weight subspaces. For orthonormal bases :math:`Q_A` and
:math:`Q_B`,

.. math::

    K(A, B) = \operatorname{tr}(P_A P_B)
              = \lVert Q_A^\top Q_B \rVert_F^2
              = \sum_i \cos^2 \theta_i,

where :math:`\theta_i` are the principal angles. The implementation covers
reduced-SVD basis extraction, rank metadata, random-subspace moments, OQ/OK/OV
comparisons, grouped-query attention, masks, and bounded-memory tiled scoring.

Attribution patching
^^^^^^^^^^^^^^^^^^^^

:pr:`1750` develops node-level attribution patching from one clean activation,
one corrupt activation, and one corrupt-run gradient:

.. math::

    \operatorname{effect}(node) =
    (a_{clean} - a_{corrupt}) \cdot
    \frac{\partial metric}{\partial a_{corrupt}}.

The sign convention is denoising: a positive score means moving a corrupt node
toward its clean activation increases the metric. A deliberately linear model
provides the exact correctness oracle. Edge Attribution Patching and integrated
gradients remain explicitly reserved follow-ups rather than being presented as
implemented in this open pull request.

Validation, probing, and model compatibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:pr:`1735` added independent BERT Bridge-to-Hugging-Face parity for logits,
activation-cache points, and padded attention masks. :issue:`1728` specifies a
leakage-safe sparse-probing pipeline that splits before feature selection or
normalization and evaluates deterministic random-coordinate and shuffled-label
controls. :pr:`1752` addresses NeoX/Pythia unembedding compatibility across
``embed_out`` and ``lm_head`` layouts.

Across the program, correctness is tested through independent KKT conditions,
outer-product reconstruction, basis invariance, direct Hugging Face parity, and
exact identities on deliberately linear models. Open-weight experiments,
decodability results, and first-order approximations are documented with their
claim boundaries.

.. note::

    Pull-request and issue status is a verified snapshot as of **7 September
    2026**. See :doc:`project_work` for the source-linked contribution table.