# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Kim Kitsuragi'
author = 'Victor Ferat'
copyright = '2026, Victor Ferat'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']
templates_path = ['_templates']

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Edit Theme --------------------------------------------------------------
# https://pydata-sphinx-theme.readthedocs.io/en/v0.7.2/user_guide/configuring.html
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
  "github_url": "https://github.com/vferat/sphinx-portfolio", #TODO
  "icon_links": [
        {
            "name": "X",
            "url": "https://x.com/kim_kitsuragi", #TODO
            "icon": "fa-brands fa-x-twitter",
        },
        {
            "name": "ORCID",
            "url": "https://orcid.org/orcid-search/search?searchQuery=kim%20kitsuragi", #TODO
            "icon": "fa-brands fa-orcid",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/kim-kitsuragi-b54b88260/", #TODO
            "icon": "fa-brands fa-linkedin",
        },        
        ],
  "show_prev_next": False, # disable next/previous buttons
  "navbar_persistent" : [] # disable the search button
}

html_favicon = "_static/favicon.ico"
html_title = "Kim Kitsuragi"  #TODO

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_show_sourcelink = False

# -- Sidebar Options for HTML output -----------------------------------------
html_sidebars = {'index': ['sidebar.html'],
                 'about': ['sidebar.html'],
                 'publications': ['sidebar.html']}

# -- Bibliography ------------------------------------------------------------
extensions += ['sphinxcontrib.bibtex']
bibtex_bibfiles = ['bibliography.bib']


# -- Markdown syntax extension -----------------------------------------------
# Cards and grid
extensions += ['sphinx_design']
myst_enable_extensions = ["colon_fence"]

# toggle
extensions += ['sphinx_togglebutton']

# figures
numfig = True

# Equations
math_numfig = True

# Tabs
extensions += ['sphinx_tabs.tabs']

# Copy button
extensions += ['sphinx_copybutton']

# Spelling
extensions += [ 'sphinxcontrib.spelling' ]

# Inter sphinx
extensions += ["sphinx.ext.intersphinx"]

# Github context
html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "vferat", #TODO
    "github_repo": "sphinx-template",  #TODO
    "github_version": "main",
    "doc_path": "./source/",
}
html_theme_options["use_edit_page_button"] = False

# -- Referencing -------------------------------------------------------------
extensions += ['sphinx_sitemap']
html_baseurl = 'https://vferat.github.io' #TODO
html_extra_path = ["../.nojekyll"]