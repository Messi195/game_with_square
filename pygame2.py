# Импортируем библиотеку pygame для создания игр и модуль random для случайных чисел
import pygame
import random

# Инициализируем все модули Pygame (графика, звук, ввод-вывод и др.)
pygame.init()

# --- Настройки окна ---
# Кортеж, задающий размеры окна (ширина, высота)
window_size = (800, 600)
# Создаем главное окно игры с заданными размерами
screen = pygame.display.set_mode(window_size)
# Устанавливаем заголовок окна (имя приложения)
pygame.display.set_caption("ИГРА")
# Создаем объект Clock для управления частотой обновления игры (FPS)
clock = pygame.time.Clock()

# --- Определение цветов ---
# Цвет белый (значения RGB)
WHITE = (255, 255, 255)
# Цвет черный (значения RGB)
BLACK = (0, 0, 0)
# Цвет синий (значения RGB)
BLUE = (0, 0, 255)
# Цвет красный (значения RGB)
RED = (255, 0, 0)

# --- Параметры игрока ---
# Ширина и высота прямоугольника игрока
player_width, player_height = 50, 50
# Скорость передвижения игрока (пикселей за шаг)
player_speed = 10

# --- Параметры врага ---
# Ширина и высота прямоугольника врага
enemy_width, enemy_height = 50, 50

# --- Фоновая музыка ---
# Загружаем музыкальный файл для фона (укажите путь к файлу)
# pygame.mixer.music.load("./music.mp3")
# # Проигрываем музыку в бесконечном цикле (-1 означает повтор)
# pygame.mixer.music.play(-1)

# --- Функция для отображения текста ---
def draw_text(text, x, y, color, size=36):
    # Создаем объект шрифта с заданным размером
    font = pygame.font.Font(None, size)
    # Рендерим текст (делаем текст пригодным для отображения на экране)
    rendered_text = font.render(text, True, color)
    # Отображаем текст на экране в заданных координатах (x, y)
    screen.blit(rendered_text, (x, y))

# --- Функция финишного экрана ---
def finish_screen(score):
    # Заполняем весь экран черным цветом (очищаем экран)
    screen.fill(BLACK)
    # Отображаем сообщение "ИГРА ЗАВЕРШЕНА!" крупным белым шрифтом на экране
    draw_text("ИГРА ЗАВЕРШЕНА!", 220, 200, WHITE, size=50)
    # Показываем итоговый счёт игрока
    draw_text(f"Ваш счёт: {score}", 310, 300, WHITE, size=40)
    # Выводим инструкцию для выхода из игры (ESC)
    draw_text("Нажмите [ESC], чтобы выйти", 245, 400, WHITE, size=30)
    # Выводим инструкцию для перезапуска игры (R)
    draw_text("Нажмите [R], чтобы сыграть снова", 220, 450, WHITE, size=30)
    # Обновляем экран, чтобы отображаемые тексты стали видны
    pygame.display.flip()

    # Цикл обработки событий для финишного экрана
    while True:
        for event in pygame.event.get():
            # Проверяем, если пользователь закрывает окно игры
            if event.type == pygame.QUIT:
                pygame.quit()  # Завершаем работу Pygame
                exit()  # Полностью прерываем выполнение программы
            # Проверяем нажатия клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Если нажата клавиша ESC
                    pygame.quit()  # Закрываем Pygame
                    exit()  # Полностью завершаем программу
                if event.key == pygame.K_r:  # Если нажата клавиша R
                    return  # Выходим из функции, чтобы перезапустить игру

# --- Основной игровой процесс ---
def main_game():
    global score  # Объявляем глобальную переменную для счёта

    # Устанавливаем начальные координаты игрока
    player_x, player_y = 100, 300
    # Генерируем случайные координаты для врага
    enemy_x = random.randint(0, 750)
    enemy_y = random.randint(0, 550)

    # Создаем прямоугольник игрока (для отслеживания положения)
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    # Создаем прямоугольник врага
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    # Сброс переменной для счёта
    score = 0
    # Фиксируем момент старта игры (время в миллисекундах)
    start_ticks = pygame.time.get_ticks()
    # Устанавливаем продолжительность игры в секундах
    game_duration = 10

    # Флаг для работы игрового цикла
    running = True
    while running:
        # --- Обработка событий ---
        for event in pygame.event.get():
            # Если окно закрыто, завершаем игру
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # --- Проверка таймера ---
        # Рассчитываем прошедшее время (в секундах)
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        # Рассчитываем оставшееся время, но не допускаем отрицательных значений
        remaining_time = max(0, int(game_duration - elapsed_time))

        # Если время закончилось, завершаем игровой цикл
        if remaining_time == 0:
            break

        # --- Обработка нажатий клавиш ---
        keys = pygame.key.get_pressed()  # Получаем состояние всех клавиш
        # Если нажата клавиша LEFT и игрок не выходит за границу окна
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed  # Двигаем игрока влево
        # Если нажата клавиша RIGHT и игрок не выходит за границу окна
        if keys[pygame.K_RIGHT] and player_x < window_size[0] - player_width:
            player_x += player_speed  # Двигаем игрока вправо
        # Если нажата клавиша UP и игрок не выходит за верхний край окна
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed  # Двигаем игрока вверх
        # Если нажата клавиша DOWN и игрок не выходит за нижний край окна
        if keys[pygame.K_DOWN] and player_y < window_size[1] - player_height:
            player_y += player_speed  # Двигаем игрока вниз

        # --- Обновляем положение игрока ---
        player_rect.topleft = (player_x, player_y)

        # --- Проверяем столкновение игрока с врагом ---
        if player_rect.colliderect(enemy_rect):
            score += 1  # Увеличиваем счёт
            # Перемещаем врага в случайное место на экране
            enemy_x = random.randint(0, 750)
            enemy_y = random.randint(0, 550)
            enemy_rect.topleft = (enemy_x, enemy_y)

        # --- Отрисовка ---
        # Очищаем экран, заполняя его чёрным цветом
        screen.fill(BLACK)
        # Рисуем игрока (синий прямоугольник)
        pygame.draw.rect(screen, BLUE, player_rect)
        # Рисуем врага (красный прямоугольник)
        pygame.draw.rect(screen, RED, enemy_rect)
        # Отображаем текущий счёт игрока
        draw_text(f"Счет: {score}", 10, 10, WHITE)
        # Отображаем оставшееся время
        draw_text(f"Время: {remaining_time} сек", 10, 40, WHITE)

        # Обновляем экран, чтобы изменения стали видимыми
        pygame.display.flip()
        # Ограничиваем FPS игры до 60 кадров в секунду
        clock.tick(60)

    # После завершения игры отображаем финишный экран
    finish_screen(score)

# --- Главный цикл программы ---
while True:
    main_game()  # Запускаем основной игровой процесс 