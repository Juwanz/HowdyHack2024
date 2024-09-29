#!/usr/bin/env python
import math
#TODO '''GATHER DATA VALUES FOR USER, LOOP THROUGH DATABASE'''

# LOOP THROUGH DATABASE


points = 0
def pointsCalc(error):
    if error == 0: points += 5
    elif error <2: points +=4
    elif error <3: points +=3
    elif error <4: points +=2
    elif error <5: points +=1
    return null

error = math.abs(user.room_temp - data.room_temp)
pointsCalc(error)

error = math.abs(user.roommate_interaction - data.roommate_interaction)
pointsCalc(error)

error = math.abs(user.age - data.age)
pointsCalc(error) 

error = math.abs(user.cleanliness - data.cleanliness)
pointsCalc(error)

error = math.abs(user.roomie_loud - data.self_loud)
pointsCalc(error)

error = math.abs(user.roomie_guests - data.self_guests)
pointsCalc(error)

error = int(user.self_major == data.self_major)
if error == 0:
    points += 5

error = math.abs(user.sleep_time - data.sleep_time)
pointsCalc(error)

percent_match = points / 40 * 100















