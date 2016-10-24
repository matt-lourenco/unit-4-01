# Created on 24 oct 2016
# Created by: Matthew Lourenco
# this is a program that converts celsius to fahrenheit.

import ui

def celsius_to_fahrenheit(sent_celsius):
    fahrenheit = 1.8 * sent_celsius + 32
    view['reply_label'].text = str(sent_celsius) + ' degrees converted to fahrenheit is: ' + str(fahrenheit) + ' degrees.'

def calculate_touch_up_inside(sender):
    try:
        celsius = float(view['celsius_textfield'].text)
        celsius_to_fahrenheit(celsius)
    except:
        view['reply_label'].text = 'Please enter a real number.'

view = ui.load_view()
view.present('fullscreen')
