import pyglet as pg
from random import randint

win = pg.window.Window()
pg.resource.path = ['./Test_Res']
pg.resource.reindex()
#event_logger = pg.window.event.WindowEventLogger()  # Показывает все зарегестрированые события
#win.push_handlers(event_logger)

im_berd = pg.resource.image('2_2.png')
im_bar = pg.resource.image('barrier.png')
t = 0.01


class berd():

    def __init__(self):
        self.image = pg.sprite.Sprite(im_berd)
        self.image.x = 150
        self.image.y = win.height // 2
        self.v = 0
        self.dv = 6000 * t
        self.Uv = 120000 * t
        self.coun = 0

    def up(self):
        self.v = self.Uv * t

    def down(self):
        self.v -= self.dv * t

    def Transfer(self):
        self.image.y += self.v / 2

    def count(self):
        if len(bar) > 1:
            if bar[0].image1.x + bar[0].image1.width == self.image.x or bar[1].image1.x + bar[
                1].image1.width == self.image.x:
                self.coun += 1
        else:
            if bar[0].image1.x + bar[0].image1.width == self.image.x:
                self.coun += 1

    def dead(self):
        if self.image.y <= 0 or self.image.y >= win.height:
            return True
        else:
            if len(bar) > 3:
                if (self.image.y + self.image.height-5 >= bar[1].image1.y or self.image.y <= bar[1].image1.y - bar[
                    1].pozit) and (
                        self.image.x + self.image.width >= bar[1].image1.x and self.image.x <= bar[1].image1.x + bar[
                    1].image1.width):
                    print(1)
                    return True
            else:
                if (self.image.y + self.image.height-5 >= bar[0].image1.y or self.image.y <= bar[0].image1.y - bar[
                    0].pozit) and (
                        self.image.x + self.image.width >= bar[0].image1.x and self.image.x <= bar[0].image1.x + bar[
                    0].image1.width):
                    return True
            return False


class barrier():
    pozit = 125

    def __init__(self):
        self.image1 = pg.sprite.Sprite(im_bar)
        self.image2 = pg.sprite.Sprite(im_bar)
        self.image1.x = win.width
        self.image2.x = self.image1.x
        self.image1.y = randint(self.pozit, win.height)
        self.image2.y = self.image1.y - self.pozit - win.height

        self.v = 300 * t

    def Transfer(self):
        self.image1.x -= self.v
        self.image2.x -= self.v


bar = [barrier()]
bird = berd()

rast_colon = win.height - 25


def trans(bar):
    for i in range(len(bar)):
        bar[i].Transfer()
    if bar[-1].image1.x <= rast_colon:
        bar.append(barrier())
    if bar[0].image1.x < -bar[0].image1.width * 2:
        bar.pop(0)
        print(bar)


def bar_draw(bar):
    for i in range(len(bar)):
        bar[i].image1.draw()
        bar[i].image2.draw()


def text(count):
    return pg.text.Label(str(count), 'Calibri', 26, x=win.width, y=win.height, anchor_x='right', anchor_y='top')


def time(dt):
    global bird, bar
    bird.down()
    bird.Transfer()
    trans(bar)
    bird.count()
    if bird.dead():
        bird = berd()
        bar = [barrier()]
        print('Yes')


pg.clock.schedule_interval(time, t)


@win.event
def on_draw():
    win.clear()
    bar_draw(bar)
    text(bird.coun).draw()
    bird.image.draw()


@win.event
def on_key_press(symbol, modifiers):
    if symbol == pg.window.key.UP:
        bird.up()


pg.app.run()
