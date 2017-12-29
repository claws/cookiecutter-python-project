Developers Guide
################

.. include:: ../../../CONTRIBUTING.rst


.. _testing-label:

Testing
=======

The {{cookiecutter.package_display_name}} project implements a regression
test suite that improves developer productivity by identifying capability
regressions early.

Developers implementing fixes or enhancements must ensure that they have
not broken existing functionality. The {{cookiecutter.package_display_name}}
project provides some convenience tools so this testing step can be quickly
performed.

Use the Makefile convenience rules to run the tests.

.. code-block:: console

    (myvenv) $ make test

To run tests verbosely use:

.. code-block:: console

    (myvenv) $ make test.verbose

Alternatively, you may want to run the tests suite directly. The following
steps assume you are running in a virtual environment in which the
``{{cookiecutter.package_name}}`` package has been installed. If this is
not the case then you will likely need to set the ``PYTHONPATH`` environment
variable so that the ``{{cookiecutter.package_name}}`` package can be found.

.. code-block:: console

    (myvenv) $ cd tests
    (myvenv) $ python -m unittest

Individual unit tests can be run also.

.. code-block:: console

    (myvenv) $ python3 -m test_basic


.. _test-coverage-label:

Coverage
========

The ``coverage`` tool can be run to collect code test coverage metrics.

Use the Makefile convenience rule to run the tests.

.. code-block:: console

    (myvenv) $ make coverage

The test code coverage report can be found `here <../coverage/coverage.html>`_


.. _style-compliance-label:

Code Style
==========

Adopting a consistent code style assists with maintenance.

Use the Makefile convenience rule to check code style compliance and fix
problems if necessary.

.. code-block:: console

    (myvenv) $ make style.fix


.. _annotations-label:

Type Annotations
================

The code base contains type annotations to provide helpful type information
that can improve code maintenance.

Use the Makefile convenience rule to check no issues are reported.

.. code-block:: console

    (myvenv) $ make check_types


.. _documentation-label:

Documentation
=============

To rebuild this project's documentation, developers should use the Makefile
in the top level directory. It performs a number of steps to create a new
set of `sphinx <http://sphinx-doc.org/>`_ html content.

.. code-block:: console

    (myvenv) $ make docs

To quickly view the docs developers should use the Makefile in the top level
directory.

.. code-block:: console

    (myvenv) $ make docs.serve

This rule starts a simple Python web server in the directory that Sphinx
writes generated content into.
