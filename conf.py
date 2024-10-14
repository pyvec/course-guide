# Configuration file for the Sphinx documentation builder

import os
import sys


# -- Environment -------------------------------------------------------------

# Explicitly put the extensions directory to Python path
sys.path.append(os.path.abspath("_extensions"))


# -- Project information -----------------------------------------------------

project = "Dokumentace české Python komunity"
copyright = "2023, Pyvec, z.s."
author = "Pyvec, z.s."

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = ""


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
    "sphinxemoji.sphinxemoji",
    "slack",
    "twitter",
    "gh_repo",
    "myst_parser",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "cs"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "venv",
    ".venv",
    ".github",
    ".pytest_cache",
    ".ruff_cache",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "monokai"


# -- Options for HTML output -------------------------------------------------

# Set canonical URL from the Read the Docs Domain
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"
html_logo = "_static/images/org-i.svg"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "pyvec-doc"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "pyvec.tex", project, author, "manual"),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "pyvec", project, [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, "pyvec", project, author, "pyvec", project, "Miscellaneous"),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]


# -- Extension configuration -------------------------------------------------

linkcheck_ignore = [
    r"http://127\.0\.0\.1:\d+",  # localhost
    r"https://docs\.google\.com/.+",  # links to private documents
    r"https://twitter\.com/.+",  # crawling/DDoS protection
    r"https://(www\.)?buffer\.com.*",  # crawling/DDoS protection
    r"https://www\.nytimes\.com/.*",  # crawling/DDoS protection
    r"https://cz\.pycon\.org/\d+/.+",  # see https://pyvec.slack.com/archives/C4PPZNPDK/p1617716799001200
    r"https://github\.com/[^/]+/[^/]+/commits/.+",  # GitHub aggressively rate-limits these
]


# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for the emoji extension -----------------------------------------

# Ensures consistent emoji style on all computers, operating systems, browsers
sphinxemoji_style = "twemoji"


# -- Setting up extensions ---------------------------------------------------


def setup(app):
    app.add_css_file("custom.css")
    app.add_js_file("redirect.js")
