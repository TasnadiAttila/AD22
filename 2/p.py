import os
import math

file = 'C:\\Users\\tasna\\Documents\\Szkript\\AD22\\2\\input.txt'

elf_1 = ['','A','B','C']
elf_2 = ['','X','Y','Z','X','Y']
#win_lose_draw
wld = ['Y','Z','X']

scores = [3,6,0]
part_1_score = 0
part_2_score = 0

i = 0
#read data in
with open(file) as f:
    games = f.read().splitlines()

for game in games:
    #get index of the first player [rock, paper, scissors]
    one_idx = elf_1.index(game.split()[0])
    #get the value of the second player
    two = game.split()[1]
    #get the offset index of the second player
    two_idx = elf_2.index(two,one_idx)
    part_1_score += elf_2.index(two) + scores[two_idx - one_idx]

    #get the index for win/lose/draw
    wld_idx = wld.index(two)
    #get the letter from the second elf at the index specified by win/lose/draw
    letter = elf_2[one_idx + wld_idx]
    part_2_score += elf_2.index(letter) + scores[wld_idx]

print("Day 2 Part 1: " + str(part_1_score))
print("Day 2 Part 2: " + str(part_2_score))