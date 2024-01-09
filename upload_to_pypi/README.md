# **Gaussian and Binomial Distributions**
This package contains code to perform basic mathematical operations on Gaussian and Binomial distributions. Operations include finding the mean and standard deviation (of both sample and population), plotting histograms for Gaussian distribution and plotting frequncy bar charts for Binomial distributions.

## Input data
For Gaussian distribution, you can test the package using the following dummy input data.

```text
1
3
99
100
120
32
330
23
76
44
31
```

Here's some dummy data for a Binomial distribution. It contains the outcomes of 13 trials. A '0' denotes failure and a '1' denotes success.

```text
0
1
1
1
1
1
0
1
0
1
0
1
0
```

## Test the code
Type `python` in the terminal (Linux/Mac) then at the >>> prompt, type `from dg_probability import Gaussian`.
This will bring our code into memory for access. Lets try it.

```python
gaussian_one = Gaussian(10,5)
gaussian_one.mean
gaussian_one.stdev
```

Test the Binomial class by typing in the prompt `from dg_probability import Binomial`. Then try:

```python
binomial = Binomial(0.25,60)
binomial.mean
binomial.stdev
```

# Test the entire Binomial distribution module
Here's how you can test the entire Binomial distribution module using the dummy data shown in the 'Input data' section. Create a file called `data_binomial.txt` and add the dummy data for Binomial distribution to it. Save this file in the same directory where your code is.

```python
# ignore the import statement if you 
# already have the module imported
from dg_probability import Binomial

binomial = Binomial(0.4, 20)
binomial.read_data_file('data_binomial.txt')
binomial.calculate_mean()
binomial.calculate_stdev()
binomial.replace_stats_with_data()
binomial.plot_bar()
binomial.plot_bar_pdf()
```

### Source code
https://github.com/dg1223/object-oriented-programming/tree/main/upload_to_pypi
