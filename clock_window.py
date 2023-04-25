import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
import pygame
from pygame import mixer
from PIL import Image, ImageTk

class Clock:

    def __init__(self):
        self.main_window()

    def actual_time(self):
        """"Show a clock with actual time"""
        self.paused = False
        day = time.strftime("%d")
        month = time.strftime("%m")
        year = time.strftime("%Y")
        hours = time.strftime("%H")
        minutes = time.strftime("%M")
        seconds = time.strftime("%S")
        self.actual_clock_label.config(text=f"{day}/{month}/{year} {hours}:{minutes}:{seconds}",font=("Estrangelo Edessa",18),fg="#000",background="#fff")
        self.actual_clock_label.after(1000, self.actual_time)

    def main_window(self):
        """Main Window"""
        # Window Settings
        self.root = tk.Tk()
        self.root.geometry("700x400")
        self.root.config(bg="#fff")
        # icon_small = tk.PhotoImage(file="./icons/icon_small.png")
        # icon_large = tk.PhotoImage(file="./icons/icon_large.png")
        # self.root.iconphoto(False,icon_large,icon_small)
        self.root.iconbitmap(r"./icons/icon.ico")
        self.root.resizable(False,False)
        self.root.title("Sport Timer")
        # Frames
        self.buttons_frame = Frame(self.root,width=700,height=100,background="#fff")
        self.buttons_frame.place(x=0,y=300)

        self.clock_frame= Frame(self.root,width=550,height=300,background="#000")
        self.clock_frame.place(x=0,y=0)

        self.settings_frame = Frame(self.root,width=150,height=300,background="#0023FF")
        self.settings_frame.place(x=550,y=0)
        # Actual Clock
        self.actual_clock_label = Label(self.buttons_frame,text='') 
        self.actual_clock_label.place(x=470,y=35)
        self.actual_clock_label.after(1000,self.actual_time())
        # Button images 
        self.play_btn_img = PhotoImage(file="./icons/play.png")
        self.pause_btn_img = PhotoImage(file="./icons/pause.png")
        self.reset_btn_img = PhotoImage(file="./icons/reset.png")
        self.settings_btn_img = PhotoImage(file="./icons/settings.png")
        # Buttons
        self.play_button = Button(self.buttons_frame,image=self.play_btn_img,background="#fff",borderwidth=0,command=self.play,state=DISABLED)
        self.play_button.place(x=50,y=18)

        self.pause_button = Button(self.buttons_frame,image=self.pause_btn_img,background="#fff",borderwidth=0,command=self.pause,state=DISABLED)
        self.pause_button.place(x=200,y=18)

        # self.reset_button = Button(self.buttons_frame,image=self.reset_btn_img,background="#fff",borderwidth=0,command=self.reset,state=DISABLED)
        # self.reset_button.place(x=350,y=18)

        # self.settings_button = Button(self.buttons_frame,image=self.settings_btn_img,background="#fff",borderwidth=0,command=self.settings)
        # self.settings_button.place(x=500,y=18)
        # Clock
        self.clock_label = Label(self.clock_frame,text="00:00:00",background="#000",font=("Estrangelo Edessa",105),fg="#fff")
        self.clock_label.place(x=1,y=80)
        # Seconds Variable
        self.seconds = 0
        clock = time.strftime("%H:%M:%S",time.gmtime(self.seconds))
        self.clock_label.config(text=clock)
        self.alarm = 0
        # Variables for Spinboxes
        self.seconds_value = IntVar()
        self.minutes_value = IntVar()
        self.hours_value = IntVar()
        self.alarm_seconds_value = IntVar()
        # Spinboxes to configure time
        self.hours_spinbox = Spinbox(self.settings_frame,from_=0,to=59,font=("Helvetica",27),width=2,textvariable=self.hours_value)
        self.hours_spinbox.place(x=70,y=10)

        self.minutes_spinbox = Spinbox(self.settings_frame,from_=0,to=59,font=("Helvetica",27),width=2,textvariable=self.minutes_value)
        self.minutes_spinbox.place(x=70,y=60)

        self.seconds_spinbox = Spinbox(self.settings_frame,from_=0,to=59,font=("Helvetica",27),width=2,textvariable=self.seconds_value)
        self.seconds_spinbox.place(x=70,y=110)

        self.alarm_seconds_spinbox = Spinbox(self.settings_frame,from_=0,to=59,font=("Helvetica",27),width=2,textvariable=self.alarm_seconds_value)
        self.alarm_seconds_spinbox.place(x=70,y=160)
        # Labels for Spinboxes
        Label(self.settings_frame,text="HOURS",bg="#fff",font=("Helvetica",9,"bold"),fg="#fff",background="#0023FF").place(x=10,y=20)
        Label(self.settings_frame,text="MINUTES",bg="#fff",font=("Helvetica",9,"bold"),fg="#fff",background="#0023FF").place(x=5,y=70)
        Label(self.settings_frame,text="SECONDS",bg="#fff",font=("Helvetica",9,'bold'),fg="#fff",background="#0023FF").place(x=3,y=120)
        Label(self.settings_frame,text="SECONDS",bg="#fff",font=("Helvetica",9,"bold"),fg="#fff",background="#0023FF").place(x=3,y=120)
        Label(self.settings_frame,text="Alarm Every...\n Seconds",bg="#fff",font=("Helvetica",7,"bold"),justify=LEFT,fg="#fff",background="#0023FF").place(x=2,y=170)
        # Button to save changes of Time and Alarm
        self.save_button = ttk.Button(self.settings_frame,text="Save & Load changes",command=self.save)
        self.save_button.place(x=10,y=250)

        # Window Mainloop
        self.root.mainloop()
    
    def save(self):
        # Save time
        self.play_button.config(state=NORMAL)
        # self.reset_button.config(state=NORMAL)
        seconds  = self.seconds_value.get()
        minutes = self.minutes_value.get() * 60
        hours = self.hours_value.get() * 3600
        alarm = self.alarm_seconds_value.get()
        # Save time of clock and alarm sound
        self.clock = seconds + minutes + hours
        self.seconds = self.clock
        self.alarm = alarm
        # Set time on clock
        clock = time.strftime("%H:%M:%S",time.gmtime(self.seconds))
        self.clock_label.config(text=clock,bg="#000",fg="#fff")
        self.clock_frame.config(background="#000")

    def play(self):
        """Start or unpause clock and update it every second"""
        if not self.paused:
            self.paused = True
            self.play_button.config(state=DISABLED)
            self.pause_button.config(state=NORMAL)
            if self.seconds > 0:
                if self.alarm == 0:
                    pass
                # Play an alarm sound every second (Spinbox value. If is 0, no play)
                elif self.seconds % self.alarm == 0:
                    self.alarm_sound()
                clock = time.strftime("%H:%M:%S",time.gmtime(self.seconds))
                self.clock_label.config(text=clock)
                self.seconds-=1
                self.task = self.root.after(1000,self.play)
                if self.seconds <= 9:
                    self.clock_frame.config(background="#FFA22D")
                    self.clock_label.config(bg="#FFA22D",fg="#000")
            
            else:
                if self.seconds == 0:
                    self.alarm_sound_finish()
                self.clock_label.config(text="00:00:00")
                self.clock_frame.config(background="#FF0000")
                self.clock_label.config(bg="#FF0000",fg="#000")
                self.pause_button.config(state=DISABLED)
        else:
            self.paused = False

    def alarm_sound(self):
         pygame.mixer.init()
         sonido = pygame.mixer.Sound("alarm_sound.mp3")
         sonido.play()


    def alarm_sound_finish(self):
         pygame.mixer.init()
         sonido = pygame.mixer.Sound("alarm_sound_finish.mp3")
         sonido.play()

    def pause(self):
            """Pause clock"""
            self.root.after_cancel(self.task)
            self.paused = True
            self.play_button.config(state=NORMAL)
            self.pause_button.config(state=DISABLED)
    

    def reset(self):
        self.seconds = self.clock
        clock = time.strftime("%H:%M:%S",time.gmtime(self.seconds))
        self.clock_label.config(text=clock,bg="#000",fg="#fff")
        self.clock_frame.config(background="#000")
        


