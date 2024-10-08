import pyglet
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

window = pyglet.window.Window(800, 600)
window.set_caption("Odyssey Eden")
batch = pyglet.graphics.Batch()
title_label = pyglet.text.Label("Odyssey Eden",
    font_name="Arial",
    font_size=36,
    x=window.width // 2,
    y=window.width //2,
    anchor_x="center",
    anchor_y="center",
    batch=batch)

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()