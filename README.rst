Cookiecutter Python Project
###########################

This project contains a Cookiecutter template to create new Python 3.6+
projects. This approach takes lots of the boiler plate out of creating new
Python projects.

Cookiecutter is a command-line utility that creates projects from templates.
Cookiecutter lets you to easily and quickly bootstrap a new project from a
template which allows you to skip all manual setup and common mistakes when
starting a new project.

Cookiecutter takes a source directory tree and copies it into your new
project. It replaces all the names that it finds surrounded by templating
tags ``{{`` and ``}}`` with names that it finds in the file
``cookiecutter.json``.

The Python project structure produced by this Cookiecutter template
contains the following items:

  - A minimal README.rst file.
  - A Makefile that automates common developer tasks, such as:
    - Run unit tests.
    - Run code coverage checks.
    - Run style compliance checks.
    - Run type annotations checks.
    - Generate documentation.
    - Generate, test and upload a project release to PyPI.
  - A ``setup.py`` file used to generate project install and releases.
  - A ``CONTRIBUTING.rst`` guide. On Github this file is shown when sending
     a pull request or an issue. This file gets included in the generated
     documentation.
  - an empty ``CHANGELOG.rst`` file. This file gets included in the documentation.
  - A ``License`` file that defaults to the MIT License. Change this if
    you choose a license other than MIT.
  - A ``tests`` directory containing a basic unit test (using unittest) and
    a shell script that can be used to test a wheel distribution of the
    package.
  - A ``.travis.yml`` file for continuous integration setup.
  - A ``docs`` directory with a pre-configured Sphinx documentation setup. It
    contains:
    - A minimal index.rst page
    - A user focused page containing information such as install, API
      and a link to the change log.
    - A change log file.
    - A developer focused page containing information such as contributing,
      testing, code coverage, style compliance, type annotations and
      documentation.
  - An ``examples`` directory with a minimal example script. This script is
    called and tested as part of the unit tests.

It is assumed that the new Python package will eventually be:

  - hosted on Github (or perhaps GitLab)
  - published to PyPI (using bdist_wheel)
  - linked to ReadTheDocs.

The generated docs have some references and links to those sites.


Getting Started
===============

.. _one-time-setup-steps-label:

One Time Setup Steps
--------------------

You need to prepare two locations to store content:

  - A place where you store your projects (git repositories). You probably
    have a folder for that already (e.g. ``git-repos``). We will call this
    location $REPOS_DIR.

  - A place to store Python virtual environments. Avoid putting your virtual
    environment in your project directory next to your code. This will avoid
    accidentally adding venv content to a git change set. We will call this
    location $VENVS_DIR.

Create a new virtual environment for cookiecutter and install cookiecutter
using ``pip``:

.. code-block:: console

    $ python -m venv $VENVS_DIR/ccenv
    $ source $VENVS_DIR/ccenv/bin/activate
    (ccenv) $
    (ccenv) $ pip install cookiecutter

You are now ready to create a new Python project from the Cookiecutter
template provided by this project.


.. _create-new-project-label:

Create a new project
--------------------

To create a new Python project based on a cookiecutter template simply
navigate to a directory where you want to create the new project (e.g
$REPOS_DIR) and run the ``cookiecutter`` command with this template as a
command line argument.

If you have cloned a local copy of this template you can use that:

.. code-block:: console

    (ccenv) $ cookiecutter path/to/cookiecutter-python-project

Alternatively you can create a new project by referencing this template
at Github (where gh is an abbreviated shortened form for Github):

.. code-block:: console

    (ccenv) $ cookiecutter gh:claws/cookiecutter-python-project

You will be prompted for input unless you suppress it with --no-input:

  - Prompts are the keys in cookiecutter.json.
  - Default responses are the values in cookiecutter.json.
  - Prompts are shown in order.

You should now have a new Python project. Once you have created the project
you can exit the cookiecutter virtual environment.

.. code-block:: console

    (ccenv) $ deactivate
    $


Manual Modifications
--------------------

Some aspects of generating a project in a generic approach are not practical
to completely automate so there may be a few steps remaining before you can
use the new project.

- If you specify a license other than MIT then you will need to update the
  ``LICENSE`` file to contain your license content. By default it contains
  a MIT License.

- If you do not plan to publish project artifacts at GitHub, PyPI or
  ReadTheDocs then remove any links to those sites. Affected files are:

    - README.rst
    - setup.py
    - docs/source/index.rst

- Update any additional useful classifiers in ``setup.py``. The list of
  available classifiers can be found `here <https://pypi.python.org/pypi?:action=list_classifiers>`_.


Example
=======

Below is an example showing exactly how to create a new Python project using
this project. In this case the package is called ``example``.

At this point it is assumed that you have performed the actions outlined in
:ref:`one-time-setup-steps-label`. This provides a virtual environment that
makes cookiecutter available.

Create the ``example`` project using cookiecutter.

.. code-block:: console

    (ccenv) $ cookiecutter ../python-project-template
    package_name [package_name]: example
    package_display_name [example]: Example
    package_short_description [A description of the package]: This package provides example capability
    version [0.0.1]:
    full_name [Your Name]: First Last
    email []:
    github_user_name [GithubUserName]: flast
    github_repo_name [example]:
    Select license:
    1 - MIT license
    2 - BSD license
    3 - Apache Software License 2.0
    4 - GNU General Public License v3
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]:
    year [2017]:
    (ccenv) $ deactivate

Perform initial project checks.

.. note::

    The ``make style`` step will raise the following git-related error because the
    project is not yet controlled by git. This error will not be seen once the
    project is under version control.

    .. code-block::

        fatal: Not a git repository (or any of the parent directories): .git

.. code-block:: console

    $ cd example
    $ make venv
    ...
    Enter virtual environment using:

      	source path/to/venvs/example/bin/activate

    $ source path/to/venvs/example/bin/activate
    (example) $
    (example) $ make style
    (example) $ make check_types
    (example) $ make test
    (example) $ make test.verbose
    (example) $ make coverage
    (example) $ make docs
    (example) $ make docs.serve  # in browser navigate to http://localhost:8000/html
    (example) $ make dist
    (example) $ make dist.test
