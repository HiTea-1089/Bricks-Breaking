import pygame
from pygame.locals import *
from sys import exit

# 初始化游戏引擎
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Breakout Clone")

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 定义游戏元素尺寸
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 20
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
BALL_RADIUS = 10

# 定义游戏元素初始位置
paddle_x = 280
paddle_y = 460
ball_x = 320
ball_y = 240

# 定义游戏元素初始速度
ball_speed_x = 0.1
ball_speed_y = -0.1

# 定义砖块列表
blocks = []
for row in range(5):
    for col in range(11):
        blocks.append(pygame.Rect(60 * col, 20 * row, BLOCK_WIDTH, BLOCK_HEIGHT))

# 定义游戏状态
game_state = "start"  # 可选值为 "start"、"game"、"game_over" 或 "win"

# 定义按钮尺寸
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

# 定义按钮颜色
BUTTON_COLOR = BLUE
BUTTON_HOVER_COLOR = GREEN

# 定义按钮文本颜色
BUTTON_TEXT_COLOR = WHITE

# 定义按钮文本字体
BUTTON_FONT = pygame.font.SysFont(None, 24)

# 定义按钮文本
LEAVE_TEXT = "Leave"
RESTART_TEXT = "Restart"
START_TEXT = "Start"

# 定义按钮位置
leave_button_x = 270
leave_button_y = 300
restart_button_x = 270
restart_button_y = 220
start_button_x = 270
start_button_y = 220

