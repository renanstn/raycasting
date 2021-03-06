import math


# Game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH / 2
HALF_HEIGHT = HEIGHT / 2
FPS = 60
TILE = 100
SHOW_MAP = True
FPS_POSITION = (WIDTH - 65, 5)

# Minimap settings
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POSITION = (0, HEIGHT - HEIGHT // MAP_SCALE)

# Raycasting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
# NUM_RAYS = 120
MAX_DEPTH = 800  # Usado somente na versão não otimizada
DELTA_ANGLE = FOV / NUM_RAYS
DISTANCE = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJECTION_COEFFICIENT = 3 * DISTANCE * TILE
SCALE = WIDTH // NUM_RAYS

# Texture settings
TEXTURES_ON = True
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# Player settings
player_position = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
player_angle = 0
player_speed = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)
SANDY = (244, 164, 96)
DARKBROWN = (97, 61, 25)
DARKORANGE = (255, 140, 0)
