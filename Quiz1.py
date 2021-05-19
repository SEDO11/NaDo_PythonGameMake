import pygame
from random import *

pygame.init() # 초기화 (반드시 필요)

pygame.display.set_caption("SEDO Game") #게임 이름

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height)) # 화면

#화면 타이틀(제목) 설정
pygame.display.set_caption("SEDO 똥피하기 Game") #게임 이름

clock = pygame.time.Clock()
fps = 30

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\donha\\OneDrive\\바탕 화면\\python\\PythonGame\\NaDo_PythonGameMake\\배경.png")

# 캐릭터
character = pygame.image.load("C:\\Users\\donha\\OneDrive\\바탕 화면\\python\\PythonGame\\NaDo_PythonGameMake\\캐릭터.png")
character_size = character.get_rect().size # 캐릭터의 크기 구함
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로의 가장 아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0
character_speed = 0.5

# 똥
enemy = pygame.image.load("C:\\Users\\donha\\OneDrive\\바탕 화면\\python\\PythonGame\\NaDo_PythonGameMake\\적.png")
enemy_size = enemy.get_rect().size # 똥의 크기 구함
enemy_width = enemy_size[0] #똥의 가로크기
enemy_height = enemy_size[1] #똥의 세로크기
enemy_x_pos = randint(1, screen_width - enemy_width)
enemy_y_pos = 0

#폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트 종류, 크기)

#시작 시간
start_ticks = pygame.time.get_ticks() # 현재 틱 정보를 받아옴
timer = 0

# 점수
score = 0

#이벤트 루프
running = True # 게임이 진행중인가 확인하는 변수
while running:
    dt = clock.tick(fps)

    for event in pygame.event.get(): # 파이게임을 위해 무조건 필요한 코드, 사용자의 동작을 체크하는 코드
        if event.type == pygame.QUIT: # 창의 x버튼을 눌렀을 때 이벤트 발생
            running = False # 게임이 진행중이 아니다라는 값으로 바꿈

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed

        if event.type == pygame.KEYUP: # 키가 때진걸 확인
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # 오른쪽과 왼쪽을 땔때
                to_x = 0 # 움직이지 않음

    # 캐릭터의 이동속도 유지
    character_x_pos += to_x * dt         

    # 객체가 화면을 빠져나가지 못 하도록 설정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = screen_width - character_width

    #4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #똥이 랜덤으로 내려옴
    en_y = 0.5
    enemy_y_pos += en_y * dt
    if enemy_y_pos >= screen_height:
        enemy_x_pos = randint(1, screen_width - enemy_width + 1) # 화면상의 가로축에서 랜덤으로 나타남
        score += 1 # 똥을 피하면 점수 상승
        enemy_y_pos = 0 # 똥이 끝까지 내려왔을경우 다시 위로 올라감

    #충돌 체크
    if character_rect.colliderect(enemy_rect): # colliderect -> 캐릭터의 모양 기준으로 충돌이 있었는가
        print("충돌했어요")
        running = False

    #여기다가 점수 코드 쓰면 안뜸
    screen.blit(background, (0, 0)) #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #똥 그리기

    #점수
    scoreout = game_font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(scoreout, (10, 10))

    #타이머 집어넣기, 경과시간 계산
    timer = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간을 1000으로 나누어서 표시
    timerout = game_font.render("Time: " + str(int(timer + 1)), True, (255, 255, 255)) # 출력할 글자, True, 글자 색상
    screen.blit(timerout, (10, 50))

    pygame.display.update() # 게임화면을 다시 그리기, 이게 있어야 배경화면이 그려짐

# pygame 종료 
pygame.quit()