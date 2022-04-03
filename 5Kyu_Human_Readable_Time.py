# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures

def make_readable(seconds):
    result = []
    hour = 0
    if seconds // 3600 > 0:
        hour = seconds // 3600
        result.append(str(hour).zfill(2))
    else:
        result.append('00')
    sec = (seconds - hour*3600)
    if sec >= 60:
        mins = sec // 60
        result.append(str(mins).zfill(2))
    else:
        result.append('00')

    result.append(str(sec%60).zfill(2))
    c = ':'.join(result)
    return c
