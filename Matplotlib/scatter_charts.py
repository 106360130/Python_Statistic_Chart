import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 1]

plt.plot(x, y, 'o', label='o')
plt.plot(y, x, 'x', label='x')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Chart')
plt.show()