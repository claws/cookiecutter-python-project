Cookiecutter Python Project
###########################

This project contains a Cookiecutter template that helps you create new Python
3.6+ package projects by automatically generating most of the boiler plate
content for you.

Cookiecutter is a command-line utility that creates projects from templates.
Cookiecutter lets you to easily and quickly bootstrap a new project from a
template which allows you to skip all manual setup and common mistakes when
starting a new project.

Cookiecutter takes a source directory tree and copies it into your new project.
It replaces all the names that it finds surrounded by templating tags ``{{``
and ``}}`` with names that it finds in the file ``cookiecutter.json``.

The Python project structure produced by this Cookiecutter template contains
the following items:

- A minimal README.rst file.
- A Makefile that automates many common developer tasks, such as:

  - Creating a Virtual environment
  - Checking code style.
  - Performing static analysis checks.
  - Running unit tests.
  - Checking code coverage.
  - Generating documentation.
  - Generating, testing and uploading a project release to PyPI.

- A ``setup.py`` file used to generate project install and releases.
- A ``CONTRIBUTING.rst`` guide. On Github this file is shown when sending
  a pull request or an issue. This file also gets included in the generated
  developer documentation.
- An empty ``CHANGELOG.rst`` file. This file gets included in the user
  documentation.
- A ``License`` file that defaults to the MIT License. Change this if
  you choose a license other than MIT.
- An ``examples`` directory with a minimal quickstart example script. This
  script imports the package and prints the package version. It is also
  called by the unit test suite to ensure it always works.
- A ``tests`` directory containing a basic unit test (using unittest) and
  a shell script that can be used to test a wheel distribution of the
  package.
- A Github Actions continuous integration configuration.
- A ``docs`` directory with pre-configured Sphinx documentation containing:

  - A minimal ``index.rst`` page

  - A user focused page containing information such as installation
    instructions, API docs, a link to the change log and instructions
    about how to raise a bug.

  - A developer focused page containing information such as contributing,
    testing, code coverage, style compliance, type annotations and
    documentation.

It is assumed that the new Python package will eventually be:

- hosted on Github (or perhaps GitLab)
- published to PyPI
- linked to ReadTheDocs.

The generated docs have some references and links to those sites.


Getting Started
===============

One Time Setup Steps
--------------------

The process for using Cookiecutter to create a new Python package project
starts with installing Cookiecutter. This is best done by creating a new
virtual environment specifically for cookiecutter and then installing
cookiecutter using ``pip``. The example below shows how to do this.

.. code-block:: console

    $ python -m venv ccvenv --prompt cc
    $ source ccvenv/bin/activate
    (cc) $ pip install pip -U  # update pip to avoid any warnings
    (cc) $ pip install cookiecutter

You are now ready to create a new Python project from the Cookiecutter
template provided by this project.


Create a new project
--------------------

To create a new Python package project based on this cookiecutter template
simply navigate to a directory where you want to create the new project, then
run the ``cookiecutter`` command with a command line argument referencing this
template.

The easiest method is to reference this template via its Github URL (where 'gh'
is a shortened form for Github):

.. code-block:: console

    (cc) $ cookiecutter gh:claws/cookiecutter-python-project

Alternatively, if you have cloned a local copy of this template you can
reference it directly:

.. code-block:: console

    (cc) $ cookiecutter path/to/cookiecutter-python-project

You will be prompted for user input to configure the project. Prompts are the
keys in 'cookiecutter.json' and default responses are the values. Prompts are
shown in order.

Once you have generated your new Python package project you can exit the
cookiecutter virtual environment as it is no longer required.

.. code-block:: console

    (cc) $ deactivate
    $


Manual Modifications
--------------------

Some aspects of generating a project in a generic approach are not practical
to completely automate so there may be a few steps remaining before you begin
using the new project.

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
the template in this project. In this scenario the project is called
``abc 123`` and the Python package is called ``abc_123``.

It is assumed that you have performed the actions outlined in the One Time
Setup Steps section above which provides a virtual environment with
cookiecutter installed into it.

After running the cookiecutter command and passing it a reference to this
template the first question it asks for is the package display name. This is
the human friendly label that will be used in docs to refer to the project. It
is also used to create the package name so it should not contain special
characters that are invalid when used in a Python attribute. It can have spaces
and hyphens in it. The package display name is first converted to lowercase
text and then any spaces or hyphens are converted to underscores to produce a
Python package name.

.. code-block:: console

    (ccenv) $ cookiecutter ../cookiecutter-python-project/
    package_display_name [Package-Name]: abc 123
    package_name [abc_123]:
    package_short_description [A description of the package]: This is my abc 123 package.
    version [0.0.1]:
    full_name [Your Name]: First Last
    email []:
    github_user_name [GithubUserName]: flast
    github_repo_name [abc_123]:
    Select license:
    1 - MIT license
    2 - BSD license
    3 - Apache Software License 2.0
    4 - GNU General Public License v3
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]:
    year [2018]:

The project has been created in the ``abc_123`` directory.

.. code-block:: console

    $ cd abc_123

We can now kick the tires of this new project by performing some initial
project checks.

First, let's create a project specific virtual environment and activate it.
This will install all of the project's development dependencies as well as
the project itself. The project will be installed as an editable package (by
using the ``-e`` flag to ``pip``).

.. code-block:: console

    $ make venv
    ...
    Enter virtual environment using:

      	source venv/abc_123/bin/activate

    $ source venv/abc_123/bin/activate
    (abc_123) $

Now that we have a virtual environment we can check the remaining convenience
functions provided by the Makefile.

.. code-block:: console

    (abc_123) $ make style
    (abc_123) $ make check-style
    (abc_123) $ make check-static-analysis
    (abc_123) $ make test
    (abc_123) $ make test-verbose
    (abc_123) $ make coverage
    (abc_123) $ make check-docs
    (abc_123) $ make docs
    (abc_123) $ make serve-docs  # in browser navigate to http://localhost:8000/html
    (abc_123) $ make dist
    (abc_123) $ make dist-test
