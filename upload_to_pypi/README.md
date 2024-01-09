# **Gaussian and Binomial Distributions**
This package contains code to perform basic mathematical operations on Gaussian and Binomial distributions. Operations include finding the mean and standard deviation (of both sample and population), plotting histograms for Gaussian distribution and plotting frequncy bar charts for Binomial distributions.

## Test the code
Type `python` in the terminal (Linux/Mac) then at the >>> prompt, type `from distributions import Gaussian`.
This will bring our code into memory for access. Lets try it.

```python
gaussian_one = Gaussian(10,5)
gaussian_one.mean
gaussian_one.stdev
```

Test the Binomial class by typing in the prompt `from distributions import Binomial`. Then try:

```python
binomial = Binomial(0.25,60)
binomial.mean
binomial.stdev
```
