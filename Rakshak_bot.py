# import every important module
from tkinter import filedialog
import os
import pyautogui
import webbrowser
import time
import tkinter as tk
import cv2 
import numpy as np

#my coordinates
#28.3496137,77.3330161

class Point(object):
	def val(self):
		return int(self.x),int(self.y)
	def __init__(self, x=0, y=0):
	    self.x = x
	    self.y = y

	def __add__(self, other):
	    return Point(self.x + other.x, self.y + other.y)

	def __eq__(self, other):
	    return self.x == other.x and self.y == other.y
    
    
def custom():
    print('Custom image mode')
    root.destroy()
    global loc 
    loc = 2
    
def get_map():
    global img_path , map_path
    s1 = e1.get()
    s2 = e2.get()
    url = "https://www.google.com/maps/@"+str(s1)+","+str(s2)+",16.75z"
    webbrowser.open(url,autoraise = True, new=1)
    time.sleep(10)
    img_path = '/home/hangman/Desktop/productathon/map.png'
    map_path = '/home/hangman/Desktop/productathon/orignal_map.png'
    pyautogui.screenshot(img_path)
    os.system("kill $(ps -x | grep firefox)")
    orig = cv2.imread(img_path,1)
    gray = cv2.imread(img_path,0)
    orig = orig[100:700,450:1200]
    gray = gray[100:700,450:1200]
    img = gray
    kernel = np.ones((5,5),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    kernel = np.ones((1,1),np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((3,3),np.uint8)
    img = cv2.dilate(img,kernel,iterations = 2)
    kernel = np.ones((1,1),np.uint8)
    img = cv2.erode(img,kernel,iterations = 1)
    ret,img = cv2.threshold(img,254,255,cv2.THRESH_BINARY)
#    cv2.imshow("img" , img)
    cv2.imwrite(img_path,img)
    cv2.imwrite(map_path,orig)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()    
#    temp.destroy()
    
    
def loaction():
    root.destroy()
    global loc
    loc = 1
    
def showimage():
    global img_path
    img_path = filedialog.askopenfilename(initialdir = os.getcwd , title = "Select image File" , filetypes = (("PNG file","*.png"),("JPG file","*.jpg"),("All files","*.")))
#    img = cv2.imread(img_path , 1)
#    cv2.imshow('img',img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
def plan_path():
    global img_path
    print(img_path)
    custom.destroy()
def solve_map():
    temp.destroy()
    global img_path
    print(img_path)
def BFS(s, e):

    global img, h, w

    found = False
    q = []
    v = [[0 for j in range(w)] for i in range(h)]
    parent = [[Point() for j in range(w)] for i in range(h)]

    q.append(s)
    v[s.y][s.x] = 1
    while len(q) > 0:
        p = q.pop(0)
        for d in dir4:
            cell = p + d
            if (cell.x >= 0 and cell.x < w and cell.y >= 0 and cell.y < h and v[cell.y][cell.x] == 0 and
                    (img[cell.y][cell.x][0] != 0 or img[cell.y][cell.x][1] != 0 or img[cell.y][cell.x][2] != 0)):
                q.append(cell)
                v[cell.y][cell.x] = v[p.y][p.x] + 1  # Later

                parent[cell.y][cell.x] = p
                if cell == e:
                    found = True
                    del q[:]
                    break

    path = []
    list_cord = []
    if found:
        p = e
        while p != s:
            path.append(p)
            p = parent[p.y][p.x]
        path.append(p)
        path.reverse()
        for i in range(len(path)):
            a,b = path[i].val()
            list_cord.append([a,b])
        for p in path:
            img[p.y][p.x] = [255, 0, 0]
        print("Path Found")
    
    else:
	    print("Path Not Found")
    return list_cord
    


def mouse_event(event, pX, pY, flags, param):

    global img, start, end, p

    if event == cv2.EVENT_LBUTTONUP:
        if p == 0:
            cv2.rectangle(img, (pX - rw, pY - rw),
                          (pX + rw, pY + rw), (0, 0, 255), -1)
            start = Point(pX, pY)
            print("start = ", start.x, start.y)
            p += 1
        elif p == 1:
            cv2.rectangle(img, (pX - rw, pY - rw),
                          (pX + rw, pY + rw), (0, 200, 50), -1)
            end = Point(pX, pY)
            print("end = ", end.x, end.y)
            p += 1 
#def disp():
#    global img
#    cv2.imshow("Image", img)
#    cv2.setMouseCallback('Image', mouse_event)
#    while True:
#        cv2.imshow("Image", img)
#        k = cv2.waitKey(1) & 0xFF
#        if k==ord('q'):
#            break
loc = 0
img_path = ''
map_path = ''
# create a tkinter window 
root = tk.Tk()               

# Open window having dimension 100x100 
root.geometry('250x200+120+120')  
  
# Create a Button 
btn1 = tk.Button(root, text = 'custom', bd = '5', 
                          command = custom,pady = 10)  
btn2 = tk.Button(root, text = 'google maps', bd = '5', 
                          command = loaction,pady=10)
btn3 = tk.Button(root, text = 'quit', bd = '5', 
                          command = root.destroy,pady = 10)    
  
# Set the position of button on the top of window.    
btn1.pack(side = 'left') 
btn2.pack(side = 'right')
btn3.pack(side = 'bottom')    
  
root.mainloop()
if loc == 1:
    
    temp = tk.Tk()
    tk.Label(temp,text="Latitude").grid(row=0)
    tk.Label(temp,text="Longitude").grid(row=1)
    e1 = tk.Entry(temp)
    e2 = tk.Entry(temp)
    
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    
    tk.Button(temp , text='GET_MAP', command=get_map).grid(row=3,column=0,sticky=tk.W,pady=4)
    tk.Button(temp , text='Quit', command=temp.destroy).grid(row=3,column=1,sticky=tk.W,pady=4)
    tk.Button(temp , text='Find_Path' , command=solve_map).grid(row=3,column=2,sticky=tk.W,pady=4)
    temp.mainloop()

if loc == 2:
    
    custom = tk.Tk()
    frame = tk.Frame()
    frame.pack(side = tk.BOTTOM , padx = 15,pady = 15)
    label = tk.Label(custom)
    label.pack()
    button = tk.Button(frame, text = "Browse image" , command = showimage)
    button.pack(side = tk.LEFT)
    button2 = tk.Button(frame, text = "Find Path" , command = plan_path)
    button2.pack(side = tk.LEFT , padx = 10)
    
    custom.mainloop()
# till this point map has been loaded in its best possible form of a maze
#print(img_path)
if len(img_path)!=0:
    
    rw = 2
    p = 0
    start = Point()
    end = Point()
    
    dir4 = [Point(0, -1), Point(0, 1), Point(1, 0), Point(-1, 0)]
    
    
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    _, img = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    h, w = img.shape[:2]
    
    print("Select start and end points : ")
    cv2.imshow("Image", img)
    cv2.setMouseCallback('Image', mouse_event)
    while p < 2:
        cv2.waitKey(1)
    cv2.imshow("Image", img)
    cord_list = BFS(start, end)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if(len(map_path) == 0):
    map_path = img_path
print(map_path)
org = cv2.imread(map_path,1)
i = 0
while(i < len(cord_list)):
    x, y = cord_list[i]
    org = cv2.circle(org,(x,y), 2, (0,0,255), -1)
    cv2.imshow('simulation' , org)
    cv2.waitKey(100)
    i+=5
cv2.waitKey(0)
cv2.destroyAllWindows()

    


