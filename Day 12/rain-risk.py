import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 12')

def findDistance(fp='input.txt'):
    inst = open(fp).read().strip('\n').split('\n')
    dx = 0
    dy = 0
    rot = ['N', 'E', 'S', 'W']
    face = 'E'
    for i in inst:
        faceDir = i[0]
        val = int(i[1:])
        if faceDir == 'F':
            faceDir = face
        if faceDir == 'N':
            dy += val
        if faceDir == 'E':
            dx += val
        if faceDir == 'S':
            dy -= val
        if faceDir == 'W':
            dx -= val
        if faceDir == 'R':
            face = rot[int((rot.index(face) + val/90) % 4)]
        if faceDir == 'L':
            face = rot[int((rot.index(face) - val/90) % 4)]
    return abs(dx) + abs(dy)

def findWaypoint(fp='input.txt'):
    inst = open(fp).read().strip('\n').split('\n')
    dx = 0
    dy = 0
    waypoint = [10, 1]
    for i in inst:
        rot = {0: [waypoint[0], waypoint[1]], 1: [waypoint[1], 0 - waypoint[0]],
               2: [0 - waypoint[0], 0 - waypoint[1]], 3: [0 - waypoint[1], waypoint[0]]}
        faceDir = i[0]
        val = int(i[1:])
        if faceDir == 'F':
            dx += (val * waypoint[0])
            dy += (val * waypoint[1])
        if faceDir == 'N':
            waypoint[1] += val
        if faceDir == 'E':
            waypoint[0] += val
        if faceDir == 'S':
            waypoint[1] -= val
        if faceDir == 'W':
            waypoint[0] -= val
        if faceDir == 'R':
            waypoint = rot[(val/90) % 4]
        if faceDir == 'L':
            waypoint = rot[(4 - (val/90)) % 4]
    return abs(dx) + abs(dy)
    
