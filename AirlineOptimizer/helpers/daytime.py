from datetime import time, datetime

def DayTime(departure_time):
    departure_time = datetime.strptime(departure_time, '%H:%M')
    if departure_time > datetime.strptime('6:00', '%H:%M') and departure_time <= datetime.strptime('7:59', '%H:%M'):
        daytime = "morning"
    elif departure_time > datetime.strptime('8:00', '%H:%M') and departure_time <= datetime.strptime('10:59', '%H:%M'):
        daytime = "late_morning"
    elif departure_time > datetime.strptime('11:00', '%H:%M') and departure_time <= datetime.strptime('13:59', '%H:%M'):
        daytime = "lunch"
    elif departure_time > datetime.strptime('14:00', '%H:%M') and departure_time <= datetime.strptime('16:59', '%H:%M'):
        daytime = "afternoon"
    elif departure_time > datetime.strptime('17:00', '%H:%M') and departure_time <= datetime.strptime('19:59', '%H:%M'):
        daytime = "dinner"
    elif departure_time > datetime.strptime('20:00', '%H:%M') and departure_time <= datetime.strptime('22:59', '%H:%M'):
        daytime = "evening"
    elif departure_time > datetime.strptime('23:00', '%H:%M') and departure_time <= datetime.strptime('05:59', '%H:%M'):
        daytime = "night"
    else:
        daytime = "error, daytime not detected"
    return daytime

