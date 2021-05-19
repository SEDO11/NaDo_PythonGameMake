# 게임 개발 프레임
import pygame

#############################################################################################
#기본 초기화 (반드시 필요한 부분들)
pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height)) # 화면

#화면 타이틀(제목) 설정
pygame.display.set_caption("SEDO Game") #게임 이름

# FPS
clock = pygame.time.Clock()
fps = 60
#############################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 설정)
########################################
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

# 캐릭터 이동 속도
# ex 캐릭터가 100 만큼 이동을 해야함
# 10 fps : 1초 동안에 10번 동작 -> 1번에 10만큼 이동
# 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼 이동
character_speed = 0.6

# 적 캐릭터
enemy = pygame.image.load("C:\\Users\\donha\\OneDrive\\바탕 화면\\python\\PythonGame\\NaDo_PythonGameMake\\적.png")
enemy_size = enemy.get_rect().size # 캐릭터의 크기 구함
enemy_width = enemy_size[0] #캐릭터의 가로크기
enemy_height = enemy_size[1] #캐릭터의 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos = screen_height - ((screen_height + enemy_height) / 2) # 화면 세로의 가장 아래에 위치

#폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트 종류, 크기)

#총 시간
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks() # 현재 틱 정보를 받아옴
############################################

#이벤트 루프
running = True # 게임이 진행중인가 확인하는 변수
while running:
    dt = clock.tick(fps) # 게임화면의 초당 프레임 수

    print("fps: " + str(clock.get_fps()))
    for event in pygame.event.get(): # 파이게임을 위해 무조건 필요한 코드, 사용자의 동작을 체크하는 코드
        #2. 이벤트 처리 키보드, 마우스
        if event.type == pygame.QUIT: # 창의 x버튼을 눌렀을 때 이벤트 발생
            running = False # 게임이 진행중이 아니다라는 값으로 바꿈
        
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 키가 때진걸 확인
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # 오른쪽과 왼쪽을 땔때
                to_x = 0 # 움직이지 않음
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP: # 위와 아래키를 땔때
                to_y = 0 # 움직이지 않음
    
    #3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt #캐릭터 이동
    character_y_pos += to_y * dt #캐릭터 이동

    # 캐릭터가 화면을 벗어나지 않게 해주는 것
    if character_x_pos < 0: # 가로
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = screen_width - character_width

    if character_y_pos < 0: # 세로
        character_y_pos = 0
    elif character_y_pos > (screen_height - character_height):
        character_y_pos = screen_height - character_height

    #4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect): # colliderect -> 캐릭터의 모양 기준으로 충돌이 있었는가
        print("충돌했어요")
        running = False

    #5. 화면에 그리기
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) #적 캐릭터 그리기

    #타이머 집어넣기, 경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간을 1000으로 나누어서 표시
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    #만약 시간이 0이하이면 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() # 게임화면을 다시 그리기, 이게 있어야 배경화면이 그려짐
# 잠시 대기
pygame.time.delay(2000)

# pygame 종료
print("게임을 종료합니다.")
pygame.quit()