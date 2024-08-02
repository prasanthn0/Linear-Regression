import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Ordinary Least Squares
class OLS:
    def __init__(self, X , Y):
        self.X = X  # Series of independent variable
        self.Y = Y # Series of dependent variable
        
    def linear(self, m, c):
        Y = [m*x + c for x in self.X]
        return Y
    
    def slope(self):
        x_ = np.mean(self.X)
        y_ = np.mean(self.Y)
        
        covariance = sum([(x-x_)*(y-y_) for x,y in zip(self.X, self.Y)])
        variance = sum([(x-x_)**2 for x in self.X])
        
        return covariance/variance
    
    def intercept(self,m):
        x_ = np.mean(self.X)
        y_ = np.mean(self.Y)
        c = y_ - (m * x_)
        
        return c
    
    def predict(self):
        slope = self.slope()
        intercept = self.intercept(slope)
        predicted = self.linear(slope, intercept)
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
    data = pd.read_csv(r"Automobile_data.csv")
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
    predicted = ols.predict()
    ols.plot(predicted)
        
        
        
        
    
    