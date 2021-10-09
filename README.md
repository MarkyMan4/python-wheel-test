Package code is in the testwheel folder.

For testing, the package can be installed by running the following from the root directory of the project:
<code>pip install .</code>

Build the wheel by running <code>python setup.py bdist_wheel</code>

The .whl file will go to the dist folder. This file can then be installed using pip.

The key files for building the wheel are: 
- setup.cfg
- pyproject.toml
- setup.py