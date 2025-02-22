#!/usr/bin/env python3


# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys
import sphinx_rtd_theme
import recommonmark
from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath('.'))
# -- Project information -----------------------------------------------------

project = 'Hyperledger Indy HIPE'
copyright = '2024, Hyperledger Indy'
author = 'Hyperledger Indy'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''
nickname = 'hipe'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'recommonmark',
    'sphinx.ext.autosectionlabel',
]

# Prefix document path to section labels, otherwise autogenerated labels would look like 'heading'
# rather than 'path/to/file:heading'
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#

source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'text/index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'IndyProjectEnhancementsdoc'


# -- Options for LaTeX output ------------------------------------------------

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
    (master_doc, 'IndyProjectEnhancements.tex', 'Indy Project Enhancements Documentation',
     'Hyperledger Indy', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'indyprojectenhancements', 'Indy Project Enhancements Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'IndyProjectEnhancements', 'Indy Project Enhancements Documentation',
     author, 'IndyProjectEnhancements', 'Hyperledger Indy Project Enhancement (HIPE) Documents.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#


source_parsers = {
    '.md' : 'recommonmark.parser.CommonMarkParser',
}
# -------------- Additional fix for Markdown parsing support ---------------
# Once Recommonmark is fixed, remove this hack.
from recommonmark.states import DummyStateMachine
# Monkey patch to fix recommonmark 0.4 doc reference issues.
orig_run_role = DummyStateMachine.run_role
def run_role(self, name, options=None, content=None):
    if name == 'doc':
        name = 'any'
    return orig_run_role(self, name, options, content)
DummyStateMachine.run_role = run_role

def setup(app):
    app.add_config_value('recommonmark_config', {
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)

# ------------ Remote Documentation Builder Config -----------
# Note: this is a hacky way of maintaining a consistent sidebar amongst all the repositories. 
# Do you have a better way to do it?
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if(on_rtd):
    rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
    if rtd_version not in ['stable', 'latest']:
        rtd_version = 'latest'
    try:
        os.system("git clone https://github.com/hyperledger/indy-docs.git remote_conf")
        os.system("mv remote_conf/remote_conf.py .")
        import remote_conf
        remote_conf.generate_sidebar(globals(), nickname)
        intersphinx_mapping = remote_conf.get_intersphinx_mapping(rtd_version)
        master_doc = "toc"
    
    except:
        e = sys.exc_info()[0]
        print(e)
    finally:      
        os.system("rm -rf remote_conf/ __pycache__/ remote_conf.py")

