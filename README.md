# sabertooth
Getting Things Going! Here is the info. for grabbing the install via pip from https://github.com/MomsFriendlyRobotCompany/pysabertooth. There is a license and permission to use their software.
The MIT license states that their software can be distributed and used freely as long as you show off their MIT license on their software product. This should come in handy in case they get 
angry or upset b/c of the lack of license agreements being met.

...

# So, we seem to keep meeting this way!
I am basically using the BBGW, a Motor Bridge Cape, and a Sabertooth 2 x 12 to make some motors move. You can find the BBGW by searching online for BeagleBone Green Wireless. Seeed Studio 
produced it by their association w/ BeagleBoard.org. 

...

I am going to attempt to, w/ this ongoing project, use a Flask application to promote Python software that makes an HTML page command our motors. If you have any doubts, please pitch in and
let me know your take on this subject. 

...

# For starters!
Here is the starter software in Python from the link I shared above w/ the command, via pip, to install pysabertooth. I found this software on their GitHub.com page online. 

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

    saber = Sabertooth("/dev/ttyO1", baudrate=9600, address=128, timeout=0.1)
    
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
From above, the software uses the library SaberTooth. I then imported time to use time.sleep to keep my motors turning for a period of time. The fourth line, that was changed due to reasons on 
the Linux board, the BBGW, is done to suit the UART capabilities of the board at /dev/ttyO1 for UART1. I slowed the baudrate down to set it as a packetized serial connection from the Sabertooth
2 x 12. The address, if you read over the packetized serial section of the Sabertooth 2 x 12 documentation, states that the address at 128 w/ switches one and two up can be used w/ that, 
specific baudrate.

I will show a photo later of this fact.

...

DimensionEngineering.com is where you can purchase one of these boards w/ the Atmel AVR chip and caps. The board, the Sabertooth 2 x 12 V 1.00, lets you regulate the onboard chip via inputs and 
outputs. You, on this board, will get two DC motor outputs, four inputs, and a switch that allows you to manage the chip addresses for different uses, i.e. PWM, UART, GPIO, and etc...

# Now...

    On your BBGW w/ Motor Bridge Cape attached, utilize the P9 header. 
    Use your UART1 pins, P9_24 and P9_26 respectively, w/ leads attached
    to the S1 and S2 screw connectors on the Sabertooth.
    
...

I talked some "smack" earlier about setting up a Flask application in Python to make an HTML page have the capabilities to let you control your motors via UART. 

...

I feel like what I stated is false as of now b/c I have only used PWM to set up the BBGW for testing purposes. All truths aside, take a break, pitch-in, and/or let us build something. 

I will get on this project tonight and make some strides.

Seth

P.S. If I get in trouble over the lack of the MIT license listed in my README.md, please let me know. Oh and UART will not work w/ the current configuartion of my set up. Please make a note.
