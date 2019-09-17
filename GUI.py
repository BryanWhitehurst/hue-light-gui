from tkinter import *
import requests, random, json, time

window = Tk()
 
window.title("Light Colors")
window.geometry('1000x600')
 
lbl = Label(window, text="Room N222 Light Operator V1", font=("Times New Roman", 20))
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="     ", font=("Times New Roman", 20))
lbl2.grid(column=1, row=0)

lbl3 = Label(window, text="Set Custom Hue (0-65535)", font=("Times New Roman", 20))
lbl3.grid(column=2, row=0)

lbl4 = Label(window, text=" ", font=("Times New Roman", 20))
lbl4.grid(column=0, row=7)

lbl3 = Label(window, text="Set Custom Brightness (1-254)", font=("Times New Roman", 20))
lbl3.grid(column=0, row=7)

lbl3 = Label(window, text="Set Custom Saturation (0-254)", font=("Times New Roman", 20))
lbl3.grid(column=2, row=7)

def toggleOn():
    data = json.dumps({"on": bool(1)})

    requests.put('http://130.160.155.109/api/WloqjO9v8WOZz8WV8LrAo7Wv55yKK7yHXzTCe-tI/groups/1/action', data=data)

def toggleOff():
    data = json.dumps({"on": bool(0)})

    requests.put('http://130.160.155.109/api/WloqjO9v8WOZz8WV8LrAo7Wv55yKK7yHXzTCe-tI/groups/1/action', data=data)

def colorloop():
    data = json.dumps({"effect": "colorloop"})

    requests.put('http://130.160.155.109/api/WloqjO9v8WOZz8WV8LrAo7Wv55yKK7yHXzTCe-tI/groups/1/action', data=data)
    

def none():
    data = json.dumps({"effect": "none"})

    requests.put('http://130.160.155.109/api/WloqjO9v8WOZz8WV8LrAo7Wv55yKK7yHXzTCe-tI/groups/1/action', data=data)

def setColor():
    num = colorNum.get()
    
    data = json.dumps({"hue": int(num)})

    requests.put('http://130.160.155.109/api/WloqjO9v8WOZz8WV8LrAo7Wv55yKK7yHXzTCe-tI/lights/1/state', data=data)

def setColor2():
    num = colorNum2.get()
    
    data = json.dumps({"hue": int(num)})

    requests.put('http://130.160.155.109/api/WloqjO9v8WOZz8WV8LrAo7Wv55yKK7yHXzTCe-tI/lights/2/state', data=data)

def setColor3():
    num = colorNum3.get()
    
    data = json.dumps({"hue": int(num)})

    requests.put('http://130.160.155.109/api/WloqjO9v8WOZz8WV8LrAo7Wv55yKK7yHXzTCe-tI/lights/3/state', data=data)

def setColor4():
    num = colorNum4.get()
    
    data = json.dumps({"hue": int(num)})

    requests.put('http://130.160.155.109/api/WloqjO9v8WOZz8WV8LrAo7Wv55yKK7yHXzTCe-tI/lights/4/state', data=data)

def setBri():
    num = briNum.get()
    
    data = json.dumps({"bri": int(num)})

    requests.put('http://130.160.155.109/api/WloqjO9v8WOZz8WV8LrAo7Wv55yKK7yHXzTCe-tI/groups/1/action', data=data)

def setSat():
    num = satNum.get()
    
    data = json.dumps({"sat": int(num)})

    requests.put('http://130.160.155.109/api/WloqjO9v8WOZz8WV8LrAo7Wv55yKK7yHXzTCe-tI/groups/1/action', data=data)

def reset():
    data = json.dumps({"hue": 8418})
    data2 = json.dumps({"sat": 140})

    requests.put('http://130.160.155.109/api/WloqjO9v8WOZz8WV8LrAo7Wv55yKK7yHXzTCe-tI/groups/1/action', data=data)
    requests.put('http://130.160.155.109/api/WloqjO9v8WOZz8WV8LrAo7Wv55yKK7yHXzTCe-tI/groups/1/action', data=data2)

btn = Button(window, text="Colorloop", command=colorloop)
btn.grid(column=0, row=4)

btn2 = Button(window, text = "None", command=none)
btn2.grid(column = 0, row = 5)


btn4 = Button(window, text = "Set Light 1", command = setColor)
btn4.grid(column = 3, row = 3)

btn5 = Button(window, text = "Set Light 2", command = setColor2)
btn5.grid(column = 3, row = 4)

btn6 = Button(window, text = "Set Light 3", command = setColor3)
btn6.grid(column = 3, row = 5)

btn7 = Button(window, text = "Set Light 4", command = setColor4)
btn7.grid(column = 3, row = 6)

btn8 = Button(window, text="Toggle on", command=toggleOn)
btn8.grid(column=0, row=2)

btn9 = Button(window, text="Toggle off", command=toggleOff)
btn9.grid(column=0, row=3)

btn10 = Button(window, text="Enter", command=setBri)
btn10.grid(column=1, row=8)

btn10 = Button(window, text="Enter", command=setSat)
btn10.grid(column=3, row=8)

btn11 = Button(window, text = "Reset", command = reset)
btn11.grid(column = 0, row = 6)

colorNum = Entry(window,width=25)
colorNum.grid(column = 2, row = 3)

colorNum2 = Entry(window,width=25)
colorNum2.grid(column = 2, row = 4)

colorNum3 = Entry(window,width=25)
colorNum3.grid(column = 2, row = 5)

colorNum4 = Entry(window,width=25)
colorNum4.grid(column = 2, row = 6)

briNum = Entry(window,width=25)
briNum.grid(column = 0, row = 8)

satNum = Entry(window,width=25)
satNum.grid(column = 2, row = 8)

window.mainloop()
