from aoc_get import get_input
import re

inp = get_input(20)
tiles_s = inp.split('\n\n')

class Monster:
    def __init__(self, monster_s):
        self.lines = monster_s.splitlines()
    
    def print(self):
        for line in self.lines:
            print(line)
        print('\n')

    def rotate(self):
        new_lines = [''] * len(self.lines[0])
        for line in self.lines:
            for i in range(len(line)):
                new_lines[i] += line[len(line) - 1 - i]
        self.lines = new_lines

    # switch top and bottom
    def flipv(self):
        self.lines = self.lines[::-1]

    # switch left and right
    def fliph(self):
        self.lines = [line[::-1] for line in self.lines]

    def get_lines(self):
        return self.lines.copy()


class Tile:
    def __init__(self, tile_s):
        self.lines = tile_s.splitlines()[1:]
        self.id = tile_s[5:9]
        self.reframe()

    def get_center(self):
        center_lines = []
        for line in self.lines[1:-1]:
            center_lines.append(line[1:-1])
        return center_lines

    def get_next_right(self, side):
        t1, t2 = side_table[side]
        if self.id == t1.id:
            return t2 
        else:
            return t1

    def get_next_bottom(self, side):
        t1, t2 = side_table[side]
        if self.id == t1.id:
            return t2 
        else:
            return t1

    def print(self):
        for line in self.lines:
            print(line)
        print('\n')

    def reframe(self):
        self.frame = self.get_frame()
        self.top, self.bottom, self.left, self.right = self.frame

    def rotate(self):
        new_lines = [''] * len(self.lines[0])
        for line in self.lines:
            for i in range(len(line)):
                new_lines[i] += line[len(line) - 1 - i]
        self.lines = new_lines
        self.reframe()

    # switch top and bottom
    def flipv(self):
        self.lines = self.lines[::-1]
        self.reframe()

    # switch left and right
    def fliph(self):
        self.lines = [line[::-1] for line in self.lines]
        self.reframe()

    def match_left(self, side):
        side_rev = side[::-1]
        while self.left != side and self.left != side_rev:
            self.rotate()
        if side != self.left:
            self.flipv()

    def match_top(self, side):
        side_rev = side[::-1]
        while self.top != side and self.top != side_rev:
            self.rotate()
        if side != self.top:
            self.fliph()

    def get_frame(self):
        top = self.lines[0]
        bottom = self.lines[-1] 
        left = right = '' 
        for line in self.lines:
            left += line[0]
            right += line[-1]
        return top, bottom, left, right

    def set_coords(self, x, y):
        self.coords = (x, y)

tiles = {}
side_table = {}
for s in tiles_s: 
    t = Tile(s) 
    tiles[t.id] = t
    for side in t.frame:
        if side in side_table:
            side_table[side].append(t)
        else:
            side_table[side] = [t]
            
        # edis is 'side' reversed
        edis = side[::-1]
        if edis in side_table:
            side_table[edis].append(t)
        else:
            side_table[edis] = [t]

def is_border(side_s):
    tiles = side_table[side_s] 
    return len(tiles) == 1

res = []

for tile in tiles.values():
    tile_score = 0
    frame = tile.get_frame()
    for side in frame:
        if is_border(side):
            tile_score += 1
    if tile_score == 2:
        res.append(tile.id)

# print(res)

p1 = 1
for r in res:
    p1 *= int(r)
print(p1)

top_left = tiles[res[0]] 

def set_first_tile(tile):
    
    while not (is_border(tile.left) and is_border(tile.top)):
        tile.rotate()
    return tile


first_tile = set_first_tile(top_left)

picture = [[first_tile]]
to_match_top = first_tile.bottom
to_match_left = first_tile.right
prev_tile = top_left


# set first column
while not is_border(to_match_top):
    next_tile = prev_tile.get_next_bottom(to_match_top)
    next_tile.match_top(to_match_top)
    picture.append([next_tile])
    prev_tile = next_tile
    to_match_top = next_tile.bottom

i = 0
while i < len(picture):
    prev_tile = picture[i][0]
    to_match_left = prev_tile.right
    while not is_border(to_match_left):
        next_tile = prev_tile.get_next_right(to_match_left)
        next_tile.match_left(to_match_left)
        prev_tile = next_tile
        picture[i].append(next_tile)
        to_match_left = next_tile.right
    i += 1

clean_pic = []
tile_height = len(first_tile.lines) - 2

for tile_row in picture:
    row_lines = [''] * tile_height
    for tile in tile_row:
        center_lines = tile.get_center()
        for i in range(tile_height):
            row_lines[i] += center_lines[i]
    clean_pic.extend(row_lines)

# the image is now straight. We just need to go through it and 
# locate all sea monsters.


monster_s = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''

m = Monster(monster_s)

# all horizontal symmetries
h_sprites = []
h_sprites.append(m.get_lines())
m.flipv()
h_sprites.append(m.get_lines())
m.fliph()
h_sprites.append(m.get_lines())
m.flipv()
h_sprites.append(m.get_lines())

m.rotate()

# all vertical symmetries
v_sprites = []
v_sprites.append(m.get_lines())
m.flipv()
v_sprites.append(m.get_lines())
m.fliph()
v_sprites.append(m.get_lines())
m.flipv()
v_sprites.append(m.get_lines())


# what is left? iterate clean_pic with all horizontal sprites, then
# verticals. Return and the number of monsters encountered
# then use that number to calculate water roughness


def check_for_monster_v(i, j, pic):
    m_count = 0
    for sprite in v_sprites:
        m_count += check_sprite(i, j, pic, sprite)
    return m_count

def check_for_monster_h(i, j, pic):
    m_count = 0
    for sprite in h_sprites:
        m_count += check_sprite(i, j, pic, sprite)
    return m_count

def check_sprite(i, j, pic, sprite):
    for x in range(len(sprite)):
        for y in range(len(sprite[0])):
            if sprite[x][y] == '#':
                if pic[i + x][j + y] != '#':
                    return False
    return True

num_monsters = 0

for i in range(len(clean_pic) - len(m.lines)):
    for j in range(len(clean_pic[0]) - len(m.lines[0])):
        num_monsters += check_for_monster_v(i, j, clean_pic)

m.rotate()
for i in range(len(clean_pic) - len(m.lines)):
    for j in range(len(clean_pic[0]) - len(m.lines[0])):
        num_monsters += check_for_monster_h(i, j, clean_pic)

num_hashtags = str(clean_pic).count('#')
num_bad_hashtags = str(monster_s).count('#') * num_monsters
diff = num_hashtags - num_bad_hashtags

p2 = diff
print(p2)
