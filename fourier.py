import pyglet
from pyglet.window import mouse
from pyglet.gl import glBegin, GL_LINE_LOOP, glMatrixMode, GL_PROJECTION, glLoadIdentity, GL_MODELVIEW, glScalef, \
    GL_LINES, glColor3f, glVertex2f, glEnd, GL_LINE_STRIP, glTranslatef, glLineWidth, GL_TRIANGLES
import numpy as np
from curves.heart import get_coeffs

W = 800
H = 800

window = pyglet.window.Window(W, H)
fps_display = pyglet.window.FPSDisplay(window)

T = 0
coeffs, start_index = get_coeffs()

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
    glLineWidth(2)
    pyglet.graphics.draw(2, GL_LINES,
                         ('v2f', (x, y, x2, y2)),
                         ('c3B', (0, 0, 255, 0, 0, 255)))
    glLineWidth(1)
    draw_circle(x, y, l)

    d = l * 0.1
    xq = (l - d) * np.cos(angle) + x
    yq = (l - d) * np.sin(angle) + y

    xk = xq - d * np.sin(angle)
    yk = yq + d * np.cos(angle)

    xh = xq + d * np.sin(angle)
    yh = yq - d * np.cos(angle)

    pyglet.graphics.draw(3, GL_TRIANGLES,
                         ('v2f', (x2, y2, xk, yk, xh, yh)),
                         ('c3B', (0, 0, 255, 0, 0, 255, 0, 0, 255)))

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
