class Pipe:
    def __init__(self, x, y, gap, img, rotated_img):
        self.x = x
        self.y = y
        self.gap = gap
        self.img_a = img
        self.img_b = rotated_img

    def update(self):
        self.x -= 1

    def draw(self, surface):
        surface.blit(self.img_a, (self.x, self.y,
                     self.img_a.get_width(), self.img_a.get_height()))
        surface.blit(self.img_b, (self.x, self.y + self.img_b.get_height() + self.gap,
                     self.img_b.get_width(), self.img_b.get_height()))
