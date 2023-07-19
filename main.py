from keras.models import load_model
from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np
import PIL.Image, PIL.ImageTk
import time
root = Tk()
root.title('Mecanum ESP32 CAM')

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
#"http://192.168.1.35:81/stream"
camera = cv2.VideoCapture(0)

# Function to be executed when the button is clicked
def button_click():
    print("Button clicked!")

# Create a frame to hold the video and button
frame = Frame(root)
frame.pack()

# Create a label to display the video
label = Label(frame)
label.grid(row=0, column=0, columnspan=3)

# Function Button
def move_forward():
    print("Tiến")

def move_backward():
    print("Lùi")

def move_left():
    print("Trái")

def move_right():
    print("Phải")

def stop():
    print("Dừng")
#TO DO
###########
label_text_var = StringVar()
label_text_var.set("Label above buttons")
label_above_buttons = Label(frame, textvariable=label_text_var)
label_above_buttons.grid(row=1, column=0, columnspan=3)

btn_forward = Button(frame, text="Tiến", command=move_forward)
btn_backward = Button(frame, text="Lùi", command=move_backward)
btn_left = Button(frame, text="Trái", command=move_left)
btn_right = Button(frame, text="Phải", command=move_right)
btn_stop = Button(frame, text="Dừng", command=stop)
btn_right1 = Button(frame, text="Phải", command=move_right)
###########
# Grid layout for the buttons

btn_forward.grid(row=2, column=1, pady=5)
btn_backward.grid(row=4, column=1, pady=5)
btn_left.grid(row=3, column=0, padx=5)
btn_right.grid(row=3, column=2, padx=5)
btn_stop.grid(row=3, column=1)
btn_right1.grid(row=3,column=3,padx=5)
def show_frame():
    _, frame_image = camera.read(0)

    # Resize the raw image into (224-height,224-width) pixels
    frame_image = cv2.resize(frame_image, (224, 224), interpolation=cv2.INTER_AREA)

    # Convert the frame image to PIL Image object
    pil_image = PIL.Image.fromarray(frame_image)

    # Make a copy of the original image for prediction
    image_copy = pil_image.copy()

    # Convert image to NumPy array
    image_array = np.asarray(image_copy, dtype=np.float32)

    # Reshape the image array
    image_array = image_array.reshape(1, 224, 224, 3)

    # Normalize the image array
    image_array = (image_array / 127.5) - 1

    # Predict the model
    prediction = model.predict(image_array)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Convert image back to PIL Image object
    pil_image = PIL.Image.fromarray(frame_image)

    # Convert image to Tkinter PhotoImage
    image_tk = PIL.ImageTk.PhotoImage(pil_image)

    # Update the label with the new image
    label.configure(image=image_tk)
    label.image = image_tk

    # Call this function again after 10 milliseconds
    label.after(10, show_frame)

# Call the show_frame function to start displaying the video
show_frame()

# Run the main event loop to display the GUI

root.mainloop()

