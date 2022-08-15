import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


def animate(i):
    line_count = 0
    data = open('pr.txt', 'r').read()
    lines = data.split('\n')
    xs = []
    ys = []

    for line in lines:
        if line != '':
            y, x = line.split(', ')
            xs.append(float(x))
            ys.append(float(y))
            line_count += 1

    ax.clear()
    ax.plot(xs, ys)

    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title("Plot1")


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
