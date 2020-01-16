### decode date

#def decodeYear(seconds):
def decodeDate(seconds):
    years = (seconds / (365*24*60*60))
    year = years + 1970
    print str(year)
'''
def decodeDate (seconds):
    year = decodeYear (seconds)


def decodeDay(seconds, years):
    daysFloat = ((years - (years / 4.0)) * 366) + ((years / 4.0) * 365)
    daysInt = ((years - (years / 4)) * 366) + ((years / 4) * 365)
    days = daysFloat - daysInt
    print str(daysFloat)
    print str(daysInt)
'''
