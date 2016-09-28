#Courtesy of Pgoapi, tjado, and Adafruit 
#For Raspberry pi zero 

import os
import sys
import json
import time
import pprint
import logging
import getpass
import argparse
import random
from subprocess import call
from gpiozero import LED 

import RPi.GPIO as GPIO
from time import sleep

#PGO API
from pgoapi import pgoapi
from pgoapi import utilities as util

#Pokemon rarity 
#From http://www.gamerevolution.com/faq/pokemon-go/pokmon-rarity---from-common-to-legendary-with-pictures-125819
COMMON_POKE = [69,10,50,84,96,23,133,92,74,118,98,66,129,81,56,52,32,29,43,46,16,60,19,27,79,48,100,13,41]
UNCOMMON_POKE = [63,24,1,4,35,104,101,102,42,75,88,58,93,106,116,39,124,14,140,64,109,82,11,53,17,25,77,54,20,111,28,86,90,21,7,120,72,37]
RARE_POKE = [142,59,12,113,91,85,147,51,125,83,22,136,55,44,107,97,135,99,108,68,67,126,122,30,33,38,138,95,47,61,137,57,78,112,117,119,123,143,121,114,73,110,40]
VERY_RARE_POKE = [65,15,5,87,148,103,94,76,130,2,141,115,131,105,89,34,31,139,18,127,62,26,80,134,49,71,45,8,70]
EPIC_POKE = [9,6,36,149,128,3]
LEGENDARY_POKE = [144,132,151,150,146,145]

#Assign gpio pinouts 
led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

#Function to enable or disable the LEDs 
def enable_led(pinNum, enableOrNot):
    if enableOrNot:
        GPIO.output(pinNum, True)
    else:
        GPIO.output(pinNum, False)

#Initial configuration
#Courtesy to Tjado 
def init_config():
    parser = argparse.ArgumentParser()
    config_file = "config.json"

    # If config file exists, load variables from json
    load   = {}
    if os.path.isfile(config_file):
        with open(config_file) as data:
            load.update(json.load(data))

    # Read passed in Arguments
    required = lambda x: not x in load
    parser.add_argument("-a", "--auth_service", help="Auth Service ('ptc' or 'google')",
        required=required("auth_service"))
    parser.add_argument("-u", "--username", help="Username", required=required("username"))
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument("-l", "--location", help="Location", required=required("location"))
    parser.add_argument("-d", "--debug", help="Debug Mode", action='store_true')
    parser.add_argument("-t", "--test", help="Only parse the specified location", action='store_true')
    parser.set_defaults(DEBUG=False, TEST=False)
    config = parser.parse_args()

    # Passed in arguments shoud trump
    for key in config.__dict__:
        if key in load and config.__dict__[key] == None:
            config.__dict__[key] = str(load[key])

    if config.__dict__["password"] is None:
        log.info("Secure Password Input (if there is no password prompt, use --password <pw>):")
        config.__dict__["password"] = getpass.getpass()

    if config.auth_service not in ['ptc', 'google']:
      log.error("Invalid Auth service specified! ('ptc' or 'google')")
      return None

    return config

#hook up a pi and look into sudo raspi-config 


def main():

	#All LEDs should be disabled initially 
    enable_led(led1, False)
    enable_led(led2, False)
    enable_led(led3, False)
    # log format
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(module)10s] [%(levelname)5s] %(message)s')
    # log level for http request class
    logging.getLogger("requests").setLevel(logging.WARNING)
    # log level for main pgoapi class
    logging.getLogger("pgoapi").setLevel(logging.INFO)
    # log level for internal pgoapi class
    logging.getLogger("rpc_api").setLevel(logging.INFO)

    #load the config 
    config = init_config()
    #load the pgoapi
    api = pgoapi.PGoapi()

    



