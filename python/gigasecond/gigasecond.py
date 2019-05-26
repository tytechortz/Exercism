from datetime import datetime
from datetime import timedelta 

def add_gigasecond(moment):
    return((moment + timedelta(days=1000000000/86400)))


