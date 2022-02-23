from datetime import datetime as dt

def time_now():
    """Returns the current time in string format HH-MM."""
    return dt.now().strftime("%H-%M")

def today_date():
    """Returns today's date in string format 2022-02-22."""
    return str(dt.now().date())