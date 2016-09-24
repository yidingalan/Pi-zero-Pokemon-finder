#Courtesy of Pgoapi, tjado, and Adafruit 
#Works for Raspberry pi zero 
#More details will be added later on

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



