u2p050-twitterfetcher
-------



Project Documentation
-------

-- You Need To fill up this section --

Requirements
-------

This project will need certain dependencies for you dev environnements (pip, pipenv and awscli),
Those dependencies can be installed by running `make dep`.

You can also install everything needed the first time you install this project by running:

.. code-block::
    $ make welcome

This will run ``make env-dev``.


How to use
-------

You will need first to install awscli if it's not done and configure it with our devops.
The first step before starting to dev is to unsure that the minimum dependencies are installed before you start working:

.. code-block::
    make env-dev

To clean everything (venv etc ...)

.. code-block::
    make clean

This command will create the virtualenv (if it doesn't exist).

You can then open a shell into the virtualenv using:

.. code-block::
    source .venv/bin/activate

To logout use ``Ctrl+D``.

Add dependencies
~~~~~~~

Inside the virtualenv:

```bash
    pip3 install {my_dependency}
```
You will need to update the ``requirements.txt``.

Run Test
~~~~~~~

.. code-block::
    make test

Run Linter
~~~~~~~

.. code-block::
    make lint

Format code
~~~~~~~

.. code-block::
    make fmt

Clean all project file
~~~~~~~

.. code-block::
    make clean

Aditional informations
-------

There is a default `setup.py` with this project.
You should expand the default arguments for the make run command as your project gets bigger.

Test and Lint
~~~~~~~

This project contains a pre-commit hook which will prevent pushing code that doesn't pass the linter
or with test that failed.
Tools used for linting are ``pylint``, ``isort``, ``black``, ``mypy``.

The docstrings follows google convention.