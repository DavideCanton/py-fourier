import pyglet
from pyglet.window import mouse
from pyglet.gl import glBegin, GL_LINE_LOOP, glMatrixMode, GL_PROJECTION, glLoadIdentity, GL_MODELVIEW, glScalef, \
    GL_LINES, glColor3f, glVertex2f, glEnd, GL_LINE_STRIP, glTranslatef
import numpy as np

W = 800
H = 800

window = pyglet.window.Window(W, H)
fps_display = pyglet.window.FPSDisplay(window)


def sawtooth(n):
    c0 = 0
    coeffs_pos = [1j * ((-1) ** n) / (2 * n * np.pi) for n in range(1, n)]
    coeffs_neg = [x.conjugate() for x in coeffs_pos[::-1]]
    coeffs_pos = coeffs_neg + [c0] + coeffs_pos
    return coeffs_pos, -n + 1


def heart():
    return [-1, 2, -1], 0


def heart2():
    return [-0.001223j, (0.000896 + 0j), (-0 + 0.001286j), (-0.000943 + 0j), (-0 - 0.001354j), (0.000994 + 0j),
            0.001429j, (-0.00105 + 0j), -0.001511j, (0.001112 - 0j), 0.001601j, (-0.001179 + 0j), (-0 - 0.001701j),
            (0.001254 + 0j), 0.001811j, (-0.001337 + 0j), -0.001933j, (0.00143 + 0j), (-0 + 0.00207j), (-0.001534 + 0j),
            (-0 - 0.002224j), (0.001651 + 0j), (-0 + 0.002398j), (-0.001784 - 0j), (-0 - 0.002597j), (0.001936 - 0j),
            0.002824j, (-0.002111 - 0j), -0.003087j, (0.002314 + 0j), 0.003393j, (-0.002552 - 0j), (-0 - 0.003753j),
            (0.002834 - 0j), (-0 + 0.004183j), (-0.003173 + 0j), (-0 - 0.004701j), (0.003585 - 0j), (-0 + 0.005338j),
            (-0.004097 - 0j), (-0 - 0.006134j), (0.004745 - 0j), 0.007151j, (-0.005586 - 0j), (-0 - 0.008491j),
            (0.006717 - 0j), (-0 + 0.010317j), (-0.008302 + 0j), -0.012928j, (0.01065 - 0j), 0.016891j,
            (-0.014373 + 0j), -0.023353j, (0.020644 - 0j), (-0 + 0.034449j), (-0.030716 + 0j), (-0 - 0.051556j),
            (0.035408 - 0j), (-0 + 0.047586j), (0.10557 + 0j), (-0 - 0.656819j), (1.754871 - 0j), (-0 + 0.656819j),
            (0.10557 - 0j), (-0 - 0.047586j), (0.035408 + 0j), (-0 + 0.051556j), (-0.030716 + 0j), -0.034449j,
            (0.020644 - 0j), (-0 + 0.023353j), (-0.014373 - 0j), (-0 - 0.016891j), (0.01065 - 0j), 0.012928j,
            (-0.008302 - 0j), (-0 - 0.010317j), (0.006717 + 0j), (-0 + 0.008491j), (-0.005586 - 0j), -0.007151j,
            (0.004745 + 0j), (-0 + 0.006134j), (-0.004097 + 0j), -0.005338j, (0.003585 + 0j), 0.004701j,
            (-0.003173 + 0j), -0.004183j, (0.002834 - 0j), (-0 + 0.003753j), (-0.002552 - 0j), -0.003393j,
            (0.002314 - 0j), 0.003087j, (-0.002111 + 0j), -0.002824j, (0.001936 - 0j), (-0 + 0.002597j),
            (-0.001784 + 0j), -0.002398j, (0.001651 - 0j), 0.002224j, (-0.001534 + 0j), -0.00207j, (0.00143 + 0j),
            0.001933j, (-0.001337 - 0j), -0.001811j, (0.001254 + 0j), 0.001701j, (-0.001179 - 0j), -0.001601j,
            (0.001112 + 0j), 0.001511j, (-0.00105 + 0j), -0.001429j, (0.000994 + 0j), (-0 + 0.001354j),
            (-0.000943 + 0j)], -60


T = 0
coeffs, start_index = heart2()
S = 0.9
P = 2 * np.pi
points = []
DX = 0
DY = 0
ST = 2


def draw_circle(x, y, r):
    glBegin(GL_LINE_LOOP)
    glColor3f(255, 0, 0)

    for i in range(360):
        deg_in_rad = i / 180 * np.pi
        glVertex2f(x + np.cos(deg_in_rad) * r, y + np.sin(deg_in_rad) * r)

    glEnd()


def draw_line_from(x, y, l, angle):
    x2 = x + l * np.cos(angle)
    y2 = y + l * np.sin(angle)
    pyglet.graphics.draw(2, GL_LINES, ('v2f', (x, y, x2, y2)),
                         ('c3B', (0, 0, 255, 0, 0, 255)))
    draw_circle(x, y, l)
    return [x2, y2]


@window.event
def on_draw():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glScalef(S, S, S)
    glTranslatef(DX, DY, 0)

    window.clear()

    p = [0, 0]
    t = T
    for i in range(len(coeffs)):
        e = coeffs[i] * np.exp(2 * np.pi * (i + start_index) * t * 1j / P)
        p = draw_line_from(p[0], p[1], np.abs(e), np.angle(e))
    points.append(p)

    glBegin(GL_LINE_STRIP)
    glColor3f(255, 255, 255)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

    fps_display.draw()


@window.event
def on_mouse_scroll(_x, _y, _scroll_x, scroll_y):
    global S
    S += scroll_y / 10
    if S <= 0:
        S = 0.1


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, _modifiers):
    global DX, DY
    if buttons & mouse.LEFT:
        DX += -dx * 0.0005 * S
        DY += -dy * 0.0005 * S


@window.event
def on_mouse_press(x, y, button, _modifiers):
    global DX, DY, S
    if button & mouse.RIGHT:
        DX = 0
        DY = 0
        S = 0.5


def update(dt):
    global T
    T += dt / ST


def main():
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()


if __name__ == '__main__':
    main()
