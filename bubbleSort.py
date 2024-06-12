import time

def bubble_sort(data, drawData):
    global start
    global end
    start = time.time()
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['#F95738' if x == j or x == j+1 else '#F4D35E' for x in range(len(data))] )
                
                time.sleep(0.6)
    end = time.time()
    drawData(data, ['#F95738' for x in range(len(data))])


def duration_Btime():
    duration =  str(round(end - start))+ " seconds"
    return duration

