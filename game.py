from ui import *

import pygame
import random
import math
import time
import sys


class Card:
    def __init__(self, shape_id, rect):
        self.shape_id = shape_id
        self.color = None

        self.rect = pygame.Rect(rect)

        self.revealed = False
        self.matched = False

        self.flip_progress = 0
        self.flip_target = 0

        self.wrong_flash = 0

    def start_flip(self, front):
        self.flip_target = 1 if front else 0

    def update(self):
        diff = self.flip_target - self.flip_progress

        if abs(diff) < FLIP_SPEED:
            self.flip_progress = self.flip_target
        else:
            self.flip_progress += FLIP_SPEED if diff > 0 else -FLIP_SPEED

        if self.wrong_flash > 0:
            self.wrong_flash -= 1

    def draw(self, surf):
        scale = abs(math.cos(math.radians(self.flip_progress * 180)))

        width = max(4, int(self.rect.width * scale))

        draw_rect = pygame.Rect(
            self.rect.centerx - width // 2,
            self.rect.y,
            width,
            self.rect.height
        )

        shadow = draw_rect.move(4, 4)

        pygame.draw.rect(
            surf,
            COLORS["shadow"],
            shadow,
            border_radius=CARD_RADIUS
        )

        showing_front = self.flip_progress >= 0.5

        if self.wrong_flash > 0:
            bg = COLORS["wrong"]
            border = COLORS["wrong_border"]

        elif self.matched:
            bg = COLORS["matched"]
            border = COLORS["matched_border"]

        elif showing_front:
            bg = COLORS["card_face"]
            border = COLORS["accent"]

        else:
            bg = COLORS["card_back"]
            border = COLORS["card_border"]

        pygame.draw.rect(
            surf,
            bg,
            draw_rect,
            border_radius=CARD_RADIUS
        )

        pygame.draw.rect(
            surf,
            border,
            draw_rect,
            2,
            border_radius=CARD_RADIUS
        )

        if showing_front and width > 20:
            draw_shape(
                surf,
                self.shape_id,
                draw_rect.centerx,
                draw_rect.centery,
                int(min(draw_rect.width, draw_rect.height) * 0.72),
                self.color
            )


