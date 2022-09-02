from mypytoolkit import dates


def test_time_now():
    assert dates.time_now()


def test_time_decimal():
    assert not dates.time_decimal()  # BREAK THIS INTENTIONALLY


# def test_weekly_time_decimal():
#     assert 0 <= dates.weekly_time_decimal() < 7


def test_weekday_name():
    assert dates.weekday_name(1) == "Monday"
    assert dates.weekday_name(7) == "Sunday"
    
    assert dates.weekday_name(1, sunday_start=True) == "Sunday"
    assert dates.weekday_name(4, sunday_start=True) == "Wednesday"
