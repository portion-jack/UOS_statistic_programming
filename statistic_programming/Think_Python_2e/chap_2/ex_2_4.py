from math import pi

def spherical_volume(radius):
    volume = (4/3)*(pi)*(radius)**3
    return volume

print("ex_2_4_1")
print(spherical_volume(radius=5))

price = 24.95
dc_price = price * (1-0.4)
tot_price = dc_price + 3 + (dc_price+0.75)*59
print("ex_2_4_2")
print(tot_price)

def time2sec(hour=0,minute=0,second=0):
    tot_sec = hour*3600 + minute*60 + second
    return tot_sec

tot_time = time2sec(minute=8,second=15)*2 + time2sec(minute=7,second=12)*3

def sec2time(second=0):
    hour = second//3600
    second_after_hour = second % 3600
    minute = second_after_hour // 60
    second_after_minute = second_after_hour % 60
    return hour, minute, second_after_minute

hour, minute, second = sec2time(tot_time)


print('ex_2_4_3')
if 52+minute > 60:
    hour += 1
    minute -= 60
    print("{0}:{1}".format(6+hour,52+minute,second))
else :
    print("{0}:{1}".format(6+hour,52+minute,second))
