#!/usr/bin/env python3

version = 0.994

import sys, os, shelve, subprocess, time
import curses
#from time import sleep
from picamera import PiCamera
from picamera import Color 

os.system("clear")
os.system("setleds -D +num")

#resuls = subprocess.Popen(['fbset -s'], shell=True, stdout=subprocess.PIPE).communicate()[0]
#resuls2 = resuls.splitlines()
#resuls3 = resuls2[1].decode('ascii')
#resuls4 = resuls3.split(" ")
#resuls5 = resuls4[1].split('\"')
#resuls6 = resuls5[1].split("x")
#width = int(resuls6[0])
#height = int(resuls6[1])

resuls = subprocess.Popen(['vcgencmd get_lcd_info'], shell=True, stdout=subprocess.PIPE).communicate()[0]
resuls = resuls.splitlines()
resuls = resuls[0].decode('ascii')
resuls = resuls.split(" ")
width = int(resuls[0])
height = int(resuls[1])

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

#print(time.time())
#print(time.time()+3)
#time.sleep(10)

#diese Funktion blockiert, sie wartet bis ein Zeichen eingegeben worden ist...
def one_char():
    char=sys.stdin.read(1)
    return char

def exists(filename):
    try:
        f = open(filename)
        f.close()
        return 1
    except:
        return 0



## Konfiguration zur Laufzeit nicht änderbarer Paramter bzw. Vorbelegung##
camera = PiCamera(resolution=(width, height), sensor_mode=2)
camera.framerate = 15
camera.sharpness = 20 # -100 +100
camera.preview_alpha = 255
camera.preview_fullscreen = True # True False
camera.iso = 0 # 0(auto) 1600
camera.exposure_mode = "auto" # off auto night nightpreview backlight spotlight sports snow beach verylong fixedfps antishake fireworks
camera.awb_mode = "auto" # off auto sunlight cloudy shade tungsten fluorescent incandescent flash horizon
#camera.awb_gains = 4.0, 4.0 # 0.0 8.0
camera.meter_mode = "matrix" # average spot backlit matrix
camera.saturation = 30 # -100 +100
camera.video_stabilization = False # True False
camera.image_effect = "none" #none, negative, solarize, sketch, denoise,emboss, oilpaint, hatch, gpen, pastell, watercolor, film, blur, saturation, colorswap, washedout, posterise, colorpoint, cartoon, deinterlace1, deinterlace2
#camera.color_effects = 128, 128 #schwarz-weiss, Werte gehen von 0-255
camera.drc_strength = "low" # off low medium high
camera.image_denoise = True # True False
camera.video_denoise = True # True False
#camera.analog_gain = 1.0 # Fraction
#camera.digital_gain = 0.8 # Fraction
camera.annotate_background = Color("white")
camera.annotate_foreground = Color("black")
camera.annotate_text = "" # max 255 characters

if not os.path.exists("pictures"):
    print("erstelle Picture-Directory")
    os.system("mkdir pictures")
    time.sleep(3)

if not exists("tarpi.param.db"):
    print("erzeuge Datenbank")
    param = shelve.open("tarpi.param")
    param["camera.contrast"] = "36" # -100 +100
    param["camera.brightness"] = "50" # 0 100
    param["camera.annotate_text_size"] = "16" # 6 160
    param["camera.exposure_compensation"] = "0" # -25 +25
    param["camera.vflip"] = "0" # True False
    param["camera.hflip"] = "0" # True False
    param.close()


if exists("tarpi.param.db"):
    print("lade datenbank")
    param = shelve.open("tarpi.param")
    camera.contrast = int(param["camera.contrast"])
    camera.brightness = int(param["camera.brightness"])
    camera.vflip = int(param["camera.vflip"])
    camera.hflip = int(param["camera.hflip"])
    camera.exposure_compensation = int(param["camera.exposure_compensation"])
    camera.annotate_text_size = int(param["camera.annotate_text_size"])
    param.close()

textsize = camera.annotate_text_size
zoomstep = 5
x1 = 0
y1 = 0
xw = 100
yw = 100

count = 0

op = ''

camera.start_preview()
fadeout = int(time.time()) + 5
os.system("clear")

camera.annotate_background = Color('white')
camera.annotate_foreground = Color('black')
camera.annotate_text = '< TarPi ' + str(version) + ' >   screen: ' + str(width) + '*' + str(height) + ' '
time.sleep(3)
camera.annotate_text = ""

