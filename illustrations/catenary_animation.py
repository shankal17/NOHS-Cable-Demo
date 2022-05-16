import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
sys.path.append('src')
from compute import *
 
 
# creating a blank window
# for the animation
fig = plt.figure()
axis = plt.axes(xlim =(-10, 10),
                ylim =(-2, 20))
 
line, = axis.plot([], [], lw = 2)
temp_text = axis.text(0.51, 0.13, '', transform=axis.transAxes, bbox=dict(facecolor='red'), fontsize=14)
arrow = patches.Arrow(0, 0, 0, 0, color='k', zorder=100, width=0.5)

def init():
    line.set_data([], [])
    temp_text.set_text('')
    axis.add_patch(arrow)
    return line, temp_text, arrow
 
# initializing empty values
# for x and y co-ordinates
x = np.linspace(-10, 10)
c = np.linspace(2, 7, 100)
 
# animation function
def animate(i):
    y = c[i] * np.cosh(x / c[i])
    line.set_data(x, y)
    temp_text.set_text('Catenary Parameter c = %.1f' % c[i])
    arrow = patches.Arrow(0, 0, 0, c[i], color='k', zorder=100, width=0.5)
    axis.add_patch(arrow)
     
    return line, temp_text, arrow
 
# calling the animation function    
anim = FuncAnimation(fig, animate,
                     init_func = init,
                     frames = len(c),
                     interval = 20,
                     blit = True)
 
# show plot
axis.grid(True)
plt.show()

