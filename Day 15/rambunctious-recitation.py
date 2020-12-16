from collections import defaultdict

def memoryGame(queue):
    mostRecent = dict()
    turn = 0
    speak = 0
    duration = 0
    # starting numbers
    for i in queue[:len(queue)-1]:
        turn += 1
        mostRecent[i] = turn
        
    queue = queue[len(queue)-1:]
        
    while turn < 30000000:
        turn += 1
        speak = queue.pop(0)
        if speak not in mostRecent.keys():
            mostRecent[speak] = turn
            duration = 0
        else:
            duration = turn - mostRecent[speak]
            mostRecent[speak] = turn
        queue.append(duration)
    return speak

memoryGame([0,20,7,16,1,18,15])