while True:
    os.system("clear")
    op = one_char()
    camera.annotate_text_size = textsize
    camera.annotate_background = Color('white')
    camera.annotate_foreground = Color('black')
    if ord(op) == 13:
        if not camera.annotate_text == "":
            camera.annotate_text = ""
            op = " "
        else:    
            camera.annotate_background = Color('blue')
            camera.annotate_foreground = Color('white')
            camera.annotate_text = "  Press 0 for Maintainance \n 1 = contrast -  7 = contrast + \n 3 = brightness -  9 = brightness + \n / = ev +  * = ev - \n + = zoom in  - = zoom out \n 5 = reset to default zoom \n 0 = reset to default picture values \n , = flip image "
            op = one_char()
        if op == "5":
            camera.annotate_text = ""
            count = count + 1
            file = "./pictures/capture" + str('{:04d}'.format(count)) + ".jpg"
            while exists(file):
                count = count + 100
                file = "./pictures/capture" + str('{:04d}'.format(count)) + ".jpg"
            camera.capture(file, format='jpeg', use_video_port=True, quality=100)
            camera.annotate_text = " Picture: " + file + " taken "
            op = " "
        if op == "+":
            if textsize < 160 - 4:
                textsize = textsize + 4
                camera.annotate_text_size = textsize
                camera.annotate_text = "  Press 0 for Maintainance \n 1 = contrast -  7 = contrast + \n 3 = brightness -  9 = brightness + \n / = ev +  * = ev - \n + = zoom in  - = zoom out \n 5 = reset to default zoom \n 0 = reset to default picture values \n , = flip image "
                time.sleep(1)
                camera.annotate_text = ""
                op = " "
        if op == "-":
            if textsize > 6 + 4:
                textsize = textsize - 4
                camera.annotate_text_size = textsize
                camera.annotate_text = "  Press 0 for Maintainance \n 1 = contrast -  7 = contrast + \n 3 = brightness -  9 = brightness + \n / = ev +  * = ev - \n + = zoom in  - = zoom out \n 5 = reset to default zoom \n 0 = reset to default picture values \n , = flip image "
                time.sleep(1)
                camera.annotate_text = ""
                op = " "
        if ord(op) == 13:
            camera.annotate_text = ""
            camera.annotate_text_size = textsize
            camera.annotate_background = Color('white')
            camera.annotate_foreground = Color('black')
        if op == "0":
            param = shelve.open("tarpi.param")
            param["camera.contrast"] = str(camera.contrast)
            param["camera.brightness"] = str(camera.brightness)
            param["camera.exposure_compensation"] = str(camera.exposure_compensation)
            param["camera.annotate_text_size"] = str(textsize)
            param["camera.vflip"] = camera.vflip
            param["camera.hflip"] = camera.hflip
            param.close()
            camera.annotate_text_size = textsize + 8
            camera.annotate_background = Color('red')
            camera.annotate_foreground = Color('white')
            camera.annotate_text = " 8 = Reboot \n 5 = System \n 2 = Shutdown "
            op = one_char()
            if op == "8":
                camera.annotate_text = " System Reboot "
                os.system("sudo reboot now -h")
            if op == "2":
                camera.annotate_text = " Shutdown "
                os.system("sudo shutdown now -h")
            if op == "5":
                camera.annotate_text = " System "
                os.system("SSH_TTY=local")
                curses.nocbreak()
                curses.echo()
                curses.endwin()
                break
            camera.annotate_background = Color('white')
            camera.annotate_foreground = Color('black')
            camera.annotate_text = ""
            camera.annotate_text_size = textsize
    if op == "+": 
        if xw >= 20:
            x1 = x1 + zoomstep
            y1 = y1 + zoomstep
            xw = xw - 2 * zoomstep
            yw = yw - 2 * zoomstep
        zoomfaktor = '{:02.2f}'.format(100/xw)
        camera.zoom =(x1/100, y1/100, xw/100, yw/100)
        camera.annotate_text = ' xShift: ' + str(x1) + '-' + str(x1+xw) + ' yShift: ' + str(y1) + '-' + str(y1+yw) + ' Zoomfaktor: ' + str(zoomfaktor) + ' '
 
    if op == "-":
