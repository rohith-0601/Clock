from tkinter import *
from datetime import *
import time

#let's set screen
screen = Tk()
screen.title("Clock")
screen.geometry("630x430")
screen.maxsize(630,430)
screen.minsize(629,429)


#let's get backgrounds
afternoon_image = PhotoImage(file ="./afternoon.png")
evng_image = PhotoImage(file = "./evng.png")
mrng_image = PhotoImage(file = "./mrng.png")
night_image = PhotoImage(file = "./night.png")

#let's set screen background now
screen_bg = Canvas(screen,width=630,height = 430)
screen_bg.grid(row = 0,column = 0)
#creating time and date display text
bg_image = screen_bg.create_image(315,215,image = afternoon_image)
display_time = screen_bg.create_text(200,215,text = "",font = "Ariel 40 bold",fill = "#021526")
display_sec = screen_bg.create_text(300,223,text = "",font ="Ariel 15 bold",fill = "#021526")
display_details = screen_bg.create_text(210,250,text = "",font = "Ariel 15 bold",fill = "#021526")

#let's create time display
def timer():
    global bg_image
    now = datetime.now()
    hour = now.hour
    present_time = now.strftime("%I:%M %p")
    present_sec = now.strftime("%S")
    present_details = now.strftime("%A | %d %B %Y")

    screen_bg.itemconfig(display_time,text = present_time)
    screen_bg.itemconfig(display_sec,text = present_sec)
    screen_bg.itemconfig(display_details,text = present_details)

    if 6 <= hour < 12:
       screen_bg.itemconfig(bg_image,image = mrng_image)
       screen_bg.itemconfig(display_time, fill="white")
       screen_bg.itemconfig(display_sec, fill="white")
       screen_bg.itemconfig(display_details, fill="white")
       screen_bg.coords(display_time, 315, 215)
       screen_bg.coords(display_sec, 415, 223)
       screen_bg.coords(display_details, 320, 250)
    elif 12 <= hour < 17:
        screen_bg.itemconfig(bg_image,image = afternoon_image)
        screen_bg.itemconfig(display_time, fill="#021526")
        screen_bg.itemconfig(display_sec, fill="#021526")
        screen_bg.itemconfig(display_details, fill="#021526")
        screen_bg.coords(display_time, 200, 215)
        screen_bg.coords(display_sec, 300, 223)
        screen_bg.coords(display_details, 210, 250)
    elif 17 <= hour < 20:
        screen_bg.itemconfig(bg_image,image = evng_image)
        screen_bg.itemconfig(display_time, fill="white")
        screen_bg.itemconfig(display_sec, fill="white")
        screen_bg.itemconfig(display_details, fill="white")
        screen_bg.coords(display_time, 315, 215)
        screen_bg.coords(display_sec, 415, 223)
        screen_bg.coords(display_details, 320, 250)
    else:
        screen_bg.itemconfig(bg_image, image=night_image)
        screen_bg.itemconfig(display_time,fill = "white")
        screen_bg.itemconfig(display_sec, fill="white")
        screen_bg.itemconfig(display_details, fill="white")
        screen_bg.coords(display_time,315,215)
        screen_bg.coords(display_sec, 415, 223)
        screen_bg.coords(display_details,320,250)

    screen.after(1000,timer)

#running program
timer()
screen.mainloop()