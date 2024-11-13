from tkinter import *
import ttkbootstrap as ttk
import pygame
import keyboard
import os

# Initialize window
root = Tk()
root.title("yasin.GHasemi1387py")
root.geometry("1000x200")
root.resizable(False, False)




def toggle_play_pause():
    if status.get() == "-Playing":
        status.set("-Paused")
        pygame.mixer.music.pause()
        playpausebtn.config(text="PLAY")
    else:
        if status.get() == "-Paused":
            status.set("-Playing")
            pygame.mixer.music.unpause()
            playpausebtn.config(text="PAUSE")
        else:
            track.set(playlist.get(ACTIVE))
            status.set("-Playing")
            pygame.mixer.music.load(playlist.get(ACTIVE))
            pygame.mixer.music.play()
            playpausebtn.config(text="PAUSE")






# Add this after creating the root window
root.tk.call('tk', 'windowingsystem')
if root.tk.call('tk', 'windowingsystem') == 'win32':
    root.tk.call('set', 'themename', 'dark')


# Initialize pygame
pygame.init()
pygame.mixer.init()

# Create StringVars
track = StringVar()
status = StringVar()

# Create frames
trackframe = LabelFrame(root, text="Song Track", font=("Blue Screen Personal Use", 15, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
trackframe.place(x=0, y=0, width=600, height=100)

songtrack = Label(trackframe, textvariable=track, width=20, font=("Blue Screen Personal Use", 24, "bold"), bg="grey", fg="gold")
songtrack.grid(row=0, column=0, padx=10, pady=5)

trackstatus = Label(trackframe, textvariable=status, font=("Blue Screen Personal Use", 24, "bold"), bg="grey", fg="gold")
trackstatus.grid(row=0, column=1, padx=10, pady=5)

buttonframe = LabelFrame(root, text="Control Panel", font=("Blue Screen Personal Use", 15, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
buttonframe.place(x=0, y=100, width=600, height=100)

songsframe = LabelFrame(root, text="Song Playlist", font=("Blue Screen Personal Use", 15, "bold"), bg="grey", fg="white", bd=5, relief=GROOVE)
songsframe.place(x=600, y=0, width=400, height=200)

# Create playlist
scrol_y = Scrollbar(songsframe, orient=VERTICAL)
playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE, 
                  font=("Blue Screen Personal Use", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)


def prev_song(event=None):
    current = playlist.curselection()
    prev_index = (current[0] - 1) % playlist.size()
    playlist.selection_clear(0, END)
    playlist.selection_set(prev_index)
    playlist.activate(prev_index)
    playsong()


def next_song(event=None):
    current = playlist.curselection()
    next_index = (current[0] + 1) % playlist.size()
    playlist.selection_clear(0, END)
    playlist.selection_set(next_index)
    playlist.activate(next_index)
    playsong()



# Functions
def playsong():
    selected_song = playlist.get(ACTIVE)
    track.set(selected_song)
    status.set("-Playing")
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()

#def InfoAndHelp():
#    root=Tk()
#    root.title("help, info")
#    root.geometry("400x400")
#    root.resizable(False, False)
#    l1 = Label(root, text="made by: yasin.GHasemi1387py")
#    l1.pack()
#    l2 = Label(root, text="github: https://github.com/yasin-Ghasemi1387py")
#    l2.pack()
#    l3 = Label(root, text="space to play or pause")
#    l3.pack()
#    l4 = Label(root, text="arrows to change the music")
#    l4.pack()
#    l5 = Label(root, text="control+h to dark mode")
#    l5.pack()
#    l6 = Label(root, text="was to lazy to add sound controls")
#    l6.pack()
#
#
#    pass

#YUP, was lazy again XD




def stopsong():
    status.set("-Stopped")
    pygame.mixer.music.stop()

def pausesong():
    status.set("-Paused")
    pygame.mixer.music.pause()

def unpausesong():
    status.set("-Playing")
    pygame.mixer.music.unpause()

def toggle_dark_mode():
    bg_color = "#1a1a1a"
    text_color = "#ffffff"
    accent_color = "#2d2d2d"
    highlight_color = "#00ff00"
    button_bg = "#333333"
    button_fg = "#00ff00"
    frame_bg = "#1f1f1f"
    
    if darkmodebtn['text'] == "DARK":
        # Switch to dark mode
        root.config(bg=bg_color)
        
        trackframe.config(bg=frame_bg, fg=text_color)
        
        buttonframe.config(bg=frame_bg, fg=text_color)
        
        songsframe.config(bg=frame_bg, fg=text_color)
        
        for widget in trackframe.winfo_children():
            if isinstance(widget, Label):
                widget.config(bg=frame_bg, fg=highlight_color)
        
        for widget in buttonframe.winfo_children():
            if isinstance(widget, Button):
                widget.config(bg=button_bg, fg=button_fg, activebackground=accent_color, activeforeground=highlight_color)
        
        playlist.config(
            bg=accent_color,
            fg=text_color,
            selectbackground=highlight_color,
            selectforeground=bg_color,
            activestyle='none'
        )
        darkmodebtn.config(text="LIGHT")
    else:
        


        # Switch back to light mode
        
        root.config(bg="SystemButtonFace")
        
        
        
        trackframe.config(bg="grey", fg="white")
        
        buttonframe.config(bg="grey", fg="white")
        
        songsframe.config(bg="grey", fg="white")
        
        for widget in trackframe.winfo_children():
            if isinstance(widget, Label):
                widget.config(bg="grey", fg="gold")
        
        for widget in buttonframe.winfo_children():
            if isinstance(widget, Button):
                widget.config(bg="gold", fg="navyblue", activebackground="SystemButtonFace", activeforeground="black")
        
        playlist.config(
            bg="silver",
            fg="navyblue",
            selectbackground="gold",
            selectforeground="black",
            activestyle='none'
        )
        darkmodebtn.config(text="DARK")



playpausebtn = Button(
    buttonframe,
    text="PLAY",
    command=toggle_play_pause,
    width=8,
    height=1,
    font=("Blue Screen Personal Use", 16, "bold"),
    fg="navyblue", 
    bg="gold")

playpausebtn.grid(row=0, column=0, padx=10, pady=5)


unpausebtn = Button(
    buttonframe, 
    text="UNPAUSE", 
    command=unpausesong, 
    width=10, 
    height=1, 
    font=("Blue Screen Personal Use", 16, "bold"), 
    fg="navyblue", 
    bg="gold")

unpausebtn.grid(row=0, column=2, padx=10, pady=5)





stopbtn = Button(
    buttonframe, 
    text="STOP", 
    command=stopsong, 
    width=6, 
    height=1, 
    font=("Blue Screen Personal Use", 16, "bold"), 
    fg="navyblue", 
    bg="gold")

stopbtn.grid(row=0, column=3, padx=10, pady=5)




darkmodebtn = Button(
    buttonframe, 
    text="DARK", 
    command=toggle_dark_mode, 
    width=6, 
    height=1, 
    font=("Blue Screen Personal Use", 16, "bold"), 
    fg="navyblue", 
    bg="gold")

darkmodebtn.grid(row=0, column=4, padx=10, pady=5)





# Load music files
os.chdir(r"E:\codes\python\really a music player\musics")
songtracks = os.listdir()
# Change the loop variable name from 'track' to 'song'
for song in songtracks:
    playlist.insert(END, song)









# Keyboard shortcuts
root.bind('<space>', lambda event: toggle_play_pause())
root.bind('<Control-d>', lambda event: toggle_dark_mode())
root.bind('<Escape>', lambda event: root.quit())
root.bind('<Left>', prev_song)
root.bind('<Right>', next_song)






root.mainloop()

