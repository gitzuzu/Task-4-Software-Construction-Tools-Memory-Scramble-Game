import pygame
import math

SCREEN_W, SCREEN_H = 1000, 720
FPS = 60
CARD_RADIUS = 12
FLIP_SPEED = 0.03

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


def draw_shape(surf, shape_id, cx, cy, size, color):
    r = size // 2
    s = shape_id % 8

    if s == 0:
        pygame.draw.circle(surf, color, (cx, cy), r)

    elif s == 1:
        pygame.draw.rect(surf, color, (cx-r, cy-r, r*2, r*2), border_radius=6)

    elif s == 2:
        pts = [
            (cx, cy-r),
            (cx+r, cy+r),
            (cx-r, cy+r)
        ]
        pygame.draw.polygon(surf, color, pts)

    elif s == 3:
        pts = [
            (cx, cy-r),
            (cx+r, cy),
            (cx, cy+r),
            (cx-r, cy)
        ]
        pygame.draw.polygon(surf, color, pts)

    elif s == 4:
        pygame.draw.circle(surf, color, (cx-r//2, cy-r//3), r//2)
        pygame.draw.circle(surf, color, (cx+r//2, cy-r//3), r//2)
        pts = [(cx-r, cy-r//5), (cx+r, cy-r//5), (cx, cy+r)]
        pygame.draw.polygon(surf, color, pts)

    elif s == 5:
        for angle in range(0, 360, 72):
            rad = math.radians(angle)
            px = cx + int(math.cos(rad) * r)
            py = cy + int(math.sin(rad) * r)
            pygame.draw.circle(surf, color, (px, py), r//3)
        pygame.draw.circle(surf, color, (cx, cy), r//3)

    elif s == 6:
        pts = []
        pygame.draw.line(surf, color, (cx+r, cy-r), (cx-r, cy+r), 6)