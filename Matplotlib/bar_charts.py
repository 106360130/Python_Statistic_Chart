import numpy as np
import matplotlib.pyplot as plt

students = ['Jack', 'Mary', 'Mike', 'David']
math_scores = [78, 67, 90, 81]
x = np.arange(len(students))

plt.bar(x, math_scores, color=['red', 'green', 'blue', 'yellow'])
plt.xticks(x, students)
plt.xlabel('Students')
plt.ylabel('Math')
plt.title('Final Term')
plt.show()