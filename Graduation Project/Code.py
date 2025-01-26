from pygame import*

class Player(sprite.Sprite):
    def __init__(self, image_path, x, y, width, height,speed):
        self.image = image.load(image_path)
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height) 

    def load(self, window):
        window.blit(self.image, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)  

    def movement(self):
        self.old_rect = self.rect.copy()
        keys = key.get_pressed()
        if keys[K_d] and self.x < 253:
            self.x += self.speed
        if keys[K_a] and self.x >5:
            self.x -= self.speed
    def movement2(self):
        self.old_rect = self.rect.copy()
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.x < 565:
            self.x += self.speed
        if keys[K_LEFT] and self.x >317:
            self.x -= self.speed

    def gravity(self):
        self.old_rect = self.rect.copy()
        if self.y < 265:
            self.y += 10

    
    def jumping(self):
        self.old_rect = self.rect.copy()
        Jump = False
        jump_speed = 0
        key_pressed = key.get_pressed()
        
        if key_pressed[K_w] and self.y > 110:
            self.y -= 20
            if self.y <= 110:
                self.y = 110
                self.y += jump_speed
                jump_speed += 5
    def jumping2(self):
        self.old_rect = self.rect.copy()
        Jump = False
        jump_speed = 0
        key_pressed = key.get_pressed()
        
        if key_pressed[K_UP] and self.y > 110:
            self.y -= 20
            if self.y <= 110:
                self.y = 110
                self.y += jump_speed
                jump_speed += 5

class Ball:
    def __init__(self, image_path, x, y, width, height):
        self.image = image.load(image_path)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)  

    def load(self, window):
        window.blit(self.image, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)



class Nets:
    def __init__(self, image_path, x, y, width, height):
        self.image = image.load(image_path)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Rect(x, y, width, height)  

    def load(self, window):
        window.blit(self.image, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)
            

            
            
            
            

        

