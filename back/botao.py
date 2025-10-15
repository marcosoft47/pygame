import pygame
#button class
class Botao():
	def __init__(self, x: int, y: int, image: pygame.surface.Surface, scale: float):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def update(self, surface: pygame.surface.Surface) -> bool:
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen

		return action

	def render(self, surface: pygame.surface.Surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))
