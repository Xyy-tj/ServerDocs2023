# -- Path setup --------------------------------------------------------------

import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = "NaMI Server Docs"
copyright = "2020, nami-442"
author = "nami-442"


# -- General configuration ---------------------------------------------------

extensions = ["sphinx_rtd_theme", "recommonmark"]
templates_path = ["_templates"]
exclude_patterns = []
master_doc = "index"


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

