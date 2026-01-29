
import pygame
import random
from datetime import datetime
from constants import Colors
pygame.init()


window_height = 600
window_width = 800

UFO = {
    "width": 15,
    "height": 15,
    "color": Colors.BLUE,
    "speed": 3,
    "items": [],
}


tank = {
    "width": 30,
    "height": 15,
    "pos_x": window_width // 2,
    "pos_y": window_height - 30,
    "color": Colors.GREEN,
    "speed": 5,
    "projectiles": [],
}



font_tank_info = pygame.font.SysFont('Calibri', 10, True, False)

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Arcanoid Game")



is_running = True

clock = pygame.time.Clock()

is_KEY_DOWN = set()
last_fire_time = datetime.now()
while is_running:
    current_time = datetime.now()
    # Event handling and logic(update state)
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            is_KEY_DOWN.add(event.key)
        if event.type == pygame.KEYUP:
            is_KEY_DOWN.remove(event.key)
            
    for key in is_KEY_DOWN:
        if key == pygame.K_LEFT:
            tank["pos_x"] -= tank["speed"]
        if key == pygame.K_RIGHT:
            tank["pos_x"] += tank["speed"]
        if key == pygame.K_SPACE:
            if (current_time - last_fire_time).total_seconds() > 0.3:
                last_fire_time = current_time
                tank["projectiles"].append((tank["pos_x"]+tank["width"]//2,tank["pos_y"]-10))
            
    for i in range(len(tank["projectiles"])):
                tank["projectiles"][i] = (tank["projectiles"][i][0], tank["projectiles"][i][1]-10)
    tank["projectiles"] = [tank["projectiles"][i] for i in range(len(tank["projectiles"])) if tank["projectiles"][i][1] > 0]

    
    if len(UFO["items"]) < 5:
        UFO["items"].append(
            {
                "pos_x":  random.randint(0, window_width - UFO["width"]),
                "pos_y": 10,
            }
        )
    for item in UFO["items"]:
        r = random.randint(0, 3)
        if r == 0:
            item["pos_x"] -= UFO["speed"]
        elif r == 1:
            item["pos_x"] += UFO["speed"]
        elif r == 2:
            item["pos_y"] += UFO["speed"]
        if item["pos_y"] > window_height:
            UFO["items"].remove(item)

    for item in UFO["items"]:
        for projectile in tank["projectiles"]:
            if (
                item["pos_x"] < projectile[0] < item["pos_x"] + UFO["width"]
                and
                item["pos_y"] < projectile[1] < item["pos_y"] + UFO["height"]
            ):
                UFO["items"].remove(item)
                tank["projectiles"].remove(projectile)
                break

    # Drawing code
    screen.fill(Colors.WHITE)
    
    for item in UFO["items"]:
        pygame.draw.rect(
            screen,
            UFO["color"],
            (
                item["pos_x"],
                item["pos_y"],
                UFO["width"],
                UFO["height"],
            ),
        )

    pygame.draw.rect(
        screen,
        tank["color"],
        (
            tank["pos_x"],
            tank["pos_y"],
            tank["width"],
            tank["height"],
        ),
    )
    tank_info_str = f"Tank pos: ({tank['pos_x']}, {tank['pos_y']}) projectiles: {len(tank['projectiles'])}"
    text = font_tank_info.render(f"{tank_info_str}",True,Colors.BLACK)
    screen.blit(text, (tank["pos_x"],
            tank["pos_y"] - 15))
    for projectile in tank["projectiles"]:
        pygame.draw.circle(
            screen,
            Colors.RED,
            projectile,
            2,
        )
    pygame.display.flip()
    clock.tick(60)
    

