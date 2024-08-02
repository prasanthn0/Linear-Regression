import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Ordinary Least Squares  - Calculating slope and y-intercept
class OLS:
    def __init__(self, X , Y):
        self.X = X  # Series of independent variable
        self.Y = Y # Series of dependent variable
        
    def get_mean(self,arr):
        return np.mean(arr)

    # variance
    def get_variance(self,arr, mean):
        return np.sum((arr-mean)**2)

    # covariance
    def get_covariance(self,arr_x, mean_x, arr_y, mean_y):
        final_arr = (arr_x - mean_x)*(arr_y - mean_y)   # [(x-x_)*(y-y_) for x,y in zip(self.X, self.Y)]
        return np.sum(final_arr)
        
    def linear(self, m, c, X):
        print(m)
        Y = [m*x + c for x in X]
        return Y
    
    def get_slope(self):
        x_ = self.get_mean(self.X)
        y_ = self.get_mean(self.Y)
        
        covariance = self.get_covariance(self.X, x_, self.Y, y_)
        variance = self.get_variance(self.X, x_)
        
        return covariance/variance
    
    def get_intercept(self,m):
        x_ = self.get_mean(self.X)
        y_ = self.get_mean(self.Y)
        
        c = y_ - (m * x_)
        
        return c
    
    def fit_linear(self):
        self.slope = self.get_slope()
        self.intercept = self.get_intercept(self.slope)
        
    def predict(self, pred_X):
        predicted = self.linear(self.slope, self.intercept, pred_X)
        return predicted
    
    def r_squared_error(self, Y_hat):
        # R-squared value or co-efficient of determination
        # It is a measure of how close is the fitted data to the actual data . Larger the R-squared value , better is the fit
        y_ = np.mean(self.Y)
        
        sse = sum([(y-y_hat)**2 for y,y_hat in zip(self.Y, Y_hat)])
        sst = sum([(y-y_)**2 for y in self.Y])
        
        r_sqr = 1 - (sse/sst)
        
        return r_sqr
    
    def plot(self, Y_hat):
        plt.figure(figsize=(8, 5))
        plt.plot(self.X, Y_hat, color='#f25f5c')
        plt.scatter(self.X, Y_hat, color='#f25f5c')
        plt.title('Predicted values by Linear Regression', fontsize=15)
        plt.xlabel('engine-size')
        plt.ylabel('price')
        plt.scatter(self.X, self.Y, color="#247ba0")

        # Save the plot as a PNG file
        plt.savefig('predicted_values.png')
        
    
if __name__ == '__main__':
    data = pd.read_csv(r"data/raw/Automobile_data.csv")
    data = data.loc[data['price']!='?']
    print(data['price'].value_counts()[:5])
    try:
        data[['price']] = data[['price']].astype(int)
    except ValueError:
        print("Trying out the line of code above will result to this error:\n")
        print("Value Error: invalid literal for int() with base 10: '?'")
    X = data['engine-size']
    Y = data['price']
    ols = OLS(X,Y)
    ols.fit_linear()
    predicted = ols.predict(X)
    ols.plot(predicted)
        
        
        
        
    
    