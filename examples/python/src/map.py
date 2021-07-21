import settings


text_map = [
    '111111111111',
    '1.....2....1',
    '1.22.....2.1',
    '1..........1',
    '1.22..22...1',
    '1.2......2.1',
    '1.....2....1',
    '111111111111'
]

# Transforma o mapa de caracteres acima em um mapa de blocos
world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * settings.MAP_TILE, j * settings.MAP_TILE))
            if char == '1':
                world_map[(i * settings.TILE, j * settings.TILE)] = '1'
            if char == '2':
                world_map[(i * settings.TILE, j * settings.TILE)] = '2'
