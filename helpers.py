import csv
import datetime
from math import floor

with open('nigeria.csv', 'r') as f:
    nigeria = [row[0].upper() for row in csv.reader(f)]

months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

ia= ['ABUJA HQRS', 'ALAUSA LAGOS', 'IKOYI LAGOS', 'CALABAR', 'ABEOKUTA'] # Passport Issuing Authorities (some)

cal = {} # create a dictionary mapping months to their numeric values
monthVal = 0

for month in months:
    monthVal += 1
    cal[monthVal] = month

current = datetime.date.today()

def GetName(strrr):
    names = []
    name = ""
    breakCount = 0
    l = len(strrr)

    for i in range(5, l):
        if strrr[i] == '<':
            breakCount += 1
            if breakCount == 1:
                continue
            elif breakCount > 1 and breakCount < 4:
                names.append(name)
                name = ''
                continue
            else:
                names.append(name)
                break
        name += strrr[i]
    return names

def GetID(strrr):
    if strrr[0] == '4':
        idno = 'A' + strrr[1:9]
    elif strrr[0].isalpha() == True:
        idno = strrr[:9]
    else:
        idno = "Not Found. Upload Clearer Image"
    return idno

def Gender(strrr):      # Get Gender From String
    gender = strrr[20:21]
    if gender.upper() == 'M':
        sex = 'Male'
    elif gender.upper() == 'F':
        sex = 'Female'
    else:
        sex = 'Unidentified'
    return sex

def GetPOB(lst):    # Get Place Of Birth from List of Places
    if len(lst) == 0:
        pob = 'NA'
    elif len(lst) == 1:
        if lst[0] in ia:
            pob = 'Place of birth can not be determined'
        else:
            pob = lst[0]
    elif len(lst) == 2:
        pob = lst[0]
    else:
        pob = 'Multiple Locations detected, Consider ReUploading Image File'

    return pob

def GetPIA(lst): # Get Passport Issuing Authority from List of Places
    if len(lst) == 0:
        pia = 'NA'
    elif len(lst) == 1 and lst[0] in ia:
        pia = lst[0]
    elif len(lst) == 2:
        pia = lst[1]
    else:
        pia = 'Undetected, Consider ReUploading Image File'

    return pia

def GetDates(strrr):
    data = {}
    data['dob'] = strrr[13:19].replace('o', '0') #replace any 'o' in dates with '0'
    data['exp'] = strrr[21:27].replace('o', '0')
    # FormatDate(data)
    return data

def ED(strrr):      #ExtractDates
    lst = []
    yr = int(strrr[:2])
    mnth = int(strrr[2:4])
    day = int(strrr[4:])
    lst.extend([yr, mnth, day])
    return lst

def FormatDate(dicto):
    dct = {}
    for key in dicto:
        x = dicto[key]
        date = str(ED(x)[2]) + ' ' + cal[ED(x)[1]] + ' ' + str(ED(x)[0])
        dct[key] = date
    return dct

def Age(strrr):
    # get year for date
    yr = ED(strrr)[0]
    
    if current.year < yr + 2000:
        yr = yr + 1900
    else:
        yr = yr + 2000
    
    birthdate = datetime.date(yr, ED(strrr)[1], ED(strrr)[2])
    diff = current - birthdate
    age = floor(diff.days / 365.25)
    return age

def Validity(strrr):
    yr = ED(strrr)[0]

    if yr + 2000 > current.year + 10:
        yr += 1900
    else:
        yr += 2000

    expiry = datetime.date(yr, ED(strrr)[1], ED(strrr)[2])

    if expiry > current:
        return True
    return False