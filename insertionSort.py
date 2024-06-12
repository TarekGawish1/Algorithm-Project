import time
def insertion_sort(data, drawData):
    global start
    global end
    start = time.time()
    for i in range(len(data)):
        for j in range(i,0,-1):
            if data[j] < data[j - 1]:
                swap = data[j - 1]
                data[j - 1] = data[j]
                data[j] = swap
                time.sleep(0.6)	
                #dark orange for the swapped bar "smallest"and #green for the step we reach in bars 
                drawData(data, ['#3bbf88' if x == i else '#F95738' if x == j - 1  else '#F4D35E' for x in range(len(data))])	
    end = time.time()

                	
def duration_Itime():
    duration = str(round(end - start))+ " seconds"
    return duration