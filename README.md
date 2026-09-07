# TransformerLens Contributions

A source-linked technical record of Janmenjaya Panda's contributions to
[TransformerLens](https://github.com/TransformerLensOrg/TransformerLens),
including research features, numerical validation, model compatibility work,
proposals, and collaboration.

The documentation uses Sphinx and includes an automated GitHub Pages
deployment.

## Site contents

- **Home** introduces the contribution record and its scope.
- **Overview** presents the project, mentor, verified statistics, and a detailed
  mathematical account of Jacobian Lens, J-space, Backward Lens, Projection
  Kernel, attribution patching, sparse probing, and model compatibility.
- **Project Work** provides a source-linked table of authored pull requests,
  related issues, code statistics, outcomes, and separately credited
  collaboration.

Contribution data is a snapshot verified against GitHub on 7 September 2026.
Live GitHub records remain authoritative as statuses change.

## Build locally

Create and activate a virtual environment, then install the pinned dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Build the site with warnings treated as errors:

```bash
make -C docs html
open docs/_build/html/index.html
```

Generated HTML is written to `docs/_build/html` and is intentionally ignored by
Git.

## Publish with GitHub Pages

The workflow in `.github/workflows/deploy-docs.yml` builds and deploys the site
on every push to `main`. In the repository's GitHub settings, select **GitHub
Actions** as the Pages source once; subsequent pushes deploy automatically.

The expected public URL is:

<https://janmenjayap.github.io/TransformerLens-contributions/>

The deployment job uses the same warning-as-error Sphinx command as the local
build, so unresolved references and malformed documentation block publication.
