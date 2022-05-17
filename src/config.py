from easydict import EasyDict

config = EasyDict()

# Measurements
config.problem = EasyDict()
config.problem.span_length = 10 # Distance units
config.problem.left_attach_height = 14 # Distance units
config.problem.right_attach_height = 6 # Distance units
config.problem.midspan_height = 2 # Distance units
config.problem.midspan_x_coordinate = 6
config.problem.left_x_coordinate = 0
config.problem.right_x_coordinate = 10

# Graph settings
config.graph_config = EasyDict()
config.graph_config.x_margin = 2
config.graph_config.y_margin = 2
config.graph_config.grid = True
