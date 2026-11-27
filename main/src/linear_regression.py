import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 9, 7, 11])

class CustomLinearRegression:
    
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias

    def predict(self, x):
        return self.weight*x + self.bias 

model = CustomLinearRegression(2, 1)
print(model.predict(x))