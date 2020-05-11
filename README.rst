pytest-datafixtures
===================
https://github.com/idlesign/pytest-datafixtures

|release| |lic| |ci| |coverage|

.. |release| image:: https://img.shields.io/pypi/v/pytest-datafixtures.svg
    :target: https://pypi.python.org/pypi/pytest-datafixtures

.. |lic| image:: https://img.shields.io/pypi/l/pytest-datafixtures.svg
    :target: https://pypi.python.org/pypi/pytest-datafixtures

.. |ci| image:: https://img.shields.io/travis/idlesign/pytest-datafixtures/master.svg
    :target: https://travis-ci.org/idlesign/pytest-datafixtures

.. |coverage| image:: https://img.shields.io/coveralls/idlesign/pytest-datafixtures/master.svg
    :target: https://coveralls.io/r/idlesign/pytest-datafixtures


Description
-----------

*Data fixtures for pytest made simple*

Offers fixtures for your tests to simplify data fixtures access.
Makes use of Python's native ``Path`` objects.

Data fixtures (files) expected to be stored in ``datafixtures`` directory next to your test modules::

    tests
    |-- datafixtures
    |-- test_basic.py
    |
    |-- subdirectory
    |---- datafixtures
    |---- test_basic.py



**Fixtures**

* ``datafix_dir`` - Path object for data fixtures directory from the current test module's directory
* ``datafix`` - Path object for a file in data fixtures directory with the same name as the current test function


datafix_dir
~~~~~~~~~~~~~~~

Access data fixtures directory:

.. code-block:: python

    def test_me(datafix_dir):

        # datafix_dir returns a Path object.
        assert datafix_dir.exists()

        # Gather data fixtures filenames.
        files = list(f'{file.name}' for file in datafix_dir.iterdir())

        # Read some fixture as text.
        filecontent = (datafix_dir / 'expected.html').read_text()

        # Or read binary.
        filecontent = (datafix_dir / 'dumped.bin').read_bytes()


datafix
~~~~~~~

Access a data fixture with test name:

.. code-block:: python

    def test_me(datafix):
        # Read datafixtures/test_me.txt file
        filecontents = datafix.with_suffix('.txt').read_text()


Requirements
------------
* Python 3.6+