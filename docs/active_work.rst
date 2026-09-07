.. _active-work:

Active Work
===========

This page is a point-in-time view of work that had not merged or closed by
**7 September 2026**. GitHub remains the authority for current status; active
diff sizes and review decisions can change after this snapshot.

Open authored pull requests
---------------------------

.. list-table::
   :widths: 12 34 18 18 18
   :header-rows: 1

   * - PR
     - Current slice
     - Opened
     - Change size
     - Related issue
   * - :pr:`1749`
     - Dynamic J-space coordinate-patch hooks
     - 5 Sep 2026
     - +880 / -244, 12 files
     - :issue:`1748`
   * - :pr:`1750`
     - Node attribution-patching substrate
     - 6 Sep 2026
     - +1,029 / -0, 3 files
     - :issue:`1742`
   * - :pr:`1752`
     - NeoX/Pythia unembedding compatibility
     - 6 Sep 2026
     - +165 / -3, 4 files
     - :issue:`1751`

Dynamic J-space hooks
^^^^^^^^^^^^^^^^^^^^^

:pr:`1749` carries anchored coordinate edits from a captured activation into a
live ``run_with_hooks`` or ``generate`` call. Review-sensitive decisions are
made visible in the PR: fail-fast behavior for inactive coordinates,
caller-owned cache shape, and one construction-time cost warning. Arbitrary
multi-slot permutations, causal benchmarks, and ``HookedTransformer`` support
remain deferred.

Attribution patching
^^^^^^^^^^^^^^^^^^^^

:pr:`1750` establishes the node model, filtered gradient cache, result contract,
and first-order scoring convention needed before edge scoring or integrated
gradients can be trusted. The follow-up sequence in :issue:`1742` covers EAP,
EAP-IG, faithfulness evaluation, oracle parity, and a demo.

NeoX/Pythia compatibility
^^^^^^^^^^^^^^^^^^^^^^^^^

:pr:`1752` resolves a concrete blocker found while broadening Backward Lens:
unembedding moved from ``embed_out`` to ``lm_head`` in newer Transformers
layouts. The current branch supports both layouts and aligns the
``TransformerBridge`` and ``HookedTransformer`` conversion paths.

Open authored issues
--------------------

.. list-table::
   :widths: 12 51 19 18
   :header-rows: 1

   * - Issue
     - Proposal or report
     - Opened
     - Implementation
   * - :issue:`1728`
     - Leakage-safe k-sparse probing over activation tensors
     - 30 Aug 2026
     - Collaborative :pr:`1729`
   * - :issue:`1742`
     - Attribution Patching + EAP/EAP-IG
     - 4 Sep 2026
     - Authored :pr:`1750`
   * - :issue:`1748`
     - Dynamic hooks for J-space coordinate patching
     - 5 Sep 2026
     - Authored :pr:`1749`
   * - :issue:`1751`
     - NeoX/Pythia unembedding regression
     - 6 Sep 2026
     - Authored :pr:`1752`

Collaboration queue
-------------------

:pr:`1729` is authored by Lorenzo Zane, not by me. My contribution is the
proposal in :issue:`1728`, coordination and review on the PR, and a focused
hardening `commit <https://github.com/janmenjayap/TransformerLens/commit/cc6470f9425beccafd191b066c0e36f8642a8d0b>`_
prepared for cherry-picking. At the snapshot date, that commit had not yet
entered the upstream PR history, so it is not counted in authored or merged PR
totals.

Status interpretation
---------------------

``Open`` means only that GitHub reported the record open at the snapshot time.
It does not imply maintainer approval, imminent merge, or a stable API. Merged
work is documented separately on :doc:`jacobian_lens`, :doc:`analysis_tools`,
and :doc:`engineering`.