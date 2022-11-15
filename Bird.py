from pygame import Rect


class Bird:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.dy = 0
        self.img = img

    def hit_pipe_or_edge(self, height, pipe):
        if self.y <= 0 or self.y >= height - self.img.get_height():
            return True

        x = pipe.x
        y = pipe.y
        b_y = pipe.b_y
        w = pipe.img_a.get_width()
        h_a = pipe.img_a.get_height()
        true_h_a = y + h_a
        true_h_b = height - b_y

        self_rect = Rect(self.x, self.y, self.img.get_width(),
                         self.img.get_height())
        return self_rect.colliderect((x, 0), (w, true_h_a)) or self_rect.colliderect((x, b_y), (w, true_h_b))

    def jump(self):
        self.dy = -5

    def update(self):
        self.dy += .5
        self.y += self.dy

    def draw(self, WIN):
        WIN.blit(self.img, (self.x, self.y))
