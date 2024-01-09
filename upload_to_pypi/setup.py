from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='dg_probability',
      version='0.2',
      description='Gaussian and Binomial distributions',
      long_description=long_description,
      long_description_content_type="text",
      packages=['dg_probability'],
      author="Shamir Alavi",
      author_email="dummy@e.mail",
      zip_safe=False)
