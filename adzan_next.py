# demo-adzan.py
import datetime

ADZAN_HOUR = 4
ADZAN_MINUTE = 45

def minutes_until_adzan():
    now = datetime.datetime.now()
    today_adzan = now.replace(hour=ADZAN_HOUR, minute=ADZAN_MINUTE, second=0, microsecond=0)


    if now > today_adzan:
        today_adzan += datetime.timedelta(days=1)

    diff = today_adzan - now
    total_minutes = int(diff.total_seconds() // 60)
    total_seconds = int(diff.total_seconds())

    return total_minutes, total_seconds

# Calculate
mins, secs = minutes_until_adzan()

# Output format for AHK
print(f"{mins}")
