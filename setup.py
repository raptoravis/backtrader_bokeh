import setuptools
from distutils.util import convert_path

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

main_ns = {}
ver_path = convert_path('backtrader_bokeh/version.py')
with open(ver_path, encoding='utf-8') as ver_file:
    exec(ver_file.read(), main_ns)

setuptools.setup(
    name='backtrader_bokeh',
    version=main_ns['__version__'],
    description='Plotting package for Backtrader (Bokeh)',
    python_requires='>=3.6',
    author='Metaer',
    author_email='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GNU General Public License v3 or later (GPLv3+)',
    url="https://github.com/iniself/backtrader_bokeh",
    project_urls={
        "Bug Tracker": "https://github.com/iniself/backtrader_bokeh/issues",
        "Documentation": "https://github.com/iniself/backtrader_bokeh/wiki",
        "Source Code": "https://github.com/iniself/backtrader_bokeh",
        "Demos": "https://github.com/iniself/backtrader_bokeh/tree/gh-pages",
    },

    # What does your project relate to?
    keywords=['trading', 'development', 'finance', 'quant', 'backtrader', 'Bokeh'],

    packages=setuptools.find_packages(),
    package_data={'backtrader_bokeh': ['config.default.json', 'config.json', 'templates/*.j2', 'templates/js/*.js']},
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software Development"
    ],

    install_requires=[
        'backtrader',
        'bokeh>=2.4.3, <3.0.0',
        'jinja2',
        'pandas',
        'matplotlib==3.7.1',
    ],
)
