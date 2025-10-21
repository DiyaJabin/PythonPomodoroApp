
#--------------IMPORTING--------------#
from tkinter import *
from PIL import Image, ImageTk, ImageSequence #for adding the animated gif
import math # for rounding off the minutes after dividing seconds by 60




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
SECONDS_IN_ONE_CYCLE=0
WORK_HEADING="Deep Work Mode 🔒"
SHORT_BREAK_HEADING="Break Time! 🌿"
LONG_BREAK_HEADING="Big Recharge Time 🔋"
TIMER_EVENT=NONE
#---------------TIMER RESET-------------#
def reset_timer():
    root.after_cancel(TIMER_EVENT) # Pauses the event
    time_display["text"]="00:00"
    timer_label["text"]="POMODORO TIMER"
    tick["text"]=""
    global CYCLES
    CYCLES=0
    canvas.delete("all")
    load_gif("resized_peek_bear_300_proportional.gif")

#------------TIMER MECHANISM---------#
def start_timer():
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    global CYCLES
    CYCLES+=1
    if CYCLES%8==0:  #At cycles 8,16 etc take the 20 min break(after one pomodoro cycle)
        canvas.delete("all")
        load_gif("resized_cheer_bear_300_proportional.gif")
        count_down(long_break_sec)
        timer_label["text"]=LONG_BREAK_HEADING
    elif CYCLES%2==0:  # AT Cycle numbers 2,4,6,etc take a short break
        canvas.delete("all")
        load_gif("resized_fan_bear_300_proportional.gif")
        count_down(short_break_sec)
        timer_label["text"]=SHORT_BREAK_HEADING
        work_sessions = CYCLES // 2
        tick["text"] = "✔" * work_sessions
    else:
        canvas.delete("all")
        load_gif("resized_pomodoro_timer_300_proportional.gif")
        count_down(work_sec)
        timer_label["text"]=WORK_HEADING








#------------COUNTDOWN MECHANISM-----------#
def count_down(count):
    global TIMER_EVENT
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
    gif=Image.open(gif_string)

    #extract frames
    frames=[ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]

    #put first frame on canvas
    img_id=canvas.create_image(150,121,image=frames[0])  #position it in the centre of the canvas

    #Animation loop
    def animate_gif_working(index=0):
        frame=frames[index]
        canvas.itemconfig(img_id,image=frame)
        root.after(100,animate_gif_working,(index+1)%len(frames))  #100ms per frame

    animate_gif_working()

load_gif("resized_peek_bear_300_proportional.gif")
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