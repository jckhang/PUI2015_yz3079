# PUI2015_yz3079_hw3

## Assignment 1

In assignment 1, 6 different distributions are drawn, specifically Normal, Poisson, Binomial, Chi-square, Exponential and Wald distribution. They are generated with regard to the same mean. So let the mean be mean, the generate functions are as follows,

mymean=100

np.random.normal(mu=mymean,sigma=1,n)

np.random.poisson(ld=mymean,n)

np.random.binomial(myn=mymean/0.5,myp=0.5,n)

np.random.chisquare(df=mymean, size=n)

np.random.exponential(bt=mymean, size=n)

np.random.wald(mu=mymean,scale=2,n)

We can infer from those plots of population mean against sample size that the larger is the sample size, the closer is the sample mean to the population mean.

## Assignment 2

Follow and understand the notebook and repeat the z-test and chisq test for employment in an unsubsidized job.