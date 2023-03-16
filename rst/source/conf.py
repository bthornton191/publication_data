# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.join(os.path.abspath('..\..')))
import pkg # type: ignore # noqa
project = pkg.project + ' v' + pkg.version
author = pkg.author
copyright = '2023, ' + author

# The full version, including alpha/beta/rc tags
release = pkg.version

# Compatible bearing plugin version
global_substitutions = {
}

# The master toctree document.
master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # 'sphinx_git',
    'sphinxemoji.sphinxemoji',
    # 'sphinxcontrib.fulltoc',
    'sphinxcontrib.globalsubs',
    'sphinx.ext.todo',
    'sphinx_design',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# html_sidebars = { '**': ['searchbox.html', 'relations.html', 'localtoc.html', 'globaltoc.html'] }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Specify custom css
html_css_files = ['css/custom.css']

# Figure numbering
numfig = True
numfig_format = {
    'figure': 'Figure %s',
    'table': 'Table %s',
    'code-block': 'Code %s',
}

math_numfig = True
math_eqref_format = "({number})"

# Browser Icon
# html_favicon = '_static/cdm.png'

todo_include_todos=True
todo_link_only = True