#AAAAAAh, das Fenster kann ja nicht grösser als x1 bis 100 werden.
        if xw <= (100 - x1) - 2 * zoomstep:    #erst xw da es abhängig von x1 ist
            xw = xw + 2 * zoomstep
            if x1 > 0: 
                x1 = x1 - zoomstep
        else:
            if x1 > 0:
                x1 = x1 - zoomstep
                xw = 100 - x1   #eigentlich logisch da sich das Fenster ja nach links schiebt der Rand aber sonst mit schiebt
            if x1 > 0: 
                x1 = x1 - zoomstep
                xw = 100 - x1
        if yw <= (100 - y1) - 2 * zoomstep:    #erst yw da es abhängig von y1 ist
            yw = yw + 2 * zoomstep
            if y1 > 0: 
                y1 = y1 - zoomstep
        else:
            if y1 > 0:
                y1 = y1 - zoomstep
                yw = 100 - y1   #eigentlich logisch da sich das Fenster ja nach oben schiebt der Rand aber sonst mit schiebt
            if y1 > 0: 
                y1 = y1 - zoomstep
                yw = 100 - y1
        zoomfaktor = '{:02.2f}'.format(100/xw)
        camera.zoom =(x1/100, y1/100, xw/100, yw/100)
        camera.annotate_text = ' xShift: ' + str(x1) + '-' + str(x1+xw) + ' yShift: ' + str(y1) + '-' + str(y1+yw) + ' Zoomfaktor: ' + str(zoomfaktor) + ' '
 
    if op == "2":
        if y1 + yw <= 100 - zoomstep:
            y1 = y1 + zoomstep
        zoomfaktor = '{:02.2f}'.format(100/xw)
        camera.zoom =(x1/100, y1/100, xw/100, yw/100)
        camera.annotate_text = ' xShift: ' + str(x1) + '-' + str(x1+xw) + ' yShift: ' + str(y1) + '-' + str(y1+yw) + ' Zoomfaktor: ' + str(zoomfaktor) + ' '
            
    if op == "8":
        if y1 >= zoomstep:
            y1 = y1 -  zoomstep
        zoomfaktor = '{:02.2f}'.format(100/xw)
        camera.zoom =(x1/100, y1/100, xw/100, yw/100)
        camera.annotate_text = ' xShift: ' + str(x1) + '-' + str(x1+xw) + ' yShift: ' + str(y1) + '-' + str(y1+yw) + ' Zoomfaktor: ' + str(zoomfaktor) + ' '

    if op == "6":
        if x1 + xw <= 100 - zoomstep:
            x1 = x1 + zoomstep
        zoomfaktor = '{:02.2f}'.format(100/xw)
        camera.zoom =(x1/100, y1/100, xw/100, yw/100)
        camera.annotate_text = ' xShift: ' + str(x1) + '-' + str(x1+xw) + ' yShift: ' + str(y1) + '-' + str(y1+yw) + ' Zoomfaktor: ' + str(zoomfaktor) + ' '

    if op == "4":
        if x1 >= zoomstep:
            x1 = x1 -  zoomstep
        zoomfaktor = '{:02.2f}'.format(100/xw)
        camera.zoom =(x1/100, y1/100, xw/100, yw/100)
        camera.annotate_text = ' xShift: ' + str(x1) + '-' + str(x1+xw) + ' yShift: ' + str(y1) + '-' + str(y1+yw) + ' Zoomfaktor: ' + str(zoomfaktor) + ' '

    if op == "5":
        x1 = 0
        y1 = 0
        xw = 100
        yw = 100
        zoomfaktor = '{:02.2f}'.format(100/xw)
        camera.zoom =(x1/100, y1/100, xw/100, yw/100)
        camera.annotate_text = ' xShift: ' + str(x1) + '-' + str(x1+xw) + ' yShift: ' + str(y1) + '-' + str(y1+yw) + ' Zoomfaktor: ' + str(zoomfaktor) + ' '

    if op == "7":
        if camera.contrast < 50:
            camera.contrast = camera.contrast + 1 
        camera.annotate_text = ' contrast: ' + str(camera.contrast) + ' brightness: ' + str(camera.brightness) + ' ev: ' + str(camera.exposure_compensation) + ' '

    if op == "1":
        if camera.contrast > -50:
            camera.contrast = camera.contrast - 1
        camera.annotate_text = ' contrast: ' + str(camera.contrast) + ' brightness: ' + str(camera.brightness) + ' ev: ' + str(camera.exposure_compensation) + ' '

    if op == "9":
        if camera.brightness < 100:
            camera.brightness = camera.brightness + 1
        camera.annotate_text = ' contrast: ' + str(camera.contrast) + ' brightness: ' + str(camera.brightness) + ' ev: ' + str(camera.exposure_compensation) + ' '

    if op == "3":
        if camera.brightness > 0:
            camera.brightness = camera.brightness - 1
        camera.annotate_text = ' contrast: ' + str(camera.contrast) + ' brightness: ' + str(camera.brightness) + ' ev: ' + str(camera.exposure_compensation) + ' '

    if op == "*":
        if camera.exposure_compensation < 25:
            camera.exposure_compensation = camera.exposure_compensation + 1
        camera.annotate_text = ' contrast: ' + str(camera.contrast) + ' brightness: ' + str(camera.brightness) + ' ev: ' + str(camera.exposure_compensation) + ' '

    if op == "/":
        if camera.exposure_compensation > -25:
            camera.exposure_compensation = camera.exposure_compensation - 1
        camera.annotate_text = ' contrast: ' + str(camera.contrast) + ' brightness: ' + str(camera.brightness) + ' ev: ' + str(camera.exposure_compensation) + ' '

    if op == "0":
        param = shelve.open("tarpi.param")
        camera.contrast = int(param["camera.contrast"])
        camera.brightness = int(param["camera.brightness"])
        camera.exposure_compensation = int(param["camera.exposure_compensation"])
        textsize = int(param["camera.annotate_text_size"])
        param.close()
        camera.annotate_text = " Parameters saved "

    if op == ",":
        if camera.vflip:
            camera.vflip = False
            camera.hflip = False
        else:
            camera.vflip=True
            camera.hflip=True
curses.nocbreak()
curses.echo()
curses.endwin()




