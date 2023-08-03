from mqtt import *
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from rover import *
import time
from robocon import *

# Mô tả hàm này...
def KhuRung1():
  global Function, th_C3_B4ng_tin, demline, dieuKienThang, Info1
  pass

def on_mqtt_message_receive_callback__V1_(th_C3_B4ng_tin):
  global Function, demline, dieuKienThang, Info1
  if th_C3_B4ng_tin == 'Nothing':
    Info1 = 1

# Mô tả hàm này...
def DiThang():
  global Function, th_C3_B4ng_tin, demline, dieuKienThang, Info1
  rover.show_rgb_led(0, hex_to_rgb('#ffa500'))
  display.scroll(demline)
  follow_line_until(20, lambda: ((rover.read_line_sensors() == (1, 1, 1, 1))), 5000)
  demline = (demline if isinstance(demline, (int, float)) else 0) + 1
  display.scroll(demline)
  if demline == dieuKienThang:
    Function = 1
    demline = 0
    display.scroll(demline)
    rover.stop()
  else:
    follow_line_until(20, lambda: (False), 500)

# Mô tả hàm này...
def KhuRung2():
  global Function, th_C3_B4ng_tin, demline, dieuKienThang, Info1
  pass

# Mô tả hàm này...
def QuayTrai():
  global Function, th_C3_B4ng_tin, demline, dieuKienThang, Info1
  rover.show_rgb_led(0, hex_to_rgb('#00ff00'))
  rover.turn_left(15, 0.5)
  turn_until_condition(0, 30, lambda: (((rover.read_line_sensors() == (0, 1, 1, 0)) or (rover.read_line_sensors() == (0, 0, 1, 1)))), 2000)
  follow_line_until((-20), lambda: (False), 500)
  Function = 2

# Mô tả hàm này...
def NextState():
  global Function, th_C3_B4ng_tin, demline, dieuKienThang, Info1
  pass

# Mô tả hàm này...
def QuayPhai():
  global Function, th_C3_B4ng_tin, demline, dieuKienThang, Info1
  rover.turn_right(15, 0.5)
  turn_until_condition(30, 0, lambda: (((rover.read_line_sensors() == (0, 1, 1, 0)) or (rover.read_line_sensors() == (1, 1, 0, 0)))), 2000)
  follow_line_until(20, lambda: (False), 500)
  Function = 0
  dieuKienThang = 4

# Mô tả hàm này...
def DiLui():
  global Function, th_C3_B4ng_tin, demline, dieuKienThang, Info1
  rover.show_rgb_led(0, hex_to_rgb('#ffffff'))
  display.scroll(demline)
  follow_line_until((-20), lambda: ((rover.read_line_sensors() == (1, 1, 1, 1))), 5000)
  demline = (demline if isinstance(demline, (int, float)) else 0) + 1
  display.scroll(demline)
  if demline == dieuKienThang:
    Function = 3
    demline = 0
    display.scroll(demline)
    rover.stop()
  else:
    follow_line_until((-20), lambda: (False), 500)

# Mô tả hàm này...
def GapThaVat():
  global Function, th_C3_B4ng_tin, demline, dieuKienThang, Info1
  rover.show_rgb_led(0, hex_to_rgb('#0000ff'))

if True:
  mqtt.connect_wifi('AITT_3', '66668888')
  mqtt.connect_broker(server='mqtt.ohstem.vn', port=1883, username='InternK', password='')
  display.set_all('#0000ff')
  rover.servo_write(1, 0)
  rover.servo_write(2, 0)
  display.set_all('#000000')
  rover.show_rgb_led(0, hex_to_rgb('#000000'))
  rover.stop()
  wait_for(lambda: (button_a.is_pressed()))
  Function = 0
  demline = 0
  dieuKienThang = 4
  mqtt.on_receive_message('V1', on_mqtt_message_receive_callback__V1_)

while True:
  mqtt.check_message()
  say(th_C3_B4ng_tin)
  if Function == 0:
    DiThang()
  elif Function == 1:
    QuayPhai()
  elif Function == 2:
    dieuKienThang = 2
    DiLui()
  elif Function == 3:
    pass
  elif Function == 4:
    pass
  elif Function == 5:
    pass
  elif Function == 6:
    pass
  else:
    rover.stop()


QuayTrai()

rover.servo_write(1, 105)
rover.servo_write(2, 90)
Function = 7

GapThaVat()
follow_line_until(20, lambda: ((rover.ultrasonic.distance_cm() < 25)), 5000)
