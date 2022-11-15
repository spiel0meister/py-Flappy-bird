class Pipe:
    def __init__(self, x, y, gap, img, rotated_img):
        self.x = x
        self.y = y
        self.img_a = img
        self.img_b = rotated_img
        self.b_y = self.y + self.img_b.get_height() + gap

    def update(self):
        self.x -= 1

    def draw(self, surface):
        surface.blit(self.img_a, (self.x, self.y))
        surface.blit(self.img_b, (self.x, self.b_y))
