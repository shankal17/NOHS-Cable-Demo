from easydict import EasyDict

config = EasyDict()

# Measurements
config.problem = EasyDict()
config.problem.span_length = 20 # Distance units
config.problem.left_attach_height = 10 # Distance units
config.problem.right_attach_height = 8 # Distance units
config.problem.midspan_height = 7 # Distance units

# Graph settings
config.graph_config = EasyDict()
config.graph_config.x_margin = 2
config.graph_config.y_margin = 2
config.graph_config.grid = True

