import numpy as np
import matplotlib.pyplot as plt
uniform = np.random.rand(100)  # Generate 100 uniform random points.
normal = np.random.randn(100)  # Generate 100 normal random points.
plt.figure()
plt.boxplot([uniform, normal])
plt.xticks([1, 2], ["Uniform", "Normal"])
plt.ylabel("$p(x)$")
plt.savefig("boxplot.png", bbox_inches="tight")
plt.show()
