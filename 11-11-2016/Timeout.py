import sys
########################Modules Path Information################################
sys.path.append("/usr/lib/pymodules/ICBP_modules")
sys.path.append("/usr/lib/NRF24")
########################Modules Path Information################################
import Unpack2
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
import array


def timeout_func(rID= ""):

    rID.startListening()
    start = time.time()

    while not rID.available():
        time.sleep (1/500)
       
        if time.time() - start > 2:
            print(" Timed out! ")
            receivedMessage = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
            ##Unpack2.unpack_func(receivedMessage, rID)
            rID.stopListening()
            break
##        else:
##            receivedMessage = []
##        
            
        
        
