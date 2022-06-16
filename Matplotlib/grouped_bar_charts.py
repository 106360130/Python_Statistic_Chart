import numpy as np
import matplotlib.pyplot as plt

students = ['Jack', 'Mary', 'Mike', 'David']
math_scores = [78, 67, 90, 81]
history_scores = [94, 71, 65, 88]
x = np.arange(len(students))
width = 0.3

plt.bar(x, math_scores, width, color='green', label='Math')
plt.bar(x + width, history_scores, width, color='blue', label='History')
plt.xticks(x + width / 2, students)
plt.ylabel('Math')
plt.title('Final Term')
plt.legend(bbox_to_anchor=(1,1), loc='upper left')
plt.show()