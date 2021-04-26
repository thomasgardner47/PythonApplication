import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi, np.pi, 100)  # Sample 100 points between -pi and pi.
y = np.sin(x)  # Compute sin of the 100 points.
plt.figure()
plt.plot(x, y)
plt.title("$y = \sin(x)$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.savefig("sin.png", bbox_inches="tight")
plt.show()  # this is the last command
