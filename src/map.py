import settings


# Os Ws são paredes, os pontinhos são chão
text_map = [
    'WWWWWWWWWWWW',
    'W......W...W',
    'W..WWW...W.W',
    'W....W..WW.W',
    'W..W....W..W',
    'W..W...WWW.W',
    'W....W.....W',
    'WWWWWWWWWWWW'
]

# Transforma o mapa de caracteres acima em um mapa de blocos
world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * settings.TILE, j * settings.TILE))
