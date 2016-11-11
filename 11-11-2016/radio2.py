import sys
########################Modules Path Information################################
sys.path.append("/usr/lib/pymodules/ICBP_modules")
sys.path.append("/usr/lib/NRF24")
########################Modules Path Information################################
import Unpack2
import Timeout
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
import array


def radio_func(str = ""):
    rID = str
    print "Starting"
    print "Radio ID = " + rID
      
    GPIO.setmode (GPIO.BCM)
    GPIO.setwarnings(False)
    rID = NRF24 (GPIO, spidev.SpiDev())

    #start = time.time()
    #Send and receive addresses
    pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0XE1]]

    #begin radio and pass CSN to gpio (8/ce0) and CE to gpio 17
    rID.begin(0,17)

    #Max bytes 32
    rID.setPayloadSize(32)
    rID.setChannel(0x76)
    rID.setDataRate(NRF24.BR_1MBPS)
    rID.setPALevel(NRF24.PA_MIN)

    rID.setAutoAck(False)
    rID.enableDynamicPayloads()
    rID.enableAckPayload()

    rID.openWritingPipe(pipes[0])
    
    #rID.startListening()
    if (rID =="radio1"):
        rID.openReadingPipe(1, [0xF0, 0xF0, 0xF0, 0xF0, 0xE1])
    if (rID == "radio2"):        
        rID.openReadingPipe(1, [0xF0, 0xF0, 0xF0, 0xF0, 0xB5])
    if (rID == "radio3"):        
        rID.openReadingPipe(1, [0xF0, 0xF0, 0xF0, 0xF0, 0xC3])
    #rID.printDetails()

    
    
    msg = list (str)
    while len(msg) < 32:
        msg.append(0)

    #start = time.time()
    rID.write(msg)
    print("sent msg: {}".format(msg))


    Timeout.timeout_func(rID)


##   rID.startListening()
##
##    
##    while not rID.available():
##        time.sleep (1/500)
##       
##        if time.time() - start > 2:
##            print(rID + " Timed out! ")
##            receivedMessage = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
##            Unpack2.unpack_func(receivedMessage, rID)
##            rID.stopListening()
##            break
                
    receivedMessage = []
    rID.read(receivedMessage, rID.getDynamicPayloadSize())
        
    #### unpack_function is a module that translates and stores values into CB1 table
    #### located:  /usr/lib/pymodules/ICBP_modules/Unpack.py
    print "Radio ID passing to Unpack = " 
    print ""
    print ("Received : {}".format(receivedMessage))
    print ""

    rID.stopListening()

    Unpack2.unpack_func(receivedMessage, rID)

    time.sleep(1/500)

