# libraries
# import cv2
# from matplotlib import pyplot
# import numpy

from helpers import GetName, GetDates, GetID, Gender, GetPOB, GetPIA, FormatDate, Age, Validity
from scan import result, places, strr

# Use helpers functions to extract useful data             
names = GetName(strr[0])
idno = GetID(strr[-1])
dates = GetDates(strr[-1])
gender = Gender(strr[-1])
pob = GetPOB(places)
pia = GetPIA(places)

# Output Data

print(f"Surname: {names[0]}")
print(f"Other Names: {names[1]} {names[2]}")
print(f"Gender: {gender}")
print(f"D.O.B: {FormatDate(dates)['dob']}")
print(f"{Age(dates['dob'])} Years")

print(f"P.O.B: {pob}\nIssuing Authority: {pia}")
print(f"Passport Number: {idno}")

if Validity(dates['exp']) == True:
    print(f"Valid. Expires: {FormatDate(dates)['exp']}")
else:
    print(f"Expired: {FormatDate(dates)['exp']}")