from datetime import datetime as dt

def time_now(int_times: bool = False):
    """Returns the current time in string format HH-MM."""
    if not int_times:
        return dt.now().strftime("%H-%M")
    else:
        time_hours, time_mins = dt.now().strftime("%H-%M").split(sep = '-')
        return (int(time_hours), int(time_mins))

def time_decminal():
    """Returns the time as a float. 08-30 is 8.5."""
    time_hours, time_mins = time_now(int_times = True)
    fraction_mins = time_mins/60
    fractional_time = time_hours + fraction_mins
    return float(fractional_time)

def today_date():
    """Returns today's date in string format 2022-02-22."""
    return str(dt.now().date())