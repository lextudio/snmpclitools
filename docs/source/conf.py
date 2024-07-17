#!/usr/bin/env python3
#
# PySNMP Applications documentation build configuration file, created by
# sphinx-quickstart on Wed Dec 20 23:37:20 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os

# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_sitemap",
    "sphinx_copybutton",
    "notfound.extension",
]

notfound_urls_prefix = "/snmpclitools/"

html_baseurl = "https://docs.lextudio.com/snmpclitools/"
sitemap_url_scheme = "{link}"
sitemap_suffix_included = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "SNMP Commands"
copyright = "2005-2019, Ilya Etingof. © Copyright 2022-2024, LeXtudio Inc."
author = "LeXtudio Inc. <support@lextudio.com>"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "0.7"
# The full version, including alpha/beta/rc tags.
release = "0.7.1"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
pygments_dark_style = "monokai"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "source_repository": "https://github.com/lextudio/snmpclitools",
    "source_branch": "main",
    "source_directory": "docs/source/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/lextudio/snmpclitools",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
}

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_title = "SNMP Commands Documentation"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "PySNMPApplicationsdoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "PySNMPApplications.tex",
        "PySNMP Applications Documentation",
        "Ilya Etingof",
        "manual",
    ),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "pysnmpapplications", "PySNMP Applications Documentation", [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "PySNMPApplications",
        "PySNMP Applications Documentation",
        author,
        "PySNMPApplications",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Configuration for Intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "pyasn1": ("https://pyasn1.readthedocs.io/", None),
    "pysmi": ("https://docs.lextudio.com/pysmi/", None),
}

# this merges constructor docstring with class docstring
autoclass_content = "both"
# Sort members by type
autodoc_member_order = "bysource"

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = False
napoleon_use_rtype = False


def setup(app):
    on_rtd = os.environ.get("READTHEDOCS", None) == "True"
    if not on_rtd:
        """Insert Google Analytics tracker
        Based on this Stackoverflow suggestion: https://stackoverflow.com/a/41885884
        """
        app.add_js_file("https://www.googletagmanager.com/gtag/js?id=G-DFLYZZK12P")
        app.add_js_file("google_analytics_tracker.js")