class Button:
    def __init__(self, rect, text, font):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.hovered = False

    def draw(self, surf):
        color = COLORS["accent_hover"] if self.hovered else COLORS["accent"]

        pygame.draw.rect(
            surf,
            color,
            self.rect,
            border_radius=10
        )

        txt = self.font.render(self.text, True, (255, 255, 255))

        surf.blit(txt, txt.get_rect(center=self.rect.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True

        return False


class InputField:
    def __init__(self, rect, default, label, font):
        self.rect = pygame.Rect(rect)

        self.value = str(default)
        self.label = label
        self.font = font

        self.active = False

    def get_int(self):
        try:
            return int(self.value)
        except:
            return 4

    def draw(self, surf, label_font):
        label = label_font.render(
            self.label,
            True,
            COLORS["text_dim"]
        )

        surf.blit(label, (self.rect.x, self.rect.y - 25))

        border = COLORS["accent"] if self.active else COLORS["card_border"]

        pygame.draw.rect(
            surf,
            COLORS["card_face"],
            self.rect,
            border_radius=8
        )

        pygame.draw.rect(
            surf,
            border,
            self.rect,
            2,
            border_radius=8
        )

        txt = self.font.render(
            self.value,
            True,
            COLORS["text"]
        )

        surf.blit(txt, txt.get_rect(center=self.rect.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.value = self.value[:-1]

            elif event.unicode.isdigit() and len(self.value) < 3:
                self.value += event.unicode


class MemoryScramble:
    def __init__(self):
        self.error_message = ""
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

        pygame.display.set_caption("Memory Scramble")

        self.clock = pygame.time.Clock()

        self.font_title = pygame.font.SysFont("Segoe UI", 52, bold=True)
        self.font_large = pygame.font.SysFont("Segoe UI", 28, bold=True)
        self.font_medium = pygame.font.SysFont("Segoe UI", 22)
        self.font_small = pygame.font.SysFont("Segoe UI", 16)

        self.state = "menu"

        self.cards = []

        self.locked = False
        self.lock_timer = 0

        self.selected = []

        self.moves = 0
        self.matches = 0

        self.time_left = 0
        self.timeout = 60

        self.last_tick = time.time()

        self.build_menu()

    def build_menu(self):
        cx = SCREEN_W // 2

        self.rows_input = InputField(
            (cx - 180, 280, 120, 50),
            4,
            "Rows",
            self.font_large
        )

        self.cols_input = InputField(
            (cx, 280, 120, 50),
            4,
            "Cols",
            self.font_large
        )

        self.time_input = InputField(
            (cx - 90, 360, 180, 50),
            60,
            "Time (sec)",
            self.font_large
        )

        self.start_btn = Button(
            (cx - 120, 460, 240, 60),
            "Start Game",
            self.font_medium
        )

        self.restart_btn = Button(
            (SCREEN_W - 160, 20, 130, 42),
            "Restart",
            self.font_small
        )

    def setup_board(self):

        self.rows = self.rows_input.get_int()
        self.cols = self.cols_input.get_int()

        if (self.rows * self.cols) % 2 != 0:
            self.cols += 1

        total = self.rows * self.cols

        MAX_CARDS = 16

        if total > MAX_CARDS:
            self.error_message = "Maximum board size is 4x4 (16 cards)"
            return

        self.error_message = ""

        self.timeout = self.time_input.get_int()
        self.time_left = float(self.timeout)

        pairs = total // 2

        ids = list(range(pairs)) * 2

        random.shuffle(ids)

        pad = 18
        top = 100

        available_w = SCREEN_W - (pad * (self.cols + 1))
        available_h = SCREEN_H - top - (pad * (self.rows + 1))

        cw = int((available_w // self.cols) * 0.88)
        ch = int((available_h // self.rows) * 0.88)

        self.cards = []

        for i, sid in enumerate(ids):
            row = i // self.cols
            col = i % self.cols

            x = pad + col * (cw + pad)
            y = top + pad + row * (ch + pad)

            self.cards.append(Card(sid, (x, y, cw, ch)))

        self.selected = []
        self.locked = False
        self.lock_timer = 0

        self.moves = 0
        self.matches = 0

        self.last_tick = time.time()

    def run(self):
        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.handle_event(event)

            self.update()
            self.draw()

    def handle_event(self, event):
        if self.state == "menu":
            self.rows_input.handle_event(event)
            self.cols_input.handle_event(event)
            self.time_input.handle_event(event)
            
        if self.start_btn.handle_event(event):

            self.setup_board()

            if self.error_message == "":
                self.state = "playing"

        elif self.state == "playing":
            if self.restart_btn.handle_event(event):
                self.state = "menu"

            if event.type == pygame.MOUSEBUTTONDOWN and not self.locked:
                self.handle_click(event.pos)

    def handle_click(self, pos):
        for i, card in enumerate(self.cards):
            if card.rect.collidepoint(pos):

                if card.revealed or card.matched:
                    continue

                card.revealed = True
                card.start_flip(True)

                self.selected.append(i)

                if len(self.selected) == 2:
                    self.moves += 1

                    a, b = self.selected

                    c1 = self.cards[a]
                    c2 = self.cards[b]

                    if c1.shape_id == c2.shape_id:
                        c1.matched = True
                        c2.matched = True

                        self.selected = []

                        self.matches += 1

                        if self.matches == len(self.cards) // 2:
                            self.state = "win"

                    else:
                        c1.wrong_flash = 30
                        c2.wrong_flash = 30

                        self.locked = True
                        self.lock_timer = 60

                break

    def update(self):
        if self.state != "playing":
            return

        for card in self.cards:
            card.update()

        if self.locked:
            self.lock_timer -= 1

            if self.lock_timer <= 0:
                self.locked = False

                for i in self.selected:
                    self.cards[i].revealed = False
                    self.cards[i].start_flip(False)

                self.selected = []

        now = time.time()

        self.time_left -= now - self.last_tick

        self.last_tick = now

        if self.time_left <= 0:
            self.state = "lose"

    def draw(self):
        self.screen.fill(COLORS["bg"])

        if self.state == "menu":
            self.draw_menu()

        else:
            self.draw_hud()

            for card in self.cards:
                card.draw(self.screen)

            if self.state == "win":
                self.draw_overlay("YOU WIN")

            elif self.state == "lose":
                self.draw_overlay("GAME OVER")

        pygame.display.flip()

    def draw_menu(self):

        if self.error_message:
            error = self.font_small.render(
                self.error_message,
                True,
                (255, 80, 120)
            )

            self.screen.blit(
                error,
                error.get_rect(center=(SCREEN_W // 2, 540))
            )
        title = self.font_title.render(
            "Memory Scramble",
            True,
            COLORS["text"]
        )

        self.screen.blit(
            title,
            title.get_rect(center=(SCREEN_W // 2, 140))
        )

        subtitle = self.font_medium.render(
            "Configure your game and start playing",
            True,
            COLORS["text_dim"]
        )

        self.screen.blit(
            subtitle,
            subtitle.get_rect(center=(SCREEN_W // 2, 190))
        )

        self.rows_input.draw(self.screen, self.font_small)
        self.cols_input.draw(self.screen, self.font_small)
        self.time_input.draw(self.screen, self.font_small)

        self.start_btn.draw(self.screen)

    def draw_hud(self):
        pygame.draw.rect(
            self.screen,
            COLORS["panel"],
            (0, 0, SCREEN_W, 80)
        )

        title = self.font_medium.render(
            "Memory Scramble",
            True,
            COLORS["text"]
        )

        self.screen.blit(title, (20, 28))

        pct = self.time_left / self.timeout

        if pct > 0.4:
            tc = COLORS["timer_ok"]
        elif pct > 0.2:
            tc = COLORS["timer_warn"]
        else:
            tc = COLORS["timer_crit"]

        timer = self.font_large.render(
            f"{int(self.time_left)}s",
            True,
            tc
        )

        self.screen.blit(
            timer,
            timer.get_rect(center=(SCREEN_W // 2, 40))
        )

        stats = self.font_medium.render(
            f"Moves: {self.moves}",
            True,
            COLORS["text_dim"]
        )

        self.screen.blit(stats, (SCREEN_W - 300, 28))

        self.restart_btn.draw(self.screen)

    def draw_overlay(self, text):
        overlay = pygame.Surface(
            (SCREEN_W, SCREEN_H),
            pygame.SRCALPHA
        )

        overlay.fill((0, 0, 0, 120))

        self.screen.blit(overlay, (0, 0))

        title = self.font_title.render(
            text,
            True,
            (255, 255, 255)
        )

        self.screen.blit(
            title,
            title.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2))
        )


if __name__ == "__main__":
    MemoryScramble().run()