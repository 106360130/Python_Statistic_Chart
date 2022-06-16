import numpy as np
import matplotlib.pyplot as plt

students = ['Jack', 'Mary', 'Mike', 'David']
math_scores = [78, 67, 90, 81]
history_scores = [94, 71, 65, 88]
x = np.arange(len(students))

plt.bar(x, math_scores, color='blue', label='Math')
plt.bar(x, history_scores, color='green', label='History', bottom=math_scores)
plt.xticks(x, students)
plt.xlabel('Students')
plt.ylabel('Math')
plt.title('Final Term')
plt.legend(bbox_to_anchor=(1,1), loc='upper left')
plt.show()