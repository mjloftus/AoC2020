import os
os.chdir('D:\\Users\\Mike\\Advent of Code\\2020\\Day 5')

def findSeatPos(boardingPass):
    row = 0
    col = 0
    maxRows = 1
    maxCols = 1
    rowD = {'F': 0, 'B': 1}
    colD = {'L': 0, 'R': 1}
    for c in boardingPass:
        if c in rowD.keys():
            row <<= 1
            row += rowD[c]
            maxRows <<= 1
        elif c in colD.keys():
            col <<= 1
            col += colD[c]
            maxCols <<= 1
    return row, col, maxCols

def findId(boardingPass):
    row, col, maxCols = findSeatPos(boardingPass)
    return row * maxCols + col

def findHighestId(fp='input.txt'):
    highestId = 0
    with open(fp) as f:
        for boardingPass in f:
            seatId = findId(boardingPass)
            if findId(boardingPass) > highestId:
                highestId = seatId
    return highestId

def findOpenSeat(fp='input.txt'):
    takenSeats = []
    with open(fp) as f:
        for boardingPass in f:
            takenSeats.append(findId(boardingPass))
    openSeats = list(set(range(max(takenSeats)+1)).difference(takenSeats))
    seats = []
    for seatId in openSeats:
        if seatId + 1 not in openSeats and seatId - 1 not in openSeats:
            seats.append(seatId)
    return seats
