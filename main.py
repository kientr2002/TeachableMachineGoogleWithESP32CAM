from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import paho.mqtt.client as mqtt
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
import time

MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "internK"
MQTT_PASSWORD = ""
MQTT_TOPIC_PUB = MQTT_USERNAME + "/feeds/V1"
MQTT_TOPIC_SUB = MQTT_USERNAME + "/feeds/V2"
default_img = Image.open("assets/1.jpg")

root = tkinter.Tk()
root.title("Robot app")
# root.geometry("600x600+150+150")

dongco_label = tkinter.Label(root, text="Dieu khien dong co")
dongco_label.grid(row=0, column=0)
cam_label = tkinter.Label(root, text="Dieu khien cam")
cam_label.grid(row=0, column=1)
manhinhchinh_label = tkinter.Label(root, text="Man hinh chinh")
manhinhchinh_label.grid(row=0, column=2)

dongco = tkinter.Frame()
cam = tkinter.Frame()
manhinhchinh = tkinter.Frame()
dongco.grid(row=1, column=0)
cam.grid(row=1, column=1)
manhinhchinh.grid(row=1, column=2)

tien = tkinter.Button(dongco, text="Tien")
tien.grid(row=0, column=1)
lui = tkinter.Button(dongco, text="Lui")
lui.grid(row=2, column=1)
trai = tkinter.Button(dongco, text="Trai")
trai.grid(row=1, column=0)
phai = tkinter.Button(dongco, text="Phai")
phai.grid(row=1, column=2)

xoaylen = tkinter.Button(cam, text="Xoay len")
xoaylen.grid(row=0, column=1)
xoayxuong = tkinter.Button(cam, text="Xoay xuong")
xoayxuong.grid(row=2, column=1)
xoaytrai = tkinter.Button(cam, text="Xoay trai")
xoaytrai.grid(row=1, column=0)
xoayphai = tkinter.Button(cam, text="Xoay phai")
xoayphai.grid(row=1, column=2)

chuphinh = tkinter.Button(manhinhchinh, text="Chup hinh")
chuphinh.grid(row=0, column=0)

cv2_img = default_img.resize((320, 240))
cv2_img = ImageTk.PhotoImage(cv2_img)
label_cv = tkinter.Label(manhinhchinh, image=cv2_img)
label_cv.grid(row=1, column=0)

get_image_running = 0
send_MQTT_running = 0
cam = cv2.VideoCapture()
ai_result = 0

# Load the model
model = load_model("keras_Model.h5", compile=False)
# Load the labels
class_names = open("labels.txt", "r").readlines()

def show_img():
    global cam, label_cv, ai_result
    ret, frame = cam.read()
    cv2_img = default_img
    if get_image_running:
        cv2_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2_img = Image.fromarray(cv2_img)
        width, height = cv2_img.size

        image = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
        ai_result = class_name[2:]

    cv2_img = cv2_img.resize((320, 240))
    cv2_img = ImageTk.PhotoImage(cv2_img)
    label_cv.config(image=cv2_img)
    label_cv.image = cv2_img #VERY IMPORTANT
    if get_image_running:
        root.after(50, show_img)

def show_cam():
    global get_image_running, cam
    get_image_running = 1
    cam = cv2.VideoCapture("http://192.168.1.56:81/stream")
    show_img()

button_show_cam = tkinter.Button(manhinhchinh, text="Start camera", command=show_cam)
button_show_cam.grid(row=0, column=1)

def stop_get_img():
    global get_image_running, cam
    get_image_running = 0
    cam.release()
    cv2.destroyAllWindows()

button_stop_get_img = tkinter.Button(manhinhchinh, text="Stop", command=stop_get_img)
button_stop_get_img.grid(row=0, column=2)

def mqtt_connected(client, userdata, flags, rc):
    print("Connected succesfully!!")
    client.subscribe(MQTT_TOPIC_SUB)

def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")

mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)

#Register mqtt events
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed

# mqttClient.loop_start()

# while True:
#     # time.sleep(5)
#     ai_result = ai_detector()
#     if not ai_result:
#         break
#     print(ai_result)
#     mqttClient.publish(MQTT_TOPIC_PUB, ai_result, 0, True)

def send_to_MQTT():
    print("123456798@#$%^& SEND TO MQTT @#$%^&123456798")
    global send_MQTT_running
    send_MQTT_running = 1
    MQTT_loop()

def MQTT_loop():
    global ai_result, send_MQTT_running
    mqttClient.publish(MQTT_TOPIC_PUB, ai_result, 0, True)
    print("SEND TO MQTT",ai_result)
    if send_MQTT_running:
        root.after(50, MQTT_loop)
    else:
        print("CLOSE SEND AI_RESULT")

def close_send_MQTT():
    global send_MQTT_running
    send_MQTT_running = 0

button_send_to_MQTT = tkinter.Button(manhinhchinh, text="Send to MQTT", command=send_to_MQTT)
button_send_to_MQTT.grid(row=0, column=3)

button_close_send_MQTT = tkinter.Button(manhinhchinh, text="Close send", command=close_send_MQTT)
button_close_send_MQTT.grid(row=0, column=4)

massage = tkinter.Label(manhinhchinh, text="Massage: ......")
massage.grid(row=1, column=1)

model_list = ["Mot", "Hai", "Ba"]
model_choose = tkinter.StringVar()
option_menu = ttk.OptionMenu(manhinhchinh, model_choose, "Not selected", *model_list)
option_menu.grid(row=1, column=1)

root.mainloop()
