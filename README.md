# sabertooth
Getting Things Going! Here is the info. for grabbing pysabertooth from https://github.com/MomsFriendlyRobotCompany/pysabertooth. There is a license and permission to use their software.
The MIT license states that their software can be distributed and used freely as long as you show off their MIT license on their software product. This should come in handy in case they get 
angry or upset b/c of the lack of license agreements being met.

...

# So, we seem to keep meeting this way!
I am basically using the BBGW, a Motor Bridge Cape, and a Sabertooth 2 x 12 V 1.00 to make some motors move. You can find the BBGW by searching online for BeagleBone Green Wireless. Seeed Studio 
produced it by their association w/ BeagleBoard.org. 

...

I am going to attempt to, w/ this ongoing project, use a Flask application to promote Python software that makes an HTML page command our motors. If you have any doubts, please pitch in and
let me know your take on this subject. 

...

# For starters!
Here is the starter software in Python from the link I shared above. I found this software on their GitHub.com page online. 

    from pysabertooth import Sabertooth

    saber = Sabertooth('/dev/tty.usbserial', baudrate=115200, address=128, timeout=0.1)

    # drive(number, speed)
    # number: 1-2
    # speed: -100 - 100

    saber.drive(1, 50)
    saber.drive(2, -75)
    saber.stop()

So...

I have changed the software to suit my needs and the set up I currently have on my BBGW to better acquiant myself w/ how this software runs.

    from pysabertooth import Sabertooth
    import time

    saber = Sabertooth("/dev/ttyO2", baudrate=9600, address=128, timeout=0.1)
    
    saber.drive(1, 85)
    saber.drive(2, 85)
    saber.stop()
    time.sleep(15)

    saber.drive(1, -60)
    saber.drive(2, -60)
    time.sleep(5)

    saber.stop()
    saber.close()    

# This software!
From above, the software uses the library pysabertooth. I then imported time to use time.sleep to keep my motors turning for a period of time. The fourth line, that was changed due to reasons on 
the Linux board, the BBGW, is done to suit the UART capabilities of the board at /dev/ttyO2 for UART2 but TXD only. I slowed the baudrate down to set it as a packetized serial connection from the Sabertooth
2 x 12. The address, if you read over the packetized serial section of the Sabertooth 2 x 12 documentation, states that the address at 128 w/ switches one and two up can be used w/ that
specific baudrate.

...

DimensionEngineering.com is where you can purchase one of these boards w/ the Atmel AVR chip and caps. You, on this board, will get two DC motor outputs, four inputs (two of which are 5v and GND),
 and a switch that allows you to manage the chip addresses for different uses, i.e. PWM, UART, ADC, and etc...

# Now...

    On your BBGW w/ Motor Bridge Cape attached, utilize the P9 header. 
    Use your UART2 pins, P9_21 respectively, w/ leads attached
    to the S1 screw connector on the Sabertooth.

# Okay and Moving Forward!

    Once things are connnected:

    use this command: sudo config-pin P9.21 uart
    This will ensure that your board is set up for uart mode.

    Once you have tested your software w/ the hardware, we need to set up
    a .sh file and then a .service file to make sure config-pin is 
    working on boot. If wanted, you could start a service, a .service file, 
    for the software your write too.

    Here is it:

    Go to /usr/bin and create a .sh file w/ your favorite editor. The file 
    goes a little like this:

    #!/bin/bash

    sudo config-pin P9.21 uart

...

I just added some funny bunch of .html software to call it in the Flask application while making the motors still move. I found this .html software on
w3schools.com. I have been searching for more info. on where I found this idea but it is not showing up again. The left side of the web page, the 
navigation section, is useless right now. It does absolutely nothing.

...

Close this file by first saving it. Use this command to turn your file into an executable: sudo chmod 755 yourfile.sh

...

Now...we need to make a .service file and save it to /etc/systemd/system, i.e. like so:

    [Unit]
    Description=Starting a Config-Pin Utility on Boot

    [Service]
    ExecStart=/usr/bin/yourfile.sh

    [Install]
    WantedBy=multi-user.target

...

This should set us up for stardom. I mean that this will inevitably start to make things easier to start once the system boots. Excuse my funny language.

Seth

P.S. If you need anything, please do not hesitate to ask away. I will "try" to answer as soon as possible. Give it three days for service.
