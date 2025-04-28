import pygame


def draw_palette():
    palette.fill(background_color)
    for i in range(len(colors)):
        color_rect = pygame.Rect(i * size, 0, size, size)
        pygame.draw.rect(palette, colors[i], color_rect)

    border_rect = pygame.Rect(CUR_INDEX * size, 0, size, size)
    pygame.draw.rect(palette, BORDER_COLOR, border_rect, width=3)
    screen.blit(palette, palette_rect.topleft)


# Инициализация pygame
pygame.init()

# Создаем окно размерами 800 на 600 пикселей
screen = pygame.display.set_mode((800, 600))

# Цвет фона (белый) и цвет кисти (черный)
background_color = (255, 255, 255)
brush_color = (0, 0, 0)

# Толщина кисти
brush_width = 5

# Холст для рисования
canvas = pygame.Surface(screen.get_size())
canvas.fill(background_color)

# Задаем константы для цветов
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (238, 130, 238)
PINK = (255, 192, 203)
GRAY = (192, 192, 192)
BLACK = (0, 0, 0)

# Константа для цвета рамки
BORDER_COLOR = (0, 0, 0)

# 10 цветов в палитре
colors = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET, PINK, GRAY, BLACK]

# Для хранения индекса выбранного цвета в палитре
CUR_INDEX = 0

# Поверхность для палитры цветов
size = 50  # Размер ячейки с цветом

# Объект Rect для палитры
palette_rect = pygame.Rect(10, 10, size * len(colors), size)
palette = pygame.Surface(palette_rect.size)

dragging_palette = False
running = True

# Главный цикл игры
while running:
    for event in pygame.event.get():
        # Выход из программы
        if event.type == pygame.QUIT:
            running = False
            # Сохранение скриншота при выходе
            pygame.image.save(screen, "screenshot.png")
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_pos = pygame.mouse.get_pos()
            if palette_rect.collidepoint(mouse_pos):
                print("Начало перемещения палитры")
                dragging_palette = True
                offset = (mouse_pos[0] - palette_rect.left, mouse_pos[1] - palette_rect.top)
            else:
                print("Не палитра")
                dragging_palette = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            print("Конец перемещения")
            dragging_palette = False

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed[0]:  # Левая кнопка мыши нажата
        if palette_rect.collidepoint(mouse_pos):
            selected_color_index = (mouse_pos[0] - palette_rect.left) // size
            CUR_INDEX = selected_color_index
            brush_color = colors[CUR_INDEX]
        else:
            pygame.draw.circle(canvas, brush_color, mouse_pos, brush_width)

    if dragging_palette:
        new_pos = (pygame.mouse.get_pos()[0] - offset[0],
                   pygame.mouse.get_pos()[1] - offset[1])
        palette_rect.topleft = new_pos

    # Отображение рисунка на экране
    screen.blit(canvas, (0, 0))

    # Рисование палитры
    draw_palette()

    # Обновляем экран
    pygame.display.flip()