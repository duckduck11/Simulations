import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

#color_theme
plt.style.use('dark_background')

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, sharey=True)
fig.suptitle('Group and Phase Velocity')

#set_x_y
ax1.set_xlim(0, 10)
ax1.set_ylim(-2, 2)

#set_chart_lines
line1, = ax1.plot([], [], color='c', lw=3)
line2, = ax2.plot([], [], color='y', lw=3)
line3, = ax3.plot([], [], color='m', lw=6)
plt.legend([line1, line2, line3], ['f1=cos(\u03C91t-k1x)', 'f0=cos(\u03C90t-k0x)', 'f1+f0'],loc='center left', bbox_to_anchor=(1, 0.5))

#set_subplots
plt.subplots_adjust(bottom=0.25)
ax_slider = plt.axes([0.1, 0.15, 0.8, 0.05])
ax_slider1 = plt.axes([0.1, 0.1, 0.8, 0.05])
ax_slider2 = plt.axes([0.1, 0.05, 0.8, 0.05])
ax_slider3 = plt.axes([0.1, 0, 0.8, 0.05])

#set_sliders
omega_0 = Slider(ax_slider, '\u03C90', valmin=0.01, valmax=0.1, valinit=0, valstep=0.001)
k_0 = Slider(ax_slider1, 'k0', valmin=0.1, valmax=3, valinit=0, valstep=0.1)
omega_1 = Slider(ax_slider2, '\u03C91', valmin=0.01, valmax=0.1, valinit=0, valstep=0.001)
k_1 = Slider(ax_slider3, 'k1', valmin=0.1, valmax=3, valinit=0, valstep=0.1)

#init_function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1, line2, line3

#animate_function
def animate(i):
    x1 = np.linspace(0, 10, 1000)
    y1 = np.cos(2 * np.pi * (omega_0.val*i - k_0.val*x1))
    line1.set_data(x1, y1)

    x2 = np.linspace(0, 10, 1000)
    y2 = np.cos(2 * np.pi * (omega_1.val*i - k_1.val*x1))
    line2.set_data(x2, y2)

    x3 = np.linspace(0, 10, 1000)
    y3 = np.cos(2 * np.pi * (omega_0.val*i - k_0.val*x1)) + np.cos(2 * np.pi * (omega_1.val*i - k_1.val*x1))
    line3.set_data(x3, y3)

    return line1, line2, line3

anim1 = FuncAnimation(fig, animate, init_func=init, frames=500, interval=20, blit=True)

plt.show()
