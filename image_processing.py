import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.style as style
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.transforms import Affine2D
transform = Affine2D().rotate_deg(45).translate(2, 2)
plt.plot([0, 1], [0, 1], transform=transform + plt.gca().transData)
plt.show()



# image = mpimg.imread('gantt.jpg')
# plt.imshow(image)
# plt.text(0.5, 0.5, 'Hello, Matplotlib!', fontsize=12, ha='center', va='center')

# style.use('ggplot')  # Apply a predefined style


# fig, ax = plt.subplots()
# line, = ax.plot([], [])

# def init():
#     line.set_data([], [])
#     return line,

# def update(frame):
#     x = np.linspace(0, 2, 100)
#     y = np.sin(2 * np.pi * (x - 0.01 * frame))
#     line.set_data(x, y)
#     return line,

# ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)
# plt.show()


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# x, y = np.random.rand(2, 100)
# z = np.random.rand(100)
# ax.scatter(x, y, z)
# plt.show()

# """
# python -m streamlit run "d:/Semester 5/Intro to Data Science/IDS Project/image_processing.py"

# """
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

t = np.arange(0.0, 1.0, 0.001)
a0 = 5
y = a0 * np.sin(2 * np.pi * t)
l, = plt.plot(t, y)

ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Amplitude', 0.1, 10.0, valinit=a0)

def update(val):
    l.set_ydata(slider.val * np.sin(2 * np.pi * t))
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()
