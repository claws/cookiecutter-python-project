Contributing Guide
==================

Contributions are welcome and greatly appreciated!

.. _contributing-expectations-label:

Expectations
------------

Before you submit a pull request, check that it meets these guidelines:

1. A pull request should cover one bug-fix or enhancement feature.

2. A pull request should preferably only have one commit upon the
   current master HEAD, (via rebases and squash).

3. If the pull request contains code changes then:

  - it should include tests (in the ``tests`` directory) that specifically
    verify the behaviour of the modification.

  - it should be style compliant (``make style`` and ``make style.fix``
    can be useful here).

  - it should include type annotations where appropriate
    (``make check_types`` can be useful here).

  - if the code changes are non-trivial:

    - the docs should be updated.
    - the change log should be updated.

4. The tests run cleanly.

5. The docs build runs cleanly.


.. _contributing-workflow-label:

Workflow
--------

The workflow that developers typically use to fix a bug or add enhancements
follows this sequence:

* Fork the ``{{cookiecutter.github_repo_name}}`` repo.

* Obtain the source.

  .. code-block:: console

      $ git clone git@github.com:your_name_here/{{cookiecutter.github_repo_name}}.git
      $ cd {{cookiecutter.package_name}}

* Create a branch for local development:

  .. code-block:: console

      $ git checkout -b name-of-your-bugfix-or-feature

  Now you can make your changes locally.

* Familiarize yourself with the developer convenience rules in the Makefile.

  .. code-block:: console

      $ make help

* Create and activate a Python virtual environment for local development.

  .. code-block:: console

      $ make venv
      $ source path/to/myvenv/bin/activate
      (myvenv) $

  These instructions create the virtual environment outside the repo
  directory so that it never accidentally gets added to the change
  set.

* Develop fix or enhancement:

  * Make a fix or enhancement (e.g. modify a class, method, function, module,
    etc).

  * Update an existing unit test or create a new unit test module to verify
    the change works as expected.

  * Run the test suite.

    .. code-block:: console

        (myvenv) $ make test

  * Check code coverage of the area of code being modified.

    .. code-block:: console

        (myvenv) $ make coverage

    Review the output produced in ``docs/source/coverage/coverage.html``.

  * Perform style check.

    .. code-block:: console

        (myvenv) $ make style

    Use the ``style.fix`` rule to automatically fix minor issues.

  * Perform type annotations check.

    .. code-block:: console

        (myvenv) $ make check_types

  * Fix any errors or regressions.

* Commit your changes and push them to your branch (e.g. Github, Gitlab):

  .. code-block:: console

      $ git add .
      $ git commit -m "A detailed description of the changes."
      $ git push origin name-of-your-bugfix-or-feature

* Check automated continuous integration steps all pass. Fix any problems
  if necessary.

* Submit a pull request through the service website (e.g. Github, Gitlab).
