project = "TransformerLens Contributions"
copyright = "2026, Janmenjaya Panda"
author = "Janmenjaya Panda"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_rtd_dark_mode",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "active_work.rst",
    "analysis_tools.rst",
    "contribution_index.rst",
    "engineering.rst",
    "jacobian_lens.rst",
]

extlinks = {
    "issue": (
        "https://github.com/TransformerLensOrg/TransformerLens/issues/%s",
        "issue #%s",
    ),
    "pr": (
        "https://github.com/TransformerLensOrg/TransformerLens/pull/%s",
        "PR #%s",
    ),
}

linkcheck_ignore = [
    r"https://transformer-circuits\.pub/2026/jacobian-lens/index\.html",
]

rst_prolog = """
.. role:: status-merged
.. role:: status-open
.. role:: status-closed
"""

html_theme = "sphinx_rtd_theme"
html_title = "Janmenjaya Panda | TransformerLens Contributions"
html_baseurl = "https://janmenjayap.github.io/TransformerLens-contributions/"
html_meta = {
    "description": (
        "A technical record of Janmenjaya Panda's open-source contributions "
        "to TransformerLens."
    ),
    "theme-color": "#006c67",
}
html_static_path = ["_static"]
html_show_sourcelink = False
html_show_sphinx = False

default_dark_mode = True

smartquotes = False