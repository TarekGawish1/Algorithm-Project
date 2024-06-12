import time
arr=[]
def partition(data, head, tail, drawData):
    global start
    global end
    start = time.time()

    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(0.05)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(0.03)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(0.3)


    #swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(0.5)
    end = time.time()
    data[border], data[tail] = data[tail], data[border]
    arr.append(end-start)
    return border

start=None
end=None
def quick_sort(data, head, tail, drawData):
    if head < tail:

        partitionIdx = partition(data, head, tail, drawData)

        #LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawData, )

        #RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawData, )


def getColorArray(dataLen, head, tail, border, currIdx, swaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('#F4D35E')
        else:
            colorArray.append('#F95738')

        if i == tail:
            colorArray[i] = '#D90429'
        elif i == border:
            colorArray[i] = '#2B2D42'
        elif i == currIdx:
            colorArray[i] = '#B04AFA'

        if swaping:
            if i == border or i == currIdx:
                colorArray[i] = '#1b998b'

    return colorArray

def duration_Qtime():
    sum=0
    for i in arr:
        sum=sum+i
    return str(round(sum))


