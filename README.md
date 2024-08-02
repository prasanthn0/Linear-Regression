# Linear-Regression

y = mx + c 
where 
m is scale coefficient 
c is slope also known as bias factor or bias coefficient
x is independent variable 
y is dependent/outcome/response variable 

Given X - series of x ; predict Y  - series of y  :

                    Y = mX + c

Given y' - mean of dependent variable ; x' - mean of independent variable ; predict c i.e, intercept:

                    c = y' - mx'

Given y' - mean of dependent variable ; x' - mean of independent variable ; predict m i.e, slope:
                    
                    m = sum[(x-x')(y-y')] / sum[(x-x')^2]

R-squared : 

        Error  = Variance of target data points around the regression line / Variance of target data points around the mean
        R-squared = 1 - Error
        R-squared = 1 - sse/sst   #sse is error sum of squares & sst is total sum of squares
        R-squared = 1 - sum[(y - y_hat)^2]/sum[(y - y_)^2]

