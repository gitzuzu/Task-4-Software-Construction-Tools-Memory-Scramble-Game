import pygame
import math
import os

SCREEN_W, SCREEN_H = 1000, 720
FPS = 60
CARD_RADIUS = 12
FLIP_SPEED = 0.03
ICON_PATH = "assets/icons"

ICON_FILES = [
    "heart.png",
    "star.png",
    "flower.png",
    "moon.png",
    "diamond.png",
    "crown.png",
    "bow.png",
    "cat.png",
]
ICONS = []

for file in ICON_FILES:
    img = pygame.image.load(os.path.join(ICON_PATH, file))
    ICONS.append(img)
COLORS = {
    "bg": (255, 245, 250),

    "panel": (255, 255, 255),

    "card_back": (255, 220, 235),
    "card_face": (255, 255, 255),

    "card_border": (255, 170, 210),

    "accent": (255, 105, 180),
    "accent_hover": (255, 130, 195),

    "matched": (220, 255, 230),
    "matched_border": (90, 200, 140),

    "wrong": (255, 220, 225),
    "wrong_border": (255, 90, 120),

    "text": (90, 40, 70),
    "text_dim": (160, 110, 140),

    "timer_ok": (100, 200, 140),
    "timer_warn": (255, 180, 90),
    "timer_crit": (255, 80, 120),

    "shadow": (240, 210, 225),
}

SHAPE_PALETTES = [
    (255, 105, 180),   # hot pink
    (255, 182, 193),   # light pink
    (255, 140, 170),   # rose
    (255, 160, 200),   # pastel pink
    (220, 120, 180),   # mauve pink
    (255, 190, 220),   # baby pink
    (255, 120, 150),   # coral pink
    (200, 140, 255),   # soft purple
]

def draw_shape(surf, shape_id, cx, cy, size, color=None):
    icon = ICONS[shape_id % len(ICONS)]

    scaled = pygame.transform.smoothscale(
        icon,
        (size, size)
    )

    rect = scaled.get_rect(center=(cx, cy))

    surf.blit(scaled, rect)