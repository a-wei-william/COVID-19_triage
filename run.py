import PySimpleGUI as sg
import sys
import os
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image



BASE_HEIGHT=400

image_elem = sg.Image(filename="", size=(400,400), pad=((30,10),(30,10)))
output_elem = sg.Text("", size=(15,1), justification='centre', auto_size_text=False)
model = keras.models.load_model('./Model.h5')

def jpg_to_png(filename):
    img = Image.open(filename)
    hpercent = (BASE_HEIGHT/float(img.size[1]))
    wsize = int((float(img.size[0])*float(hpercent)))
    img = img.resize((wsize,BASE_HEIGHT), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

def open_file():
    path_to_file = sg.popup_get_file('Document to open')
    if path_to_file:
      print('You entered ', path_to_file)
    return path_to_file
    #else:
      #    raise SystemExit("Cancelling: no filename supplied")

if __name__ == "__main__":

    sg.theme('DarkAmber')

    # ------ Menu Definition ------ #
    menu_def = [ ['Image', 'Open']
               , ['Help', 'About...'],
               ]

    # All the stuff inside your window.
    layout = [  [sg.Menu(menu_def,)]
             ,  [image_elem]
             ,  [sg.Text("              Probability of Pneumonia: "), output_elem]
             #,  [sg.Output(size=(60, 20))]
             ]

    # Create the Window
    window = sg.Window('Triage optimizer', layout, size=(500,500))

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        if event in ('Open'):
            path_to_file = open_file()
            img = image.load_img(path_to_file, target_size=(150,150))
            img = image.img_to_array(img)
            img = np.expand_dims(img,axis=0)
            prediction = model.predict(img)
            prediction = prediction.flatten()[0]#
            probability = prediction*100
            probability = str(probability) + "%"
            image_elem.Update(data=jpg_to_png(path_to_file))
            output_elem.Update(probability)
        if event in ('About...'):
            sg.popup('blahblahblah',title='About',size=(200,200))

    window.close()
