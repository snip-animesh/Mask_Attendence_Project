from pyfirmata import util, STRING_DATA
import pyfirmata

arduino = pyfirmata.Arduino("COM4")
rgbR = arduino.get_pin('d:2:o')
rgbG = arduino.get_pin('d:3:o')
rgbB = arduino.get_pin('d:4:o')

door_pin=arduino.get_pin('d:7:o')

def rgb(RGB):
    rgbR.write(RGB[0])
    rgbG.write(RGB[1])
    rgbB.write(RGB[2])


def door(state):
    door_pin.write(state)


def lcd(name, roll):
    arduino.send_sysex(STRING_DATA, util.str_to_two_byte_iter(name))
    arduino.send_sysex(STRING_DATA, util.str_to_two_byte_iter(roll))
