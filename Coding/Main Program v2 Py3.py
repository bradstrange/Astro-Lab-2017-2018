
from sense_hat import SenseHat
from picamera import PiCamera
from time import sleep
from PIL import Image
import ephem
from ephem import (Body, Planet, Moon, Jupiter, Saturn, PlanetMoon,
                    Date, Observer, readtle, readdb,
                    FixedBody, EllipticalBody, HyperbolicBody,
                    ParabolicBody, EarthSatellite,
                    constellation)
import datetime
import os
sense = SenseHat()      

def main():
    if sense.get_humidity() == 0:
        sense.show_message("02", text_colour = (255,0,0))
        main()
    elif sense.get_temperature() == 0:
        sense.show_message("03", text_colour = (255,0,0))
        main()
    elif sense.get_pressure() == 0:
        sense.show_message("04", text_colour = (255,0,0))
        main()
    elif sense.get_gyroscope() == 0:
        sense.show_message("05", text_colour = (255,0,0))                
        main()
    elif sense.get_compass_raw() == 0:
        sense.show_message("06", text_colour = (255,0,0))
        main()
    elif sense.get_orientation() == 0:
        sense.show_message("07", text_colour = (255,0,0))
        main()
    else:
        sense.show_message("01", text_colour = (0,255,0))
        f = open("Testfile.txt","a")
        temp = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()            
        orientation_deg = sense.get_orientation_degrees()
        orientation = sense.get_orientation()
        gyroscope = sense.get_gyroscope()
        compassraw = sense.get_compass_raw()
        accelerometer = sense.get_accelerometer()
        print("Temperature: %s C" % temp)
        print("Humidity: %s %%rH" % humidity)
        print("Pressure: %s Millibars" % pressure)
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_deg))
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
        print("x: {x}, y: {y}, z: {z}".format(**compassraw))
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyroscope))
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**accelerometer))
            
        camera = PiCamera()
        sleep(1)
        camera.capture("Temp.jpg")
        camera.close()
        imag = Image.open("Temp.jpg")
        imag = imag.convert ("RGB")
        X,Y = 0,0
        pixelRGB = imag.getpixel((X,Y))
        R,G,B = pixelRGB
        LuminanceA = (0.2126*R) + (0.7152*G) + (0.0722*B)
        print("Lumens: ", LuminanceA)
        os.remove("/home/pi/Documents/Temp.jpg")
            
        f.write("Te: %s C" % temp + "\n")
        f.write("Hu: %s %%rH" % humidity + "\n")
        f.write("Pr: %s Millibars" % pressure + "\n")
        f.write("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_deg) + "\n")
        f.write("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation) + "\n")
        f.write("x: {x}, y: {y}, z: {z}".format(**compassraw) + "\n")
        f.write("p: {pitch}, r: {roll}, y: {yaw}".format(**gyroscope) + "\n")
        f.write("p: {pitch}, r: {roll}, y: {yaw}".format(**accelerometer) + "\n")
        f.write("Lumens: " + str(LuminanceA))
        f.write("\n")
        f.close()         

def isstrack():
    
    name = "ISS (ZARYA)";
    line1 = "1 25544U 98067A   17341.28840128  .00005157  00000-0  85153-4 0  9993";
    line2 = "2 25544  51.6425 255.3876 0003192 201.4122 301.9164 15.54105312 88678";
    iss = ephem.readtle(name,line1,line2)
    iss.compute()
    f = open("Testfile.txt","a")
    print("Lat: %s - Long: %s" %(iss.sublat, iss.sublong) + "\n")
    f.write("Lat: %s - Long: %s" %(iss.sublat, iss.sublong) + "\n")
    f.write("\n")
    f.close()

###Main Program###
while(1):
    main()
    isstrack()

        
