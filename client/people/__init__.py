from __main__ import *
import utilities

def add_person(__id__, __person__, __location__, __email__, __phone__):
    try:
        utilities.commit_query("insert into people values (" + str(__id__) + ", '" + __person__ + "', '" + __location__ + "', '" + __email__ + "', '" + __phone__ + "');")
    except:
        print('Error: There was a problem commiting the query to MySQL.')

def clean(raw_result):
    for row in raw_result:
        __output__=''.join(str(x) for x in row)
    print(__output__)
    return int(__output__)
        
def count():
    __cursor__.execute('select count(ID) from people;')
    return clean(__cursor__.fetchall())
    
def search_for_person(__query__):
    try:
        return 1
    except:
        print('Error: Search.')
