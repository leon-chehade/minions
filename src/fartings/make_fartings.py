
from msilib import sequence
import tkinter as tk
from playsound import playsound
import random
import glob
import tkinter as tk
from PIL import ImageTk, Image
import os

def fart():   
    noises = glob.glob("data/*.mp3")
    print(noises)
    for i in range(3):
        test = random.choice(noises)
        print(test)
        playsound(test)

def show(path):
    window = tk.Tk()    
    window.title('Listen to the Minions ...')
    img = ImageTk.PhotoImage(Image.open(path))
    tk.Button(text="FURZGERAEUSCHE", image = img, command=fart).pack(fill = "both", expand = "yes")
    window.mainloop()

if __name__ == '__main__': 
    current_dir = os.getcwd()
    image_path = os.path.join(current_dir, "images", "minions.png")
    print(image_path)
    show(image_path)

    

