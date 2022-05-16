import numpy as np
import matplotlib.pyplot as plt
from config import config

problem = config.problem
graph_config = config.graph_config
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim([-graph_config.x_margin, problem.span_length+graph_config.x_margin])
ax.set_ylim([0, max(problem.left_attach_height, problem.right_attach_height)+graph_config.y_margin])
ax.grid(graph_config.grid)
plt.show()
