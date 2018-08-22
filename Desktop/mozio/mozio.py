'''
Name=''
Email=''
Phone_Number = ''
Langauge= ''
Currency=''
def data_retrieve():
    global Name
    Name = input('Enter Your Name:-  ')
    global Email
    Email = input('Enter Your Email:- ')
    global Phone_Number
    Phone_Number = input('Enter Your Phone Number:- ')
    global Langauge
    Langauge = input('Enter Your Langauge:- ')
    global Currency
    Currency = input('Enter Your Currency:- ')
def data_process():
    result = "Name:" + Name[0] + "," + Email[0] + "," + Phone_Number[0] + "," + Langauge[0] + "," + Currency[0]
    return result[]
def ticket_print():
    data_retrieve()
    print(data_process())
ticket_print()
'''

import json
import urllib2

# This is the API URL
api = "https://publicdata-weather.firebaseio.com/sanfrancisco/currently.json"

get = urllib2.urlopen(api).read()

print get
