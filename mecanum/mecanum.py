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
def r_E1_BA_BD_tr_C3_A1i():
  global _C4_90_E1_BA_BFm_line__C4_91en_5_v_E1_BA_A1ch, S_E1_BA_B5n_s_C3_A0ng_, _C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch
  display.show(Image("00000:00000:11100:00100:00100"))

# Mô tả hàm này...
def _C4_90i_th_E1_BA_B3ng_2_v_E1_BA_A1ch__C4_91en():
  global _C4_90_E1_BA_BFm_line__C4_91en_5_v_E1_BA_A1ch, S_E1_BA_B5n_s_C3_A0ng_, _C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch
  if S_E1_BA_B5n_s_C3_A0ng_ == 0:
    display.show(Image("00100:01110:00100:00100:00100"))
    time.sleep_ms(1000)
    S_E1_BA_B5n_s_C3_A0ng_ = 1
  else:
    display.scroll(_C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch)
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
      _C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch = (_C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch if isinstance(_C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch, (int, float)) else 0) + 1
      if _C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch == 2:
        display.set_all('#ff0000')
        driver.setSpeed(0,0)
        driver.setSpeed(1,0)
        driver.setSpeed(2,0)
        driver.setSpeed(3,0)
        wait_for(lambda: (button_a.is_pressed()))
        _C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch = 0
        S_E1_BA_B5n_s_C3_A0ng_ = 0
      else:
        driver.setSpeed(0,30)
        driver.setSpeed(1,30)
        driver.setSpeed(2,23)
        driver.setSpeed(3,23)
        time.sleep_ms(200)
    elif (mecanum.read_line_sensors() == (0, 1, 0, 1)) or (mecanum.read_line_sensors() == (1, 0, 1, 0)):
      _C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch = (_C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch if isinstance(_C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch, (int, float)) else 0) + 1
      if _C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch == 5:
        display.set_all('#ff0000')
        driver.setSpeed(0,0)
        driver.setSpeed(1,0)
        driver.setSpeed(2,0)
        driver.setSpeed(3,0)
        wait_for(lambda: (button_a.is_pressed()))
        _C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch = 0
        S_E1_BA_B5n_s_C3_A0ng_ = 0
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
  _C4_90_E1_BA_BFm_line__C4_91en_5_v_E1_BA_A1ch = 0
  _C4_90_E1_BA_BFm_line__C4_91en_2_v_E1_BA_A1ch = 0
  S_E1_BA_B5n_s_C3_A0ng_ = 0
  wait_for(lambda: (button_a.is_pressed()))

while True:
  _C4_90i_th_E1_BA_B3ng_2_v_E1_BA_A1ch__C4_91en()


driver.setSpeed(0,30)
driver.setSpeed(1,30)
driver.setSpeed(2,23)
driver.setSpeed(3,23)
driver.setSpeed(0,30)
driver.setSpeed(1,30)
driver.setSpeed(2,25)
driver.setSpeed(3,25)

driver.setSpeed(0,30)
driver.setSpeed(1,(-30))
driver.setSpeed(2,(-30))
driver.setSpeed(3,30)

'Lệch phải'

'Ngang phải'

'Lệch trái'

driver.setSpeed(0,30)
driver.setSpeed(1,30)
driver.setSpeed(2,30)
driver.setSpeed(3,30)

display.show(Image("01000:11111:01001:00001:00001"))
