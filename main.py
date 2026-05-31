
#--------------IMPORTING--------------#
from tkinter import *
import sys
import os
from PIL import Image, ImageTk, ImageSequence #for adding the animated gif
import math # for rounding off the minutes after dividing seconds by 60

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


#---------------CONSTANTS-----------#
WHITE="#FFFFFF"
LIGHT_BLUE="#7eb2dd"
BLUE="#1E88E5"
GREEN="#66BB6A"
PURPLE="#AB47BC"
VERY_LIGHT_BLUE="#E3F2FD"

FONT_NAME= "Courier"
WORK_MIN=25
SHORT_BREAK_MIN=5
LONG_BREAK_MIN=20
CYCLES=0
WORK_HEADING="Deep Work Mode 🔒"
SHORT_BREAK_HEADING="Break Time! 🌿"
LONG_BREAK_HEADING="Big Recharge Time 🔋"
TIMER_EVENT=None #To store ID of the scheduled countdown job created by root.after()
TIMER_RUNNING=False
GIF_EVENT=None #Store animation event ID

#---------------TIMER RESET-------------#
def reset_timer():
    global CYCLES,TIMER_EVENT,TIMER_RUNNING
    if TIMER_EVENT is not None:
        root.after_cancel(TIMER_EVENT) # Pauses the event
        TIMER_EVENT=None#Reset to no timers running
    TIMER_RUNNING=False
    CYCLES = 0
    time_display["text"]="00:00"
    timer_label["text"]="POMODORO TIMER"
    tick["text"]=""

    canvas.delete("all")
    load_gif(resource_path(("resized_peek_bear_300_proportional.gif")))

#------------TIMER MECHANISM---------#
def start_timer():
    global CYCLES,TIMER_EVENT,TIMER_RUNNING
    if TIMER_RUNNING:
        return #Prevent starting multiple timers
    TIMER_RUNNING=True

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    CYCLES+=1
    if CYCLES%8==0:  #At cycles 8,16 etc take the 20 min break(after one pomodoro cycle)
        canvas.delete("all")
        load_gif(resource_path(("resized_cheer_bear_300_proportional.gif")))
        count_down(long_break_sec)
        timer_label["text"]=LONG_BREAK_HEADING
        work_sessions = CYCLES // 2
        tick["text"] = "✔" * work_sessions
    elif CYCLES%2==0:  # AT Cycle numbers 2,4,6,etc take a short break
        canvas.delete("all")
        load_gif(resource_path(("resized_fan_bear_300_proportional.gif")))
        count_down(short_break_sec)
        timer_label["text"]=SHORT_BREAK_HEADING
        work_sessions = CYCLES // 2
        tick["text"] = "✔" * work_sessions
    else:
        canvas.delete("all")
        load_gif(resource_path(("resized_pomodoro_timer_300_proportional.gif")))
        count_down(work_sec)
        timer_label["text"]=WORK_HEADING


#------------COUNTDOWN MECHANISM-----------#
def count_down(count):
    global TIMER_EVENT,TIMER_RUNNING
    if count>0:
        minutes=math.floor(count/60)
        seconds=count%60
        if minutes<10:
            minutes="0"+str(minutes)
        if seconds<10:
            seconds="0"+str(seconds)
        time_display["text"]=f"{minutes}:{seconds}"
        TIMER_EVENT=root.after(1000,count_down,count-1)  #count-1 is a *arg passed to count_down
    else:
        TIMER_RUNNING=False
        start_timer()

#-------------UI SETUP---------------#

root=Tk()
root.title("Pomodoro Timer")
root.geometry("500x500")
root.configure(background=LIGHT_BLUE)
root.config(pady=20,padx=20)
#setting up canvas for gif
canvas=Canvas(width=300,height=243,background=LIGHT_BLUE,highlightthickness=0)
canvas.grid(row=1,column=1)


#loading the gif
def load_gif(gif_string):
    global GIF_EVENT
    if GIF_EVENT is not None:#Some gif is still running
        root.after_cancel(GIF_EVENT)#cancel it
        GIF_EVENT=None
    gif=Image.open(gif_string)

    #extract frames
    frames=[ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]
    canvas.frames=frames #Keeps GIF frames alive, otherwise sometimes images can disappear
    canvas.delete("all")

    #put first frame on canvas
    img_id=canvas.create_image(150,121,image=frames[0])  #position it in the centre of the canvas

    #Animation loop
    def animate_gif_working(index=0):
        global GIF_EVENT
        frame=frames[index]
        canvas.itemconfig(img_id,image=frame)
        GIF_EVENT=root.after(100,animate_gif_working,(index+1)%len(frames))  #100ms per frame

    animate_gif_working()

load_gif(resource_path("resized_peek_bear_300_proportional.gif"))
#adding the text
time_display=Label(text="00:00",bg=LIGHT_BLUE,fg=WHITE,font=(FONT_NAME,35,"bold"))
time_display.grid(row=2,column=1)

#adding the timer label
timer_label=Label(text="POMODORO TIMER",bg=LIGHT_BLUE,fg=WHITE,font=("Courier New",30,"bold"),wraplength=300)
timer_label.grid(row=0,column=1)


#adding the tick mark to represent number of work sessions( 2 cycles of timer)

tick=Label(text="",bg=LIGHT_BLUE,fg=WHITE,font=(FONT_NAME,15,"bold"))
tick.grid(row=3,column=1)

#buttons
start_button=Button(text="START",fg=LIGHT_BLUE,bg=WHITE,font=(FONT_NAME,15,"bold"),command=start_timer)
start_button.grid(row=3,column=0)
reset_button=Button(text="RESET",fg=LIGHT_BLUE,bg=WHITE,font=(FONT_NAME,15,"bold"),command=reset_timer)
reset_button.grid(row=3,column=2)





root.mainloop()