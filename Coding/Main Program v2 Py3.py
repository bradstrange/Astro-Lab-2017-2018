### Files Required Backup.txt Averages.txt Data.txt
from sense_hat import SenseHat #Importing main functions from SenseHat module
from picamera import PiCamera #Importing functions to use PiCamera
from time import sleep #Importing sleep function
from PIL import Image 
import datetime
import ephem
import datetime
import os # Imports OS function to edit files in the Operating System
import statistics
sense = SenseHat()      

def main(): ##Start of the main section of the code. Defined as a function
    if sense.get_humidity() == 0:
        sense.show_message("02", text_colour = (255,0,0)) # Error code #01
        main()
    elif sense.get_temperature() == 0:
        sense.show_message("03", text_colour = (255,0,0)) # Error code #02
        main()
    elif sense.get_pressure() == 0:
        sense.show_message("04", text_colour = (255,0,0)) # Error code #03
        main()
    elif sense.get_gyroscope() == 0:
        sense.show_message("05", text_colour = (255,0,0)) # Error code #04               
        main()
    elif sense.get_orientation() == 0:
        sense.show_message("06", text_colour = (255,0,0)) # Error code #05
        main()
    else:
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Calculates real time to display a time stamp of when data was recorded and written to file
        sense.show_message("01", text_colour = (0,255,0)) # Shows ' 01 ' in green to state that the program has run successfully 
        f = open("Data.txt","a") # File has already been created, opens the file to edit with new data
        temp = sense.get_temperature() # Retrieves data for temperature
        humidity = sense.get_humidity() # ' ' humidity
        pressure = sense.get_pressure() # ' ' pressure           
        orientation_deg = sense.get_orientation_degrees() # ' ' orientation in degrees
        orientation = sense.get_orientation() # ' ' orientation in raw format
        gyroscope = sense.get_gyroscope() # ' ' gyroscope
        compassraw = sense.get_compass_raw() # ' ' compass in raw format
        accelerometer = sense.get_accelerometer() # ' ' accelerometer
        pressure = pressure * 100
        print(time_stamp) # Prints time stamp
        print("Temperature: %s C" % temp) # Prints temperature in Celcius
        print("Humidity: %s %%rH" % humidity) # '' humidity in percentage
        print("Pressure: %s Pascals" % pressure) # '' pressure in millibars
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_deg)) # '' orientation in degrees
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation)) # '' orientation in raw format
        print("x: {x}, y: {y}, z: {z}".format(**compassraw)) # '' compass in raw format
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyroscope)) # '' gyroscope
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**accelerometer)) # '' accelerometer
                    
        camera = PiCamera() # Enables camera
        sleep(1) # pauses for 1 second
        camera.capture("Temp.jpg") # Captures picture
        camera.close() # Closes camera
        imag = Image.open("Temp.jpg") # Opens the image that was just taken
        imag = imag.convert ("RGB") # Converts the colour of the image into RGB
        X,Y = 0,0 # Defines X,Y as 0,0
        pixelRGB = imag.getpixel((X,Y)) # Defines pixelRGB as the values for the RGB of the image
        R,G,B = pixelRGB # Defines R G B as the individual Red, Green and Blue values
        LuminanceA = (0.2126*R) + (0.7152*G) + (0.0722*B) # Calculates the Lumens of the image by multiplying R G and B and totalling them
        print("Lumens: ", LuminanceA) # Prints lumens of surroundings
        os.remove("/home/pi/Documents/Temp.jpg")# Removes the file so it can be created again to measure Lumens

        f.write("Time Stamp:" + time_stamp + "\n") # This line and the following 9 lines write the data printed above to a file called 'Data.txt'
        f.write("Te: %s C" % temp + "\n") 
        f.write("Hu: %s %%rH" % humidity + "\n")
        f.write("Pr: %s Pascals" % pressure + "\n")
        f.write("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_deg) + "\n")
        f.write("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation) + "\n")
        f.write("x: {x}, y: {y}, z: {z}".format(**compassraw) + "\n")
        f.write("p: {pitch}, r: {roll}, y: {yaw}".format(**gyroscope) + "\n")
        f.write("p: {pitch}, r: {roll}, y: {yaw}".format(**accelerometer) + "\n")
        f.write("Lumens: " + str(LuminanceA) + "\n")
        f.write("\n") # Creates a new line in the file
        f.close() # Closes the file

        f = open("Backup.txt","a")
        f.write("Time Stamp:" + time_stamp + "\n") # This line and the following 9 lines write the data printed above to a file called 'Backup.txt' In case the original file gets corrupted 
        f.write("Te: %s C" % temp + "\n") 
        f.write("Hu: %s %%rH" % humidity + "\n")
        f.write("Pr: %s Pascals" % pressure + "\n")
        f.write("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_deg) + "\n")
        f.write("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation) + "\n")
        f.write("x: {x}, y: {y}, z: {z}".format(**compassraw) + "\n")
        f.write("p: {pitch}, r: {roll}, y: {yaw}".format(**gyroscope) + "\n")
        f.write("p: {pitch}, r: {roll}, y: {yaw}".format(**accelerometer) + "\n")
        f.write("Lumens: " + str(LuminanceA) + "\n")
        f.write("\n") # Creates a new line in the file
        f.close() # Closes the file

def averages():
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Calculates real time to display a time stamp of when data was recorded and written to file
    f = open("Averages.txt","a") # Opens the file Averages
    temp1 = sense.get_temperature() # Retrieves data for temperature
    temp2 = sense.get_temperature()
    temp3 = sense.get_temperature()
    hum1 = sense.get_humidity() # ' ' humidity
    hum2 = sense.get_humidity()
    hum3 = sense.get_humidity()
    pres1 = sense.get_pressure() # ' ' pressure
    pres2 = sense.get_pressure()
    pres3 = sense.get_pressure()
    f.write("Time Stamp: " + time_stamp + "\n")

    tempavg = [temp1, temp2, temp3] # Assigns a list to tempavg
    avg1 = statistics.mean(tempavg) # Takes an average
    print("Temp Avg:", avg1) # Prints the average
    f.write("Temp Avg: ") # Writes the average to file
    f.write(str(avg1))
    f.write("\n")

    humavg = [hum1, hum2, hum3] # '' to humavg
    avg2 = statistics.mean(humavg) # ''
    print("Hum Avg:", avg2) # ''
    f.write("Hum Avg: ") # ''
    f.write(str(avg2))
    f.write("\n")

    presavg = [pres1, pres2, pres3] # '' to presavg
    avg3 = statistics.mean(presavg) # ''
    avg3 = avg3 * 100
    print("Pres Avg:", avg3) # ''
    f.write("Pres Avg: ")
    f.write(str(avg3))
    f.write("\n")
    f.write("\n") # Make a break in the text

    
    
    f.close() # Closes the file

def isstrack(): ## Start of the program that tracks the ISS. Defined as a function
    
    name = "ISS (ZARYA)"; # Defines name as 'ISS (ZARYA)
    line1 = "1 25544U 98067A   18023.97745102  .00001826  00000-0  34732-4 0  9999"; # This line and the following line are used to calculate the longitude and latitude of the ISS using Two Line
    line2 = "2 25544  51.6422  17.6213 0003528  42.9600 346.0850 15.54203475 96097";
    iss = ephem.readtle(name,line1,line2) # Uses the function readtle to define iss as the two line data and the name of the object being tracked in orbit
    iss.compute() # Calculates the longitude and latitude
    f = open("Testfile.txt","a") # Opens the file 'Testfile.txt'
    print("Lat: %s - Long: %s" %(iss.sublat, iss.sublong) + "\n") # Prints the longitude and latitude of the ISS 
    f.write("Lat: %s - Long: %s" %(iss.sublat, iss.sublong) + "\n") # Writes to file the longitude and the latitude of the ISS
    f.write("\n") 
    f.close() # File is closed

###Main Program###
while(1): # Runs the program indefinitely
    main() # first section of the program
    averages() # Second section of the program
    isstrack() # Third section of the program

        
