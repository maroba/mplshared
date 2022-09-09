# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os
sys.path.insert(0, os.path.join(os.path.abspath('..'), 'mplshared'))


project = 'mplshared'
copyright = '2022, Matthias Baer'
author = 'Matthias Baer'

version = '0.0.1'
release = '0.0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
              'matplotlib.sphinxext.plot_directive',
              'sphinx.ext.autodoc', 'sphinx.ext.imgmath', 'sphinx.ext.intersphinx',
              'sphinx.ext.napoleon',
              'IPython.sphinxext.ipython_console_highlighting',
              'IPython.sphinxext.ipython_directive', 'nbsphinx'
              ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
