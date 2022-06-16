import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 1]

plt.plot(x, y, 'ro-', label='o')
plt.plot(y, x, 'gx--', label='x')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Chart')
plt.show()