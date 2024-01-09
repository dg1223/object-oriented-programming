from setuptools import setup

long_description = "This package contains code to perform basic mathematical operations on Gaussian and Binomial distributions. Operations include finding the mean, standard deviation (of both sample and population), plotting histograms for Gaussian distribution and plotting frequncy bar charts for Binomial distributions."

setup(name='dg_probability',
      version='0.2',
      description='Gaussian and Binomial distributions',
      long_description=long_description,
      long_description_content_type="text"
      packages=['dg_probability'],
      author="Shamir Alavi",
      author_email="dummy@e.mail",
      zip_safe=False)
