#Pandas is a Python module that is designed to facilitate reading a wide
#variety of formats – in this exercise you will load a CSV version of the Iris
#data and run it through your classifier.

# Load the data using Pandas. Print it to view it.
import pandas

import pandas as pd
import numpy as np


data = pandas.read_csv("iris.data")
print(data)


# Extract the inputs.
inputs = data.values[:,:-1].astype(float)
# Extract the targets - convert to numerical values to help with
# colouring when we plot the results.
cls = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
targets = [cls.index(c) for c in data.values[:,-1].astype(str)]
targets = np.array(targets)
