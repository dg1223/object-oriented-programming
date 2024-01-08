# How to Create a Python Package (pip)

- Create a folder (e.g. `distributions`) and move all your python scripts to it
    - There’s no need to do anything extra for the parent class
    - For child classes, import the parent classes in the following way:
        - `from .general_distribution import Distribution`
        - Our parent class `Distribution` is written in a file called `general_distribution.py`
        - Notice the dot `.` before the file name. This is a requirement in Python 3
- Create an `__init__.py` file in the same folder
    - This file is necessary for pip to understand that it is a Python package
    - When a package is imported, this is the file that;s executed first
    - It doesn’t have to contain anything
    - However, it is a good practice to import some of the classes in this file so that users do not have to import those classes using their full directory path
        - For example, the file may contain `from .gaussian_distribution import Gaussian`
        - It will help users import the Gaussian class by simply running `from distributions import Gaussian` → from **package_name** import **class**
- Create a file called `setup.py` in the same folder where the `distributions` folder is also stored
    - This file contains the metadata required to install the package
    - It contains name of the package, package version, description, the list of packages that are needed to be installed (including itself) and whatever additional metadata our package requires.
- Now we are ready to create the package. Make sure you are in the directory with the `distribution` folder and `setup.py` file. Then type `pip install .`

## **Testing the newly installed package**

Type `python` in the terminal (Linux/Mac) then at the >>> prompt, type `from distributions import Gaussian.`
This will bring our code into memory for access. Lets try it.

```python
gaussian_one = Gaussian(10,5)
gaussian_one.mean
gaussian_one.stdev
```

It is a good practice to install Python packages in a virtual environment so that there is no interference with the original Python installation.