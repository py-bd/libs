import matplotlib as plot
import matplotlib.pyplot as plt

plot.use("TKAgg")

# create data of complex numbers
data = [1 + 2j, -1 + 4j, 4 + 3j, -4, 2 - 1j, 3 + 9j, -2 + 6j, 5]

# extract real part
x = [ele.real for ele in data]
# extract imaginary part
y = [ele.imag for ele in data]

plt.scatter(x, y)

plt.ylabel('Imaginary')
plt.xlabel('Real')

plt.show()
