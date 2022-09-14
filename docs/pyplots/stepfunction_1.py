import numpy as np
import matplotlib.pyplot as plt

from mplshared import StepFunctionLine


x = np.linspace(-3, 3, 20)
y = np.sin(x)
sf1 = StepFunctionLine(x, y, linewidth=3, color='red')
plt.gca().add_line(sf1)
sf1.autolims(plt)

plt.grid()
plt.savefig('stepfunction_1.png')
plt.show()
