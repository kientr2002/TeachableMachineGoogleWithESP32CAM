from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from yolobit import *
import machine
from i2c_motors_driver import DCMotor
import time
from mecanum import *

driver = DCMotor(machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000))

# Mô tả hàm này...
def R_E1_BA_BD_tr_C3_A1i():
  global Function, Ready, LineRotate, DemLine2
  if Ready == 0:
    display.show(Image("00000:01000:11111:01000:00000"))
    time.sleep_ms(1000)
    Ready = 1
  else:
    display.scroll(LineRotate)
    if mecanum.read_line_sensors() == (0, 1, 1, 0):
      LineRotate = (LineRotate if isinstance(LineRotate, (int, float)) else 0) + 1
      if LineRotate == 2:
        display.set_all('#ff0000')
        driver.setSpeed(0,0)
        driver.setSpeed(1,0)
        driver.setSpeed(2,0)
        driver.setSpeed(3,0)
        wait_for(lambda: (button_a.is_pressed()))
        LineRotate = 0
        Ready = 0
        Function = 2
      else:
        driver.setSpeed(0,(-30))
        driver.setSpeed(1,(-30))
        driver.setSpeed(2,30)
        driver.setSpeed(3,30)
        time.sleep_ms(200)
    else:
      driver.setSpeed(0,(-30))
      driver.setSpeed(1,(-30))
      driver.setSpeed(2,30)
      driver.setSpeed(3,30)

# Mô tả hàm này...
def C_C4_83n_ch_E1_BB_89nh_r_E1_BA_BD_tr_C3_A1i():
  global Function, Ready, LineRotate, DemLine2
  if mecanum.read_line_sensors() == (1, 1, 1, 1):
    driver.setSpeed(0,0)
    driver.setSpeed(1,0)
    driver.setSpeed(2,0)
    driver.setSpeed(3,0)
    wait_for(lambda: (button_a.is_pressed()))
    Function = 0
  else:
    driver.setSpeed(0,25)
    driver.setSpeed(1,25)
    driver.setSpeed(2,35)
    driver.setSpeed(3,35)

# Mô tả hàm này...
def _C4_90i_th_E1_BA_B3ng():
  global Function, Ready, LineRotate, DemLine2
  if Ready == 0:
    display.show(Image("00100:01110:00100:00100:00100"))
    time.sleep_ms(1000)
    Ready = 1
  else:
    display.scroll(DemLine2)
    if (mecanum.read_line_sensors() == (0, 0, 1, 0)) or (mecanum.read_line_sensors() == (0, 1, 1, 0)):
      driver.setSpeed(0,30)
      driver.setSpeed(1,30)
      driver.setSpeed(2,23)
      driver.setSpeed(3,23)
    elif mecanum.read_line_sensors() == (0, 1, 0, 0):
      driver.setSpeed(0,30)
      driver.setSpeed(1,30)
      driver.setSpeed(2,25)
      driver.setSpeed(3,25)
    elif mecanum.read_line_sensors() == (1, 0, 0, 0):
      driver.setSpeed(0,30)
      driver.setSpeed(1,30)
      driver.setSpeed(2,25)
      driver.setSpeed(3,25)
    elif (mecanum.read_line_sensors() == (1, 1, 0, 0)) or (mecanum.read_line_sensors() == (1, 1, 1, 0)):
      driver.setSpeed(0,30)
      driver.setSpeed(1,30)
      driver.setSpeed(2,30)
      driver.setSpeed(3,30)
    elif mecanum.read_line_sensors() == (0, 0, 0, 1):
      driver.setSpeed(0,30)
      driver.setSpeed(1,30)
      driver.setSpeed(2,23)
      driver.setSpeed(3,23)
    elif (mecanum.read_line_sensors() == (0, 0, 1, 1)) or (mecanum.read_line_sensors() == (0, 1, 1, 1)):
      driver.setSpeed(0,30)
      driver.setSpeed(1,30)
      driver.setSpeed(2,20)
      driver.setSpeed(3,20)
    elif (mecanum.read_line_sensors() == (1, 1, 1, 1)) or (mecanum.read_line_sensors() == (1, 0, 1, 1)) or (mecanum.read_line_sensors() == (1, 1, 0, 1)) or (mecanum.read_line_sensors() == (1, 1, 1, 0)) or (mecanum.read_line_sensors() == (0, 1, 1, 1)):
      DemLine2 = (DemLine2 if isinstance(DemLine2, (int, float)) else 0) + 1
      if DemLine2 == 2:
        display.set_all('#ff0000')
        driver.setSpeed(0,0)
        driver.setSpeed(1,0)
        driver.setSpeed(2,0)
        driver.setSpeed(3,0)
        wait_for(lambda: (button_a.is_pressed()))
        DemLine2 = 0
        Ready = 0
        Function = 1
      else:
        driver.setSpeed(0,30)
        driver.setSpeed(1,30)
        driver.setSpeed(2,23)
        driver.setSpeed(3,23)
        time.sleep_ms(200)
    elif (mecanum.read_line_sensors() == (0, 1, 0, 1)) or (mecanum.read_line_sensors() == (1, 0, 1, 0)):
      DemLine2 = (DemLine2 if isinstance(DemLine2, (int, float)) else 0) + 1
      if DemLine2 == 2:
        display.set_all('#ff0000')
        driver.setSpeed(0,0)
        driver.setSpeed(1,0)
        driver.setSpeed(2,0)
        driver.setSpeed(3,0)
        wait_for(lambda: (button_a.is_pressed()))
        DemLine2 = 0
        Ready = 0
        Function = 1
      else:
        driver.setSpeed(0,30)
        driver.setSpeed(1,30)
        driver.setSpeed(2,23)
        driver.setSpeed(3,23)
        time.sleep_ms(200)
    else:
      driver.setSpeed(0,0)
      driver.setSpeed(1,0)
      driver.setSpeed(2,0)
      driver.setSpeed(3,0)

if True:
  display.set_all('#000000')
  driver.setSpeed(0,0)
  driver.setSpeed(1,0)
  driver.setSpeed(2,0)
  driver.setSpeed(3,0)
  wait_for(lambda: (button_a.is_pressed()))
  DemLine2 = 0
  Ready = 0
  LineRotate = 0
  Function = 0

while True:
  if Function == 0:
    _C4_90i_th_E1_BA_B3ng()
  elif Function == 1:
    R_E1_BA_BD_tr_C3_A1i()
  else:
    C_C4_83n_ch_E1_BB_89nh_r_E1_BA_BD_tr_C3_A1i()
