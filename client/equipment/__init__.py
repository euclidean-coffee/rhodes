from __main__ import *
import people
import utilities

def add_equipment(__type__, __make__, __model__, __serial_number__, __owner__, __price__):
    print('Hello World!')

def equipment_make(__equipment__):
    try:
       if __equipment__ in ('apple', 'mac', 'macbook', 'imac'):
           return "Apple"
       else:
           return __equipment__
    except:
        print("Error: Equipment make is wrong.")
        exit(1)

def equipment_model(__equipment__):
    try:
        return __equipment__
    except:
        print("Error: Equipment model is wrong.")
        exit(1)

def equipment_owner(__equipment__):
    try:
        if __equipment__ in ('-n', '--new'):
            print('Adding new person to database.')
            print('Submit values for the following fields.')
            __person_name__=input('Name: (First Last)')
            __person_location__=input('Location: (City, Province)')
            __person_email__=input('Email: (person@localhost.net)')
            __person_phone__=input('Phone: (1-123-4567)')
            __person__id__ =people.count()
            if (__person_id__.isnumeric()):
                people.add_person(__person__id__, __person__name__, __person_location__, __person_email__, __person_phone__)
            else:
                print('Error 13: Failed to add person.')
                exit(13)
        else:
            __person_id__=people.search_for_person(__equipment__)
            if (__person_id__ > 0):
                people.add_person(__person__id__, __person__name__, __person_location__, __person_email__, __person_phone__)
            else:
                print('Error 33: Failed to locate person in database.')
                exit(33)
    except Exception as e:
        print("Error: Equipment owner is wrong.", e)
        exit(1)

def equipment_price(__equipment__):
    try:
        return __equipment__
    except:
        print("Error: Equipment price is wrong.")
        exit(1)
        
def equipment_serial_number(__equipment__):
    try:
        return __equipment__
    except:
        print("Error: Equipment serial number is wrong.")
        exit(1)
        
def equipment_type(__equipment__):
    try:
        if __equipment__ in ('-c', '--computer'):
           return "Computer"
        else:
            return __equipment__
    except:
        print("Error: Equipment type is wrong.")
        exit(1)
        
def new_equipment(list):
    try:
        __type__ = equipment_type(list[1])
        __make__ = equipment_make(list[2])
        __mdel__ = equipment_model(list[3])
        __srnu__ = equipment_serial_number(list[4])
        __ownr__ = equipment_owner(list[5])
        __pric__ = equipment_price(list[6])
    except:
        print('Error: Something went wrong with your arguments prior to submission to database.')
        exit(1)
    try:
        add_equipment(__type__, __make__, __mdel__, __srnu__, __ownr__, __pric__)
    except:
        print('Error: Unable to submit query.')
        exit(1)
