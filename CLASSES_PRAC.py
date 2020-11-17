import pygame
from pygame import mixer
pygame.init()
mixer.init()
class student:
    name1="Tandon"
    name2="200 Rupee k chaka"
    pass
carry=student()
R=student()
i=0
a=carry.name1
b=R.name2
def fun1(f):
    print(f"{f} is a good youtuber \n")
fun1(a)
fun1(b)
print("Chaleja Bhosdike Amir madarchod")
mixer.music.load("water.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
white = (255, 255, 255)

X = 168
Y = 94

display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Image')

image = pygame.image.load(r'C:\Users\DELL\Pictures\1.jpg')

while True:

    display_surface.fill(white)

    display_surface.blit(image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            quit()

        pygame.display.update()
