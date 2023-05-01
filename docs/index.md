# test-pg-pythonpackage

This repository hosts a Python package used as a playground:
- The package <code>tp_package</code> implements basic arithmetic operations.
- Tests are implemented with <code>pytest</code>.
- Two Github workflows are added for CI: one leveraging Github actions, the other running a bash script (see <code>/scripts</code>). The CI runs linters (flake8 and pylint) as well as tests (pytest).
- GitHub pages are added and configures with <code>_config.yaml</code>
- The Python package is configured within <code>pyproject.toml</code>


To access documentation of the package, follow the [link to the tp_package documentation](/test-pg-pythonPackage/tp_package/functions.html).