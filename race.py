import pygame
import sys
import math

# Initialisatie
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Afbeeldingen laden
track_image = pygame.image.load(r"C:\Users\boude\Documents\Race-python\racebaan.jpg").convert()
car_image_original = pygame.image.load(r"C:\Users\boude\Documents\Race-python\auto.jpg").convert_alpha()

# Schaal de afbeeldingen
track_image = pygame.transform.scale(track_image, (1280, 720))
car_image_original = pygame.transform.scale(car_image_original, (60, 120))  # Afhankelijk van je autoformaat

# Auto instellingen
car_pos = pygame.Vector2(640, 360)
car_angle = 0
car_speed = 0
rotation_speed = 3
acceleration = 0.3
friction = 0.05
max_speed = 6

# Game loop
running = True
while running:
    dt = clock.tick(60) / 1000  # Tijdsdelta per frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Besturing
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        car_speed += acceleration
    if keys[pygame.K_s]:
        car_speed -= acceleration
    if keys[pygame.K_a]:
        car_angle += rotation_speed
    if keys[pygame.K_d]:
        car_angle -= rotation_speed

    # Beweging en wrijving
    car_speed = max(-max_speed, min(max_speed, car_speed))
    if car_speed > 0:
        car_speed -= friction
    elif car_speed < 0:
        car_speed += friction
    if abs(car_speed) < 0.05:
        car_speed = 0

    # Beweging volgens hoek
    direction = pygame.Vector2(math.cos(math.radians(-car_angle)), math.sin(math.radians(-car_angle)))
    car_pos += direction * car_speed

    # Auto roteren
    car_image = pygame.transform.rotate(car_image_original, car_angle)
    car_rect = car_image.get_rect(center=car_pos)

    # Tekenen
    screen.blit(track_image, (0, 0))               # Racebaan tekenen
    screen.blit(car_image, car_rect.topleft)       # Auto tekenen

    pygame.display.flip()

pygame.quit()
sys.exit()
