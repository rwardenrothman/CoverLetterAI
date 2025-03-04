# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Cover Letter AI'
copyright = '2025, Rob Warden-Rothman'
author = 'Rob Warden-Rothman'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    'myst_parser',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.plantuml',
]

source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = []
autosectionlabel_maxdepth = 3
autosectionlabel_prefix_document = True

myst_url_schemes = {
    "http": None,
    "https": None,
    "tel": {
        "url": "tel:{{path}}",
        "title": "{{path}}",
    },
    "mailto": {
        "url": "mailto:{{path}}",
        "title": "{{path}}",
    },
}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_theme_options = {
    'body_max_width': 'none'
}

plantuml = r'java -jar "C:\Users\rward\AppData\Local\JetBrains\PyCharm2024.3\markdown\download\plantumllanguageextension\plantuml.jar"'
plantuml_output_format = 'svg'