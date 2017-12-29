# This makefile has been created to help developers perform common actions.
# Most actions assume it is operating in a virtual environment where the
# python command links to the appropriate virtual environment Python.

STYLE_EXCLUDE_LIST := git status --porcelain --ignored | grep "!!" | grep ".py$$" | cut -d " " -f2 | tr "\n" ","
STYLE_MAX_LINE_LENGTH := 160
VENVS_DIR := $(HOME)/.venvs
VENV_DIR := $(VENVS_DIR)/{{cookiecutter.package_name}}

# Do not remove this block. It is used by the 'help' rule when
# constructing the help output.
# help:
# help: {{cookiecutter.package_display_name}} Makefile help
# help:

# help: help                           - display this makefile's help information
help:
	@grep "^# help\:" Makefile | grep -v grep | sed 's/\# help\: //' | sed 's/\# help\://'

# help: venv                           - create a virtual environment for development
venv:
	@test -d "$(VENVS_DIR)" || mkdir -p "$(VENVS_DIR)"
	@rm -Rf "$(VENV_DIR)"
	@python -m venv "$(VENV_DIR)"
	@/bin/bash -c "source $(VENV_DIR)/bin/activate && pip install pip --upgrade && pip install -r requirements.dev.txt && pip install -e ."
	@echo "Enter virtual environment using:\n\n\t$ source $(VENV_DIR)/bin/activate\n"


# help: clean                          - clean all files using .gitignore rules
clean:
	@git clean -X -f -d


# help: clean.scrub                    - clean all files, even untracked files
clean.scrub:
	git clean -x -f -d


# help: test                           - run tests
test:
	@python -m unittest discover -s tests


# help: test.verbose                   - run tests [verbosely]
test.verbose:
	@python -m unittest discover -s tests -v


# help: coverage                       - perform test coverage checks
coverage:
	@coverage run -m unittest discover -s tests
	@# produce html coverage report on modules
	@coverage html -d docs/source/coverage --include="src/{{cookiecutter.package_name}}/*"
	@# rename coverage html file for latter use with documentation
	@cd docs/source/coverage; mv index.html coverage.html


# help: style                          - perform pep8 check
style:
	@pycodestyle --exclude=.git,docs,$(shell $(STYLE_EXCLUDE_LIST)) --ignore=E309,E402 --max-line-length=$(STYLE_MAX_LINE_LENGTH) src/{{cookiecutter.package_name}} tests


# help: style.fix                      - perform check with autopep8 fixes
style.fix:
	@# If there are no files to fix then autopep8 typically returns an error
	@# because it did not get passed any files to work on. Use xargs -r to
	@# avoid this problem.
	@pycodestyle --exclude=.git,docs,$(shell $(STYLE_EXCLUDE_LIST)) --ignore=E309,E402 --max-line-length=$(STYLE_MAX_LINE_LENGTH) src/{{cookiecutter.package_name}} tests -q  | xargs -r autopep8 -i --max-line-length=$(STYLE_MAX_LINE_LENGTH)


# help: check_types                    - check type hint annotations
check_types:
	@cd src; MYPYPATH=$(VENV_DIR)/lib/python*/site-packages mypy -p {{cookiecutter.package_name}} --ignore-missing-imports


# help: docs                           - generate project documentation
docs: coverage
	@cd docs; rm -rf source/api/{{cookiecutter.package_name}}*.rst source/api/modules.rst build/*
	@cd docs; sphinx-apidoc -o ./source/api ../src/{{cookiecutter.package_name}}
	@cd docs; make html
	@cd docs; cp -R source/coverage build/html/.


docs.serve:
	@cd docs/build; python -m http.server

# help: dist                           - create a source distribution package
dist:
	@python setup.py bdist_wheel


# help: dist.test                      - test a source distribution package
dist.test: dist
	@cd dist && ../tests/test-dist.bash ./{{cookiecutter.package_name}}-*-py3-none-any.whl


# help: dist.upload                    - upload a source distribution package
dist.upload:
	@twine upload dist/{{cookiecutter.package_name}}-*-py3-none-any.whl


# Keep these lines at the end of the file to retain nice help
# output formatting.
# help:

.PHONY: \
	check_types clean clean.scrub coverage dist dist.test dist.upload
	docs help style style.fix test test.verbose venv
