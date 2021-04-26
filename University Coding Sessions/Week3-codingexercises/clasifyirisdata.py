from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


# always import when starting to code in python

# step 1 - load the data.

data = load_digits()
inputs = data.data
targets = data.target

# Classify the data.

classifier = MLPClassifier()
classifier.fit(inputs, targets)
outputs = classifier.predict(inputs)

# Compute and visualise the confusion matrix.

C = confusion_matrix(targets, outputs)
plt.imshow(C)
plt.colorbar()
plt.savefig("confusion.pdf", bbox_inches="tight")
plt.show()