# 定义按钮矩形
leave_button_rect = pygame.Rect(
    leave_button_x, leave_button_y, BUTTON_WIDTH, BUTTON_HEIGHT
)
restart_button_rect = pygame.Rect(
    restart_button_x, restart_button_y, BUTTON_WIDTH, BUTTON_HEIGHT
)
start_button_rect = pygame.Rect(
    start_button_x, start_button_y, BUTTON_WIDTH, BUTTON_HEIGHT
)

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == MOUSEMOTION:
            paddle_x = event.pos[0] - PADDLE_WIDTH / 2
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键点击
                if game_state == "start":
                    if start_button_rect.collidepoint(event.pos):
                        game_state = "game"
                    elif leave_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()
                elif game_state == "game":
                    if leave_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()
                    elif restart_button_rect.collidepoint(event.pos):
                        # 重新初始化游戏元素位置和状态
                        paddle_x = 280
                        paddle_y = 460
                        ball_x = 320
                        ball_y = 240
                        blocks = []
                        for row in range(5):
                            for col in range(11):
                                blocks.append(
                                    pygame.Rect(
                                        60 * col, 20 * row, BLOCK_WIDTH, BLOCK_HEIGHT
                                    )
                                )
                        game_state = "game"  # 重置游戏状态
                elif game_state == "game_over" or game_state == "win":
                    if leave_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()
                    elif restart_button_rect.collidepoint(event.pos):
                        # 重新初始化游戏元素位置和状态
                        paddle_x = 280
                        paddle_y = 460
                        ball_x = 320
                        ball_y = 240
                        blocks = []
                        for row in range(5):
                            for col in range(11):
                                blocks.append(
                                    pygame.Rect(
                                        60 * col, 20 * row, BLOCK_WIDTH, BLOCK_HEIGHT
                                    )
                                )
                        game_state = "game"  # 重置游戏状态

    screen.fill(BLACK)

    if game_state == "start":
        # 绘制"Breakout clone"文本
        font = pygame.font.SysFont(None, 48)
        text = font.render("Breakout clone", True, WHITE)
        text_rect = text.get_rect(center=(320, 150))
        screen.blit(text, text_rect)

        # 绘制"Made By HiTea with Machinet AI"小字
        small_font = pygame.font.SysFont(None, 18)
        small_text = small_font.render(
            "Made By HiTea with Machinet AI & Debugging by ChatGPT", True, WHITE
        )
        small_text_rect = small_text.get_rect(center=(320, 180))
        screen.blit(small_text, small_text_rect)

        # 绘制Copyright小字
        small_font = pygame.font.SysFont(None, 18)
        small_text = small_font.render("Copyright © 2023 HiTea", True, WHITE)
        small_text_rect = small_text.get_rect(center=(320, 430))
        screen.blit(small_text, small_text_rect)

        # 绘制Email小字
        small_font = pygame.font.SysFont(None, 18)
        small_text = small_font.render("Email: gepi45458@gmail.com", True, WHITE)
        small_text_rect = small_text.get_rect(center=(320, 470))
        screen.blit(small_text, small_text_rect)

        # 绘制开始游戏按钮
        pygame.draw.rect(screen, BUTTON_COLOR, start_button_rect)
        start_text = BUTTON_FONT.render(START_TEXT, True, BUTTON_TEXT_COLOR)
        start_text_rect = start_text.get_rect(center=start_button_rect.center)
        screen.blit(start_text, start_text_rect)

        # 绘制离开游戏按钮
        pygame.draw.rect(screen, BUTTON_COLOR, leave_button_rect)
        leave_text = BUTTON_FONT.render(LEAVE_TEXT, True, BUTTON_TEXT_COLOR)
        leave_text_rect = leave_text.get_rect(center=leave_button_rect.center)
        screen.blit(leave_text, leave_text_rect)

    elif game_state == "game":
        # 绘制挡板
        pygame.draw.rect(
            screen, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        )

        # 绘制球
        pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

        # 绘制砖块
        for block in blocks:
            pygame.draw.rect(screen, GREEN, block)

        # 更新球的位置
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # 球与边界的碰撞检测
        if ball_x - BALL_RADIUS < 0 or ball_x + BALL_RADIUS > 640:
            ball_speed_x = -ball_speed_x
        if ball_y - BALL_RADIUS < 0:
            ball_speed_y = -ball_speed_y
        elif ball_y + BALL_RADIUS > 480:
            game_state = "game_over"

        # 球与挡板的碰撞检测
        if (
            ball_y + BALL_RADIUS > paddle_y
            and ball_x > paddle_x
            and ball_x < paddle_x + PADDLE_WIDTH
        ):
            ball_speed_y = -ball_speed_y

        # 球与砖块的碰撞检测
        for block in blocks:
            if block.colliderect(
                pygame.Rect(
                    ball_x - BALL_RADIUS,
                    ball_y - BALL_RADIUS,
                    BALL_RADIUS * 2,
                    BALL_RADIUS * 2,
                )
            ):
                blocks.remove(block)
                ball_speed_y = -ball_speed_y

        # 当所有砖块清空时，游戏胜利
        if len(blocks) == 0:
            game_state = "win"

    elif game_state == "game_over":
        # 绘制"You Lose!"文本
        font = pygame.font.SysFont(None, 36)
        text = font.render("You Lose!", True, WHITE)
        text_rect = text.get_rect(center=(320, 150))
        screen.blit(text, text_rect)

        # 绘制重新开始游戏按钮
        pygame.draw.rect(screen, BUTTON_COLOR, restart_button_rect)
        restart_text = BUTTON_FONT.render(RESTART_TEXT, True, BUTTON_TEXT_COLOR)
        restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)
        screen.blit(restart_text, restart_text_rect)

        # 绘制离开游戏按钮
        pygame.draw.rect(screen, BUTTON_COLOR, leave_button_rect)
        leave_text = BUTTON_FONT.render(LEAVE_TEXT, True, BUTTON_TEXT_COLOR)
        leave_text_rect = leave_text.get_rect(center=leave_button_rect.center)
        screen.blit(leave_text, leave_text_rect)

    elif game_state == "win":
        # 绘制"You Win!"文本
        font = pygame.font.SysFont(None, 36)
        text = font.render("You Win!", True, WHITE)
        text_rect = text.get_rect(center=(320, 150))
        screen.blit(text, text_rect)

        # 绘制重新开始游戏按钮
        pygame.draw.rect(screen, BUTTON_COLOR, restart_button_rect)
        restart_text = BUTTON_FONT.render(RESTART_TEXT, True, BUTTON_TEXT_COLOR)
        restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)
        screen.blit(restart_text, restart_text_rect)

        # 绘制离开游戏按钮
        pygame.draw.rect(screen, BUTTON_COLOR, leave_button_rect)
        leave_text = BUTTON_FONT.render(LEAVE_TEXT, True, BUTTON_TEXT_COLOR)
        leave_text_rect = leave_text.get_rect(center=leave_button_rect.center)
        screen.blit(leave_text, leave_text_rect)

    # 更新屏幕
    pygame.display.update()
