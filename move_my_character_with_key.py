from pico2d import *

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global running, dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

running = True
x, y = 400, 90
frame = 0
dir_x, dir_y = 0,0

while running:
    clear_canvas()
    grass.draw(400,300,800,600)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    x += dir_x * 5
    y += dir_y * 5
    x = max(90, min(750,x))
    y = max(90, min(550,y))

    delay(0.05)

close_canvas()
#코파일럿의 도움을 받아 작성하였습니다.
