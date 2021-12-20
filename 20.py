

program = """#.#...######..#####...#.####.#####.#.#.#.#..###.#.###...#.#..#.#.#......#.##...#.#.###....#.####.#.####.#..###...#####..####.##..####..##.##.....#..##...#.#..###.###.##..###.##.##....#....#.##..###....#.#...#..#.#.#.##.#.####..#....#..######..#####.##.#.#.##.##...##.#.#..##.#######.#..##..#...#...###..####.....#.#.#.###..###.##.....#####.#..##..####..#.##..#.#.....###.#.###.#.#....#.#.#..#.#..#.##..######.#.........##...##...##.#...##..##....###...##..##......#.#.#.###.##.#.#...#..##...#..........#...###..."""

# program = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"""

image_raw = """###.#.....###.#.....##.##..#.#..#.##....#..#..#.##..#..#.###.....#.##...#.#.####.##....##.#..#...#..
#..#...######.#....#.#.#.#.##.#..#####.###.####....#.##..##...#..###..##.##.#.#.##.#.#.#.#...#......
..#..##.#.##.#..#...##.######.###...#..####..#.#.#.##.##.#...####....####.#.#..#.#.##..###..##..##.#
.##..##..#.#...####.#..#.###....##.####....##.#.#..#...##.#.....####.#.#.#.#####..#..####.#.#...#..#
..#.#.##..######.##.#..##..####.#.##.....#..###..#......######......##..##.#...#.##..#..#.##..#.###.
..###..#####...####.#.#....#####....#..#.##.##.#..#########..##..#.#.#..#..#..#..#.###.#.....######.
#...#......#.##.#.#...##...####...#.##...#........###...##.....#.##..#######.###.##....#..##.#..####
##..#......#..#..##..####.##.#....###..#.####.#.####...###.###.##....#.#.###.#.#...###.#.....#.#...#
.#.###.##.......#.#..###......##.####.##.......##..##..##.....##.......###.#.#..##..#.#####.#.#.#.#.
#..##.#.......###..###..#..#.#.#..##...#.##.......#.#.#...###.#...#.#.#.#..###.#.#..#..####...###...
..#.##.#...##.#.#.##...####.#.#.###...#..##..###....#.#..#.#.###...#..###.#.##.###......#.#.#.#.###.
..###.#.###.#.#########...###...#.###.#..##..#######..###.#.#####.####...#.###...#.##..###.#.##....#
..#....#..#.###.##..###....#.##.###.##.........##.#..####.##.###..###.##.####.####..##..##...##.#...
..###..#...#...#.###.#..##.....#.#.##..####...##.#######.##.#.##...#.###......#.#..#.###.####.##..#.
###..#.#.#.......####.#...#.#.#.###...#.###.###..#......##..#......#.#.##.###..#...#.##...#..#..####
..###....#..##.##...#.#.#..#.##.####.##.#..#######.##.#...#.###.#..#.########.#.##.#.##.#...#..###..
...#.#.#.#.....###...#..#.#....#####........###........#.#..#.#.#...####.##.#..##..###.#########...#
..#...##..###.#.#.#.##....#..##..##.....#.##..#.##.#..#.........##.##..######.#.#..#...#....###...##
#.##..##.##.##.###...#.#..#.#.##...##...##..#..#....#.###..####..##.#....###.......#.###...#.....##.
#.#..###..#..##...#.#.########.##.#.###.############.##....#..####.###...#...#..#.###.#..#...#..#...
.#..#.##.##.#..##..#...#######.##.#...#.#.#..#.#.#.#....##.####.###..##.#.#..#.#......###.#..#####.#
.#....#.##.###..#....#..#..##......#.#.#..#.##..##...#.#.#.##...##.#..#.###....#...#.###..#.####..##
.###....#..#.###.#.#.#....######....#.###.####..####.######.##..###..#...##..#.##.#..######.#.#...#.
.#.#....####..#...###..###.##..#####.#...#.#.#.#.#..###..#..###..#.##.#.#.#.##...#.##.####.#..#.#...
#....#...##.#...####...##.#....#.#...#..######.###...#.##.####.##....##.#.####.###....#.##.##.####.#
.#.#####..##.....##.#..#.#..#..#####.....##....####.#####..#.#....#..###.##...#...###.#........##...
###.####.#.##...#####.#.#####...#.####..#....####..###.###..#.#...####.#....#..##...##.##..##.#####.
..##.##..#..#.##..#.##.#...#......##.#.##....##...#########.##...####.######.#.#.###.###.##.#.##..#.
...#.#####..#.#..#.#.#.####.###....#.#.####.###.......###.##.#.....#############.###..####..#.##.#..
...########.#..#..##.##..#.##.#..#...#.#####..###....#..#......#..##....#.#...#...#..##.####.##.#.#.
#.####.#.#..#...###.###....#..##...#....##..#..#.#####.#..####...#...#...#.#.####.#.###....#.#.....#
#..##.##.#..#####...##..#.....#..#.#.....####........####..##.##...##..#####...#..#.##...#..#....#.#
...##.###..#.###..###.#####..##.#.....##.##.#....##.#.#.#........#.##.##.#.#..#.##.#..##...#..##..##
##..#...###.#.#.####....#.#.##..#...#..###..#.###.#..#.##.....#..#..#########..#.##..##.##.#.....#..
#..###...#...####..#..#.....##.#.#....###..#.###...######..##..#.##...#....#.##.###.#..##...#.#..#.#
.#.....##.#.##.#.#####..#.#.##..###..##.##.##.#..######..######.##.#.###.#.#.##.#...##.#.#...####...
###..#.#.####.#...####..#.#.#..###.#######.##.#...####.#####.##.#...#...#...#..##..#######.#.#.#.#..
####.####..#####.#.#.....#...###..######.#..#.#.##.##.##..##...#..####....##..#.##...##..#.##.#...##
##....#...#.###.###.###.......#.#.......#..##.##.#.#.#.####.......###.#.#....######.#.....##....#...
#...#.######.##..#..##.##...#.##.##.##...#.#.####......#..##.##..#..#......###.#.##.#.#..##.##..#..#
.....#.#...###...#.....##.#.#.#.###....#..#..#.##.###.#......#.......#.#.##..###.###.###..#.##.#.#.#
..##..#.##.#####.#.##..#.###..#..##..##..##.##.#.#.#.#..#...#...####.##.##.#..#.#.#.##.#####....###.
#.#..####.####..##.#...#.#.#.#.###...#####.....##...###..#####.#.#..####.#...#.###.##..###..##...#..
###.####..#...#.#####...#...####.#.#....####.#.........#..###.#....######.######.###.#..#.....#..##.
#.##..#...##.###.#..###.#.#..#.#.###...#####.#.#..###...#.##...#...###..##..##....#..##.####..#....#
.#.##..####.########.##..#..##.#.#.####....###.#####...#.###..#...##..#.#####.#####...######.#.###..
.#..#.###..#.#.#.....###.#..#..###...###.#.##.#.##..##.##..##.#.#.##....##.##.##.##..#.#....##..#..#
.#.#.##.##..#..######.##...#######.#..#.#.#####.#..#....##.....##.##...####.......#.##.#.#.#..#####.
#####...#.##.##.###.#.#.#.#.##.###.#...#.#...#......###.#.#.###..#.#....#.....#...#.#..#.#.#.##...#.
##.#........#..#.###.#.#.#.......##..###.##...##....##.##..#.###..###...##...####.########.#..#####.
##.#..#.###.#.#.#.##.##.###..###.##....######...####.#.#.#...####....####.###...##..#.#.#..#..#...#.
##..#####.#####.#.##..###.#....####.#.#.#.#..##.#.####.###....####..#.##..#...##.##.#.#.####.##..#..
...#..##..#####..##.##.##.#..#...#.#.###.....#...###.#....#.#.####...#..####....#...###.#....##..###
##.#..#..#.#.####...#.#..##.###..###...#...#...#...#.#....##...#..##..####.....###.##...#..###..#...
#...########.....###....###.####..##.##.#.##.##..#..##..##...##....##.#..#..##..#.##..#..##..##.###.
..#..#.##.#..#...##.......#...#.##..#..####..##.##..##..#..##.###.#....#..#.#....#.###.###.......###
###.##.##.######........##..#.#####...###....##..#.#####..##..##...#.###.#.###.###.######.##..#.##.#
..#..##.....#.#.#...#...###.#..##...####...####.#.#..#####.##...##...#.#.#.###..#.#...#...####.##...
.####..#..##......#.#.#....###......###.########.#..#.##...##..##.##..######.#.####...##.##.##..###.
..#.#####..##.#..##....####.###..##.#.##.####..###..##.#.#.###...##..####.##.#.....#...####.#.#..###
####....#.##....#.#.##...######.#.#...#.#...#.#..####.#..#.#..###...#.#....#####.###...#....####..#.
..####...###..##..#..#..###..#.#...##.#.###...##....#.###..#...#####.#...##...####..#.#..#...##.###.
#####.##....#.#.##....#.#.#.#.#....##...#.##.#.#.##...#.###.....####..#.#....#.#.#.######..#.##..#..
####.#.##.##...###....##...##..#..#....##..#.#.#.#..#..###.......###.#.####..#.####.....#.#.##.#..##
..#.#.###..###########.#...#..###.###.#....#...##....#.#.#..##....#..#.#.##...#.###.....##.#.#...#..
.#..#.#..#.##...#####.##.....##.#.#.#..#.#.#....###.###.#..###.#....##..##..######......##.###.#..##
#.###..##.##...##.##.....#.#.#..##.#...#.##...#..#.#...###..#.......##...##...###.#.....###..##.#.##
..##.####..###.#.##..##.#....##.#####.#....#.#.#.#.##.##..#.#..#...###.#..#..#.....#....#..#.#...###
#.##...######..###.#.#.#...##.####.###..#.##.##.###.#..#.#.###..#..##.#..#..#..##..##.#.#.#..#..#...
##.##...###.##.#.#.......#..##..#..###..#...#.#..##########..#......#...#.##..#..##.###...###.######
#.#..#.###......#...###.###..#.........#.##.#.##.###....#.######..##..#.###.......#..##...###......#
....##.#.......##.#.#.###.###.####.#.#..##.#..##.#...####.#..#...#...#..##.###.#.#.####..##......##.
.#...######..##.##...#.####..#...#.....##.#####.##....###....#......#.#.##..#.#......#.#.#..###..##.
#.##..##...#####.#.####..#..##.###.####.#.#.###.##..####..###.####..#..##.#.###.....#####.##..#..###
.###.###.#.##..#...##.#..#.#..#######...#....#.#.....#..#.#....###.#..###....#.#.#.####....#.#.##..#
####..###..#....##....#.#.....#.##.#.##..##.###..#....##..######.##.##.#.#...##..###.###.#######.###
##.#.##..#########.#.##.###.#...#######.###.#.#.#######.##...#.#..##.#.##..##.#.#....####.#..######.
....#..#.####.#........#.#.#.#.##.....###.####..##....#.###...#...####.....###...#.###...###.##.####
#.....#..##..##.######.#...######..#.....#..##..#..###.#.###.###.#.##.....##.###..#......##......###
.#..#.......#..#...#...##.####..##...#.#.#.................#.##...##..##.#..##....#.....#...##..#.#.
#...###......#......#.######.#####..#....##..##....#.#..##.##.#....###.#.....###.#.#.#.......##.#...
#######.##..#.#.##.##...#...##..#.##.##.###..##.####.###.#.##.#..#.########.....######......#.#.#.##
#...##..#.#.........##.#...#...#..###.####.####.#.##.#..#.#..##..##.##.#..##..##...#...###.##.#.....
#.##.##....#....##.##...#####.....#.###...####.##.##..#.#.##.############...#..########.###..#.####.
##..#..#.###....##.###.##..#.#..#.##..#..#.#####.#....####.#..##...#########.###...#.#..#..##.#.###.
..#..........##...###......#..#.#..#.##.#####.....###.#.##....#..###.#.##.##..#.##.#.....#.#.#...##.
..#.#..#...#####.#.#.#.##.#..#.#.#####..##.......#.#..#.########..##.#..#.#..#...######...##...#..#.
..#..#......#..###..#...#....#.#.#..####...###.#..#.........#.#.######.#.##.#.#..##..#.####......#..
##.#.###.#...#.###..#.######.#...####.#.#####..#.#.##.....#..##.##.##...#####.....####.#.########..#
..###.###.##..####..#.....#.#..#...######.#.##.##..#.##.......#.##.###....##.##.####....####...#.#..
###.#.#.##.....#.######.#...#####.##.#..##..#.#.....##....####..#..#.##.#.#.##.###.#..###.###.#.....
..##.#.#.#.#...###.####.#.##.#..#.#.#..#..#..#######.####..#.#...##....#..#....###...##..####....###
..#..#..##.#####.#.....#...#.##......#...##...##..##.##.....##.#....##.#.#.#.#.#.#...##.#.#..###.#.#
.##.#.#....#..#..##.#.#..##.###.##.#######..####.##.####..#.#.#.....#.#..##...##..##.##.####...#.##.
#......##.....#.#..#..##.###.##.#..###.##..#.....#...##.##.##.#.##..#.###.#..#..#.#.......##...#...#
#.#.###..#.#####.......#....#....#...#..#.......#.####.#..#.....#....##..#####.##....##..##.##......
###...#.#....###.###...#..#.#.#....##..##.#..###.#..##...#..#..#.#.....#.####.#.##......##..#.####..
####.##...###.....##.##.....#.#.#....#.###.######.......#.###.#.........###.#...##.###..##..#.#..##.
.#..##.##.##...###.#.#..##...#.###...###.#...#....#...###....#...#.#..#.#.#.#....#.....####...#....#
.#.####.##.##..#...##.#.#.#...##.##.#######.#.##...#.#.#...##....#####.#..#.#..#...####.##.##...###.""".splitlines()

# image_raw = """#..#.
# #....
# ##..#
# ..#..
# ..###""".splitlines()

from copy import deepcopy

image = []
for i in range(51):
    image.append([0] * (len(image_raw[0]) + 102))
for line in image_raw:
    image.append([])
    for i in range(51):
        image[-1].append(0)
    for char in line:
        if char == "#":
            image[-1].append(1)
        elif char == ".":
            image[-1].append(0)
        else:
            print("WTF")
    for i in range(51):
        image[-1].append(0)
for i in range(51):
    image.append([0] * (len(image_raw[0]) + 102))

print(image)
updog = False
for round in range(50):
    newimage = deepcopy(image)
    for [i, line] in enumerate(image):
        for [j, bit] in enumerate(line):
            binary = 0
            if i > 0:
                if j > 0:
                    if image[i-1][j-1]:
                        binary += 256
                if image[i-1][j]:
                    binary += 128
                if j < len(line) - 1:
                    if image[i-1][j+1]:
                        binary += 64
            if j > 0:
                if image[i][j - 1]:
                    binary += 32
            if image[i][j]:
                binary += 16
            if j < len(line) - 1:
                if image[i][j + 1]:
                    binary += 8
            if i < len(image) - 1:
                if j > 0:
                    if image[i+1][j - 1]:
                        binary += 4
                if image[i+1][j]:
                    binary += 2
                if j < len(line) - 1:
                    if image[i+1][j + 1]:
                        binary += 1
            if updog:
                if i == 0 or j == 0 or i == len(image) - 1 or j == len(line) - 1:
                    binary = 511
            # print(i, j, binary)
            if program[binary] == "#":
                newimage[i][j] = 1
            elif program[binary] == ".":
                newimage[i][j] = 0
            else:
                print("WTF")

    image = deepcopy(newimage)
    updog = ~updog

    sum = 0
    for line in image:
        for num in line:
            if num:
                sum += 1
    print(round, sum)

