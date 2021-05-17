#배경 이미지 넣기
import pygame

pygame.init() # 초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height)) # 화면

#화면 타이틀(제목) 설정
pygame.display.set_caption("Nado Game") #게임 이름

# 배경 이미지 불러오기
# background = pygame.image.load("C:\\Users\\donha\\OneDrive\\바탕 화면\\python\\PythonGame\\NaDo_PythonGameMake\\배경.png")


#이벤트 루프
running = True # 게임이 진행중인가 확인하는 변수
while running:
    for event in pygame.event.get(): # 파이게임을 위해 무조건 필요한 코드, 사용자의 동작을 체크하는 코드
        if event.type == pygame.QUIT: # 창의 x버튼을 눌렀을 때 이벤트 발생
            running = False # 게임이 진행중이 아니다라는 값으로 바꿈
    
    screen.fill((0,255,0))
    # screen.blit(background, (0, 0)) #배경 그리기

    pygame.display.update() # 게임화면을 다시 그리기, 이게 있어야 배경화면이 그려짐

# pygame 종료
pygame.quit()