import pyglet
from pyglet.gl import glBegin, GL_LINE_LOOP, glMatrixMode, GL_PROJECTION, glLoadIdentity, GL_MODELVIEW, glScalef, \
    GL_LINES, glColor3f, glVertex2f, glEnd, GL_LINE_STRIP
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
    return coeffs_pos, True


def heart():
    return [-1, 2, -1], False


T = 0
coeffs, has_neg = heart()
start_index = -(len(coeffs) // 2) if has_neg else 0
S = 0.1
P = 2 * np.pi
points = []


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


def update(dt):
    global T
    T += dt


def main():
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()

if __name__ == '__main__':
    main()