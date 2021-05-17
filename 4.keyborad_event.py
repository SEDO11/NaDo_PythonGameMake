#캐릭터를 움직일 수 있게 키보드 이벤트 넣기
import pygame

pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height)) # 화면

#화면 타이틀(제목) 설정
pygame.display.set_caption("Nado Game") #게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\donha\\OneDrive\\바탕 화면\\python\\PythonGame\\NaDo_PythonGameMake\\배경.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\donha\\OneDrive\\바탕 화면\\python\\PythonGame\\NaDo_PythonGameMake\\캐릭터.png")
character_size = character.get_rect().size # 캐릭터의 크기 구함
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로의 가장 아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0
keyspeed = 2

#이벤트 루프
running = True # 게임이 진행중인가 확인하는 변수
while running:
    for event in pygame.event.get(): # 파이게임을 위해 무조건 필요한 코드, 사용자의 동작을 체크하는 코드
        if event.type == pygame.QUIT: # 창의 x버튼을 눌렀을 때 이벤트 발생
            running = False # 게임이 진행중이 아니다라는 값으로 바꿈

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= keyspeed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += keyspeed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= keyspeed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += keyspeed

        if event.type == pygame.KEYUP: # 키가 때진걸 확인
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # 오른쪽과 왼쪽을 땔때
                to_x = 0 # 움직이지 않음
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP: # 위와 아래키를 땔때
                to_y = 0 # 움직이지 않음

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = screen_width - character_width
    
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > (screen_height - character_height):
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0)) #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기, 이게 있어야 배경화면이 그려짐

# pygame 종료
pygame.quit()