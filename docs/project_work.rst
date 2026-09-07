.. _project_work:

Project Work
============

The table below summarizes the pull requests, their technical scope, current
status, and related issues. Statistics are GitHub-reported values verified on
**7 September 2026**.

.. raw:: html

    <div class="project-work-table" style="max-width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch;">
        <table style="width: 100%; min-width: 860px; border-collapse: collapse; font-family: Georgia, serif; margin-bottom: 10px;">
            <thead>
            <tr style="background-color: #6ab0de; border: 2px solid #000;">
                <th style="padding: 10px; border: 2px solid #000; text-align: left; width: 6%; color: black;">Task</th>
                <th style="padding: 10px; border: 2px solid #000; text-align: left; width: 10%; color: black;">PR No.</th>
                <th style="padding: 10px; border: 2px solid #000; text-align: left; width: 54%; color: black;">Contribution</th>
                <th style="padding: 10px; border: 2px solid #000; text-align: left; width: 14%; color: black;">Status</th>
                <th style="padding: 10px; border: 2px solid #000; text-align: left; width: 16%; color: black;">Linked Issue / PRs</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">1</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1596" target="_blank" rel="noopener">#1596</a></td>
                <td style="padding: 10px; border: 2px solid #000;">
                    <div style="margin-bottom: 6px;"><strong>J-space sparse decomposition.</strong></div>
                    <div style="margin-bottom: 6px;">Added NNOMP, exact Lawson-Hanson NNLS, gradient pursuit, cached J-lens dictionaries, typed results, Bridge wrappers, KKT checks, and model-free plus GPT-2/Gemma tests.</div>
                    <div><em>Statistics: 1,613 additions; 3 deletions; 9 commits; 7 files changed.</em></div>
                </td>
                <td style="padding: 10px; border: 2px solid #000;">Merged<br/>14 Aug 2026</td>
                <td style="padding: 10px; border: 2px solid #000;">Basis for <a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1676" target="_blank" rel="noopener">#1676</a>, <a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1738" target="_blank" rel="noopener">#1738</a>, <a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1741" target="_blank" rel="noopener">#1741</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">2</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1676" target="_blank" rel="noopener">#1676</a></td>
                <td style="padding: 10px; border: 2px solid #000;">
                    <div style="margin-bottom: 6px;"><strong>J-space occupancy and fraction of variance.</strong></div>
                    <div style="margin-bottom: 6px;">Added random-dictionary controls, maximum-separation occupancy, selected-span projection metrics, median and pooled summaries, tests, and documentation.</div>
                    <div><em>Statistics: 701 additions; 4 deletions; 3 commits; 7 files changed.</em></div>
                </td>
                <td style="padding: 10px; border: 2px solid #000;">Merged<br/>19 Aug 2026</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1596" target="_blank" rel="noopener">#1596</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">3</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1721" target="_blank" rel="noopener">#1721</a></td>
                <td style="padding: 10px; border: 2px solid #000;">
                    <div style="margin-bottom: 6px;"><strong>Projection-kernel affinity for attention-head subspaces.</strong></div>
                    <div style="margin-bottom: 6px;">Implemented principal-angle geometry, basis-invariant scores, rank metadata, OQ/OK/OV Bridge wrappers, GQA support, masks, and tiled scoring.</div>
                    <div><em>Statistics: 1,620 additions; 0 deletions; 4 commits; 8 files changed.</em></div>
                </td>
                <td style="padding: 10px; border: 2px solid #000;">Merged<br/>28 Aug 2026</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/issues/1720" target="_blank" rel="noopener">Issue #1720</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">4</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1723" target="_blank" rel="noopener">#1723</a></td>
                <td style="padding: 10px; border: 2px solid #000;">
                    <div style="margin-bottom: 6px;"><strong>Backward Lens vocabulary readout.</strong></div>
                    <div style="margin-bottom: 6px;">Added exact MLP gradient-factor reconstruction, raw and normalized vocabulary projections, signed token rankings, diagnostics, state-preservation tests, docs, and a demo.</div>
                    <div><em>Statistics: 4,125 additions; 0 deletions; 18 commits; 9 files changed.</em></div>
                </td>
                <td style="padding: 10px; border: 2px solid #000;">Merged<br/>4 Sep 2026</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/issues/1686" target="_blank" rel="noopener">Issue #1686</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">5</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1735" target="_blank" rel="noopener">#1735</a></td>
                <td style="padding: 10px; border: 2px solid #000;">
                    <div style="margin-bottom: 6px;"><strong>BERT Bridge-to-Hugging-Face parity.</strong></div>
                    <div style="margin-bottom: 6px;">Added independent CPU-fp32 comparisons for final logits, five activation-cache points, and padded attention-mask behavior.</div>
                    <div><em>Statistics: 114 additions; 0 deletions; 1 commit; 1 file changed.</em></div>
                </td>
                <td style="padding: 10px; border: 2px solid #000;">Merged<br/>1 Sep 2026</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/issues/1665" target="_blank" rel="noopener">Issue #1665</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">6</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1738" target="_blank" rel="noopener">#1738</a></td>
                <td style="padding: 10px; border: 2px solid #000;">
                    <div style="margin-bottom: 6px;"><strong>Jacobian Lens decomposition demo.</strong></div>
                    <div style="margin-bottom: 6px;">Added an executed GPT-2 notebook covering sparse coordinates, variance, occupancy, ranking overlap, solver runtime, and causal removal against norm-matched controls.</div>
                    <div><em>Statistics: 1,468 additions; 0 deletions; 3 commits; 4 files changed.</em></div>
                </td>
                <td style="padding: 10px; border: 2px solid #000;">Merged<br/>3 Sep 2026</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1596" target="_blank" rel="noopener">#1596</a>, <a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1676" target="_blank" rel="noopener">#1676</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">7</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1741" target="_blank" rel="noopener">#1741</a></td>
                <td style="padding: 10px; border: 2px solid #000;">
                    <div style="margin-bottom: 6px;"><strong>Anchored J-space coordinate patching.</strong></div>
                    <div style="margin-bottom: 6px;">Implemented substitute and swap edits, exact no-op interpolation, residual preservation, absent-target insertion, conditioning diagnostics, reused-decomposition validation, and MPS fallback.</div>
                    <div><em>Statistics: 1,561 additions; 31 deletions; 11 commits; 10 files changed.</em></div>
                </td>
                <td style="padding: 10px; border: 2px solid #000;">Merged<br/>4 Sep 2026</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/issues/1739" target="_blank" rel="noopener">Issue #1739</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">8</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1749" target="_blank" rel="noopener">#1749</a></td>
                <td style="padding: 10px; border: 2px solid #000;">
                    <div style="margin-bottom: 6px;"><strong>Dynamic J-space coordinate-patch hooks.</strong></div>
                    <div style="margin-bottom: 6px;">Carries anchored edits into <code>run_with_hooks</code> and <code>generate</code>, with per-position solves, caller-owned caching, atomic failure, and focused tests.</div>
                    <div><em>Statistics: 880 additions; 244 deletions; 5 commits; 12 files changed.</em></div>
                </td>
                <td style="padding: 10px; border: 2px solid #000;">Open<br/>5 Sep 2026</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/issues/1748" target="_blank" rel="noopener">Issue #1748</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">9</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1750" target="_blank" rel="noopener">#1750</a></td>
                <td style="padding: 10px; border: 2px solid #000;">
                    <div style="margin-bottom: 6px;"><strong>Node attribution-patching substrate.</strong></div>
                    <div style="margin-bottom: 6px;">Added filtered gradient caching, typed node/config/result models, denoising sign semantics, first-order scoring, and an exact linear-network oracle.</div>
                    <div><em>Statistics: 1,029 additions; 0 deletions; 7 commits; 3 files changed.</em></div>
                </td>
                <td style="padding: 10px; border: 2px solid #000;">Open<br/>6 Sep 2026</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/issues/1742" target="_blank" rel="noopener">Issue #1742</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">10</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1752" target="_blank" rel="noopener">#1752</a></td>
                <td style="padding: 10px; border: 2px solid #000;">
                    <div style="margin-bottom: 6px;"><strong>NeoX/Pythia unembedding compatibility.</strong></div>
                    <div style="margin-bottom: 6px;">Supports <code>embed_out</code> and <code>lm_head</code>, aligns Bridge and HookedTransformer conversion, and adds model-free plus end-to-end regressions.</div>
                    <div><em>Statistics: 165 additions; 3 deletions; 4 commits; 4 files changed.</em></div>
                </td>
                <td style="padding: 10px; border: 2px solid #000;">Open<br/>6 Sep 2026</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/issues/1751" target="_blank" rel="noopener">Issue #1751</a></td>
            </tr>
            <tr>
                <td style="padding: 10px; border: 2px solid #000;">11</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/pull/1729" target="_blank" rel="noopener">#1729</a></td>
                <td style="padding: 10px; border: 2px solid #000;">
                    <div style="margin-bottom: 6px;"><strong>Leakage-safe sparse probing collaboration.</strong></div>
                    <div style="margin-bottom: 6px;">Proposed the split-before-selection design, coordinated review, and prepared a hardening commit for MPS, convergence metadata, typed results, and leakage tests. This PR is authored by another contributor.</div>
                    <div><em>Statistics: Not included in authored totals.</em></div>
                </td>
                <td style="padding: 10px; border: 2px solid #000;">Open collaboration</td>
                <td style="padding: 10px; border: 2px solid #000;"><a href="https://github.com/TransformerLensOrg/TransformerLens/issues/1728" target="_blank" rel="noopener">Issue #1728</a>, <a href="https://github.com/janmenjayap/TransformerLens/commit/cc6470f9425beccafd191b066c0e36f8642a8d0b" target="_blank" rel="noopener">commit cc6470f</a></td>
            </tr>
            </tbody>
        </table>
    </div>

    <hr/>

Statistics
----------

The seven merged authored pull requests total **11,202 additions**, **38
deletions**, **49 commits**, and **46 changed-file entries**. The three open
authored pull requests total **2,074 additions** and **247 deletions**. Counts
include source, tests, documentation, and notebooks. The non-authored
collaboration is excluded from aggregate code totals.

GitHub is the authority for status after the snapshot date. Use the links in the
table to see current review state, discussion, checks, and final merged changes.