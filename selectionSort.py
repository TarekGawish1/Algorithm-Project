import time

def selection_sort(data,drawData):
    global start
    global end
    start = time.time()
    for i in range(len(data)):      
        smallerIndx=None    
        cur=data[i]             
        for j in range(i,len(data)):
            if cur>=data[j]:
                cur=data[j]
                smallerIndx=j
                drawData(data, ['#F95738' if x == i or x == smallerIndx else '#F4D35E' for x in range(len(data))] )
                time.sleep(0.3)
        data[smallerIndx],data[i]=data[i],data[smallerIndx]
        time.sleep(0.6)
    end = time.time()
    drawData(data, ['#F95738' for x in range(len(data))])
    

def duration_Stime():
    duration = str(round(end - start)) + " seconds"
    return duration

