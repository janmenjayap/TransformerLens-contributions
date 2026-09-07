.. _contribution-index:

Contribution Index
==================

This is the source-linked ledger used by the rest of the site. It was
verified against GitHub on **7 September 2026** using the `authored pull-request
search <https://github.com/TransformerLensOrg/TransformerLens/issues?q=is%3Apr%20author%3A%40janmenjayap>`_
and `authored issue search
<https://github.com/TransformerLensOrg/TransformerLens/issues?q=is%3Aissue%20author%3A%40janmenjayap>`_.

Counting rules
--------------

* **Authored** means GitHub records ``janmenjayap`` as the PR or issue author.
* Open-PR line and file counts are snapshots, not final contribution sizes.
* Work on another contributor's PR is listed under collaboration, not authored
  PRs.
* GitHub's additions include source, tests, documentation, and notebook data.

Authored pull requests
----------------------

.. list-table:: 10 authored pull-request records
   :widths: 8 33 13 13 17 16
   :header-rows: 1

   * - PR
     - Title
     - Opened
     - Outcome
     - GitHub diff
     - Commits / files
   * - :pr:`1596`
     - J-space sparse decomposition
     - 2 Aug 2026
     - :status-merged:`Merged 14 Aug`
     - +1,613 / -3
     - 9 / 7
   * - :pr:`1676`
     - Occupancy and fraction-of-variance
     - 15 Aug 2026
     - :status-merged:`Merged 19 Aug`
     - +701 / -4
     - 3 / 7
   * - :pr:`1721`
     - Attention-head projection-kernel affinity
     - 24 Aug 2026
     - :status-merged:`Merged 28 Aug`
     - +1,620 / -0
     - 4 / 8
   * - :pr:`1723`
     - Backward Lens vocabulary readout
     - 25 Aug 2026
     - :status-merged:`Merged 4 Sep`
     - +4,125 / -0
     - 18 / 9
   * - :pr:`1735`
     - BERT Bridge-to-HF parity coverage
     - 1 Sep 2026
     - :status-merged:`Merged 1 Sep`
     - +114 / -0
     - 1 / 1
   * - :pr:`1738`
     - Jacobian Lens decomposition demo
     - 2 Sep 2026
     - :status-merged:`Merged 3 Sep`
     - +1,468 / -0
     - 3 / 4
   * - :pr:`1741`
     - Anchored J-space coordinate patching
     - 3 Sep 2026
     - :status-merged:`Merged 4 Sep`
     - +1,561 / -31
     - 11 / 10
   * - :pr:`1749`
     - Dynamic J-space coordinate-patch hooks
     - 5 Sep 2026
     - :status-open:`Open`
     - +880 / -244
     - 5 / 12
   * - :pr:`1750`
     - Node attribution-patching substrate
     - 6 Sep 2026
     - :status-open:`Open`
     - +1,029 / -0
     - 7 / 3
   * - :pr:`1752`
     - NeoX/Pythia unembedding compatibility
     - 6 Sep 2026
     - :status-open:`Open`
     - +165 / -3
     - 4 / 4

Merged authored totals
^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <section class="metric-grid metric-grid--compact" aria-label="Merged pull-request totals">
     <div class="metric"><strong>7</strong><span>merged PRs</span></div>
     <div class="metric"><strong>11,202</strong><span>additions</span></div>
     <div class="metric"><strong>49</strong><span>commits</span></div>
     <div class="metric"><strong>46</strong><span>changed-file entries</span></div>
   </section>

Authored issues
---------------

.. list-table:: 7 authored issue records
   :widths: 10 52 17 21
   :header-rows: 1

   * - Issue
     - Title
     - Opened
     - Outcome
   * - :issue:`1686`
     - Backward Lens: vocabulary readout of MLP gradient factors
     - 19 Aug 2026
     - :status-closed:`Closed 4 Sep`; :pr:`1723` merged
   * - :issue:`1720`
     - Projection-kernel affinity for attention-head weight subspaces
     - 24 Aug 2026
     - :status-closed:`Closed 28 Aug`; :pr:`1721` merged
   * - :issue:`1728`
     - Leakage-safe k-sparse probing over activation tensors
     - 30 Aug 2026
     - :status-open:`Open`; collaborative :pr:`1729`
   * - :issue:`1739`
     - J-space coordinate patching over sparse decompositions
     - 2 Sep 2026
     - :status-closed:`Closed 4 Sep`; :pr:`1741` merged
   * - :issue:`1742`
     - Attribution Patching + EAP/EAP-IG
     - 4 Sep 2026
     - :status-open:`Open`; :pr:`1750` active
   * - :issue:`1748`
     - Dynamic hooks for J-space coordinate patching
     - 5 Sep 2026
     - :status-open:`Open`; :pr:`1749` active
   * - :issue:`1751`
     - NeoX/Pythia unembedding regression on Transformers 5.13+
     - 6 Sep 2026
     - :status-open:`Open`; :pr:`1752` active

Collaborative contribution
--------------------------

.. list-table::
   :widths: 17 22 41 20
   :header-rows: 1

   * - Record
     - Role
     - Contribution
     - Snapshot status
   * - :pr:`1729`
     - Proposer, reviewer, commit author
     - Designed :issue:`1728`; coordinated overlapping work; prepared
       `cc6470f <https://github.com/janmenjayap/TransformerLens/commit/cc6470f9425beccafd191b066c0e36f8642a8d0b>`_
       for MPS, convergence, typed-result, and leakage-test hardening
     - Open; commit awaiting integration

Totals at a glance
------------------

.. list-table::
   :widths: 42 18 18 22
   :header-rows: 1

   * - Record type
     - Completed
     - Open
     - Other
   * - Authored pull requests
     - 7 merged
     - 3 open
     - None
   * - Authored issues
     - 3 closed
     - 4 open
     - None
   * - Non-authored collaboration PRs
     - 0 merged
     - 1 open
     - Credited separately