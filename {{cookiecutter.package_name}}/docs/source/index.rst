{{cookiecutter.package_display_name}}
{{cookiecutter.package_display_name|length * '#' }}

{{cookiecutter.package_short_description}}

.. toctree::
   :maxdepth: 2
   :numbered:
   :hidden:

   user/index
   api/index
   dev/index


Getting Started
===============

{{cookiecutter.package_display_name}} is available on PyPI and can be installed with `pip <https://pip.pypa.io>`_.

.. code-block:: console

    $ pip install {{cookiecutter.package_name}}

After installing {{cookiecutter.package_display_name}} you can use it like any other Python module.

Here is a simple example:

.. code-block:: python

    import {{cookiecutter.package_name}}
    # Fill this section in with the common use-case.
