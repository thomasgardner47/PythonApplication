import numpy as np 
from matplotlib import pyplot as plt 

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y)
plt.title("$y=sin(x)$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.savefig("sin.png", bbox_inches="tight")
plt.show()

###################################################
print (x)

uniform = np.random.rand(1000)
normal = np.random.randn(1000)

plt.figure()
plt.hist(uniform)
plt.figure()
plt.hist(normal)

# what this shows is the probability of generating data between 0 and 1 and what can be seen this is the probility has abit of noise but roughly the same. 

plt.figure()
plt.boxplot([uniform, normal])

# what can be seen above is a uniform boxplot with two distributions between 0 and 1, where the mean is about 0.5 and where those number are based 
# the other showing us that there is a much greater range and that we can be go negative and positive
