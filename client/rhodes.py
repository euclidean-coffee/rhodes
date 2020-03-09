#!/usr/bin/env python3

## Libraries

import mysql.connector
import getpass
import os
import sys

##

## Rhodes

import equipment
import people

##

## Global Variables

__author__ = "Sam Klein"
__software__ = "Client for Rhodes Database Manager CLI"
__version__ = "rhodes-r0-rhel-a.01"
__project__ = "https://github.com/srukle/rhodes"
__optdirs__ = "/opt/rhodes/"
__secrets__ = "/opt/rhodes/.secrets"
__user__ = ""
__pass__ = ""

##

## Subroutines

def read_secrets():
    """Method reads secrets inside the opt folder.
    If secrets cannot be found, the user is prompted 
    to create a new folder."""
    global __user__
    global __pass__
    if os.path.isfile(__secrets__):
        with open(__secrets__) as __secret_line__:
           __user__ = __secret_line__.readline().strip()
           __pass__ = __secret_line__.readline().strip()
    else:
        try:
           os.mkdir('/opt/rhodes')
           __new_secret__ = open(__secrets__,"w+")
           __new_secret__.write("user: " + input("Username: ") + "\n")
           __new_secret__.write("pass: " + input("Password: ") + "\n")
           __new_secret__.close()
           read_secrets()
        except IOError as e:
           if (e[0] == errno.EPERM):
              print >> sys.stderr, "You need root permissions."
              sys.exit(1)

def load_pass(password):
    """Reads password secrets and intreprets them 
    for rhodes."""
    if ("pass: " in password):
        return password.replace('pass: ', '')
    else:
        return 'CRITICAL ERROR'

def load_user(user):
    """Readd user secrets and intreprets them for
    rhodes."""
    if ("user: " in user):
        return user.replace('user: ','')
    else:
        return 'CRITICAL ERROR.'

def main():
    try:
        if sys.argv[1] in ('-ne', '--new-equipment'):
            equipment.new_equipment(sys.argv[1:])
        else:
            print('NOTHING')
    except Exception as ex:
        print('Error.')

if __name__ == "__main__":
    read_secrets()
    print(__user__)
    print(__pass__)
    __rhodes__ = mysql.connector.connect(
        host='localhost',
        user=load_user(__user__),
        passwd=load_pass(__pass__),
        database='rhodes'
        )
    __cursor__ = __rhodes__.cursor()
    main()
