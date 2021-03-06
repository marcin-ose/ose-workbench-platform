"""Shared base configuration for OSE workbench documentation.
"""

# Configuration for Sphinx Python Documentation Generator
# https://www.sphinx-doc.org/en/master/usage/configuration.html
conf = {
    # Read the Docs Sphinx Theme
    # Designed for great reader experience on both desktop and mobile devices.
    # https://github.com/readthedocs/sphinx_rtd_theme
    'html_theme': 'sphinx_rtd_theme',

    # Whether module names are prepended to all object names
    # (for object types where a “module” of some kind is defined),
    # e.g. for py:function directives. Default is True.
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-add_module_names
    'add_module_names': False,

    # List of strings that are module names of extensions.
    # https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
    'extensions': [

        # Include documentation from docstrings
        # https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
        'sphinx.ext.autodoc',

        # For automatic generation of Sphinx sources that,
        # use the autodoc extension
        # https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
        'sphinx.ext.apidoc',

        # Generate autodoc summaries
        # https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
        'sphinx.ext.autosummary',

        # Helps with having many external links that point to the OSE Wiki.
        # https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
        'sphinx.ext.extlinks',

        # Enables localization of theme strings in translated output
        'sphinx_rtd_theme'
    ],

    # Base configuration for the above Sphinx extensions
    'ext': {
        'autodoc': {
            # List of modules to be mocked up.
            # Useful when some external dependencies are not met at build time,
            # and break the build process.
            # https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_mock_imports
            'autodoc_mock_imports': [
                'FreeCAD',
                'FreeCADGui',
                'Part',
                'PySide'
            ]
        },
        'extlinks': {
            # Dictionary of external sites,
            # mapping unique short alias names to a base URL and a prefix.
            # https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#confval-extlinks
            'extlinks': {
                'osewikipage': (
                    'https://wiki.opensourceecology.org/wiki/%s', ''
                )
            }
        }
    }
}
