import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

students = ['Jack', 'Mary', 'Mike', 'David']
math_scores = [78, 67, 90, 81]
x = np.arange(len(students))
cmap = cm.jet(np.linspace(0, 1, len(students)))

plt.barh(x, math_scores, color=cmap)
plt.yticks(x, students)
plt.ylabel('Students')
plt.xlabel('Math')
plt.title('Final Term')
plt.show()