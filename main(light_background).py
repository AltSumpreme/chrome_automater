import pyautogui as gui 
import keyboard as k
import time 



while True:
        im=gui.screenshot()
        screen=im.getpixel((214,189))

        x1=im.getpixel((512,227))
        x2=im.getpixel((534,207))
        x3=im.getpixel((554,207))
        x4=im.getpixel((570,237))
        x5=im.getpixel((447,236))
        x6=im.getpixel((580,247))
        x7=im.getpixel((448,211))
        x8=im.getpixel((460,211))
        x9=im.getpixel((480,211))
                
        if screen[0]==32:
                if x1[0]!=225 or x2[0]!=225 or x3[0]!=225 or x4[0]!=225 or x5[0]!=225 or x6[0]!=225
                        gui.press('space')
                        time.sleep(0.001)
                if x7[0]!=225 or x8[0]!=225 or x9[0]!=225:
                         gui.press('down')
                         time.sleep(0.001)
                        
                

        if k.is_pressed('k'):
                break
