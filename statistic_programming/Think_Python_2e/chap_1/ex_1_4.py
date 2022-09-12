def killo2mile(killo):
    mile = killo/1.61
    return mile

def time2sec(hour=0,minute=0,second=0):
    tot_sec = hour * 60 * 60 + minute * 60 + second
    return tot_sec

killo = 10
minutes = 43
seconds = 30

mile = killo2mile(10)
tot_second = time2sec(minute=minutes,second=seconds)
tot_hour = tot_second/3600

ans = mile/tot_hour
print(ans)
