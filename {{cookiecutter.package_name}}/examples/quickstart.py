"""
This example script imports the {{cookiecutter.package_name}} package and
prints out the version.
"""

import {{cookiecutter.package_name}}


def main():
    print(
        f"{{cookiecutter.package_name}} version: {% raw -%}{{%- endraw %}{{cookiecutter.package_name}}.__version__{% raw -%}}{%- endraw %}"
    )


if __name__ == "__main__":
    main()
