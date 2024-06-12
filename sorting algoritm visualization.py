from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from bubbleSort import bubble_sort,duration_Btime
from selectionSort import selection_sort,duration_Stime
from insertionSort import insertion_sort,duration_Itime
from quickSort import quick_sort,duration_Qtime

import random

# the creation of window
win = Tk()
# The size of window
win.geometry("1350x750")
win.title('Visualisation of sorting algorithms')
win.config(bg='#0D3B66')

# intialization of data list
data = []
# Function that responsible for the drawing of Bars
def drawData(data, colorArray):

    canvas.delete("all")
    canvas_height = 520
    canvas_width = 1360
    
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spac_btween_canvas = 6
    # normalize data as ratios for drawing
    normaliz_data = [ i / max(data) for i in data]
    
    for i, height in enumerate(normaliz_data):
        # Top left Corner
        x0 = i * x_width + offset + spac_btween_canvas
        y0 = canvas_height - height * 500
        # Bottom right corner
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i]) 
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    win.update_idletasks()

# Function for the generation of random numbers of bars
def generating_random_numbers():
    global data
    #try and exept if no input for The size
    try:
        size = int(size_entry.get())
    except:
        size = 10
    if size > 100 : size = 100

    data = []
    for _ in range(size):
        data.append(random.randrange(size))

    drawData(data, ['#F4D35E' for x in range(len(data))])



def quick_colors():
    colors_list = ['#F4D35E','#F95738','#D90429','#2B2D42','#B04AFA','#1b998b']
    name_list = ['unsorted' , 'sorted' ,'tail' , 'index' , 'pivot' ,'swap'  ]
    m = 10
    for i in range (len(colors_list)):

        squar1 = Frame(win, width=25, height=25, bg=colors_list[i])
        squar1.place(x=60+m,y = 100)
        

        names1 = Label(win, text=name_list[i], bg='#FAF0CA')
        names1.place(x=100+m,y = 100)
        i = i+1
        m = m+200

# function of driver code "The code that executes the program"
def sort_algorithm():
    global data
    if not data: 
        return
################## Bubble sort ###############
    if algorithm_list.get() == "Bubble Sort":
        bubble_sort(data, drawData)
        complexty = Label(frame3, text = "O(n^2)", bg='#FAF0CA' , font=1, foreground="red")
        complexty.place(x=200, y=10)

        time = Label(frame3, text = "Duration Time: " + duration_Btime(), bg='#FAF0CA' , font=1)
        time.place(x=15, y=45)
################## Selection sort ###############
    elif algorithm_list.get() == "selection sort":
        selection_sort(data, drawData)

        complexty = Label(frame3, text = "O(n^2)" , bg='#FAF0CA' , font=1, foreground="red")
        complexty.place(x=200, y=10)

        time = Label(frame3, text = "Duration Time: " + duration_Stime(), bg='#FAF0CA' , font=1)
        time.place(x=15, y=45)
################## Insertion sort ###############

    elif algorithm_list.get() == "Insertion sort":
        insertion_sort(data, drawData)

        complexty = Label(frame3, text = "O(n^2)" , bg='#FAF0CA' , font=1, foreground="red")
        complexty.place(x=200, y=10)

        time = Label(frame3, text = "Duration Time: " + duration_Itime(), bg='#FAF0CA' , font=1)
        time.place(x=15, y=45)

################## Quick sort ###############

    elif algorithm_list.get() == "Quick Sort":
        quick_colors()
        quick_sort(data, 0, len(data)-1, drawData)

        complexty = Label(frame3, text = "O(nlogn)", bg='#FAF0CA' , font=1, foreground="red")
        complexty.place(x=200, y=10)

        time = Label(frame3, text = "Duration Time: " + duration_Qtime() +  " seconds", bg='#FAF0CA' , font=1)
        time.place(x=15, y=45)        
    drawData(data, ['#F95738' for x in range(len(data))]) 

#### Generate Button
generat = Button(win, text="Generate", command=generating_random_numbers, bg='#F95738', fg='white' ,font = 1)
generat.place(x = 270, y=30)

canvas = Canvas(win, width=1330, height=520, bg='#FAF0CA')
canvas.place(x=10,y = 135)


#### Size entry part
frame1 = Frame(win, width=250, height=80, bg='#FAF0CA') 
frame1.place(x=10,y = 10)

size = Label(frame1, text=" Size : ", bg='#FAF0CA' ,font = 1 )
size.place(x=20,y = 25)

size_entry = Entry(frame1)
size_entry.place(x=100,y = 30)


### Algorithm Selection list

frame2 = Frame(win, width=300 , height=80, bg='#FAF0CA') 
frame2.place(x=450,y = 10)

algorithm = Label(frame2, text="Algorithm: ", bg='#FAF0CA' , font=1)
algorithm.place(x=15, y=25)

algorithm_list = ttk.Combobox(frame2, textvariable=StringVar(),
    values=["Bubble Sort", "selection sort" ,"Insertion sort" , "Quick Sort"])
algorithm_list.current(0)
algorithm_list.place(x=125, y=30)


# Sort button
sort = Button(win, text="Sort", bg='#F95738', fg='white' ,font = 1, command = sort_algorithm)
sort.place(x = 760 , y=30)
squar1 = Frame(win, width=1335, height=30, bg='#FAF0CA')
squar1.place(x=10,y = 98)


# complexity patition
frame3 = Frame(win, width=300 , height=80, bg='#FAF0CA') 
frame3.place(x=920,y = 10)

complexty = Label(frame3, text = "complexty is: ", bg='#FAF0CA' , font=1)
complexty.place(x=15, y=10)



win.mainloop()

