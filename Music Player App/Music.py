from tkinter import *
import pygame
import os

from time import strftime

#define a Tkinter function Object
windows=Tk()
pygame.mixer.init()

n=0

#function to play and pause songs
def start_music():
    global n 
    n=n+1
    if(n==1):
        song_name=songs_box.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(0)
    elif(n%2==0):
        pygame.mixer.music.pause()
    elif(n%2)!=0:
        pygame.mixer.music.unpause()   
        

#desigining part-------
l1=Label(windows,text="Music Player",font="times 10")
l1.grid(row=5,column=1)

#button to play & pause
b2=Button(windows,text="Play/Pause",command=start_music)
b2.grid(row=10,column=5)

song_list=os.listdir()
songs_box=StringVar(windows)

songs_box.set("choose a music")

menu=OptionMenu(windows,songs_box,*song_list)
menu.grid(row=10,column=20)
windows.mainloop()
