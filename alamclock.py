import datetime
import time
import winsound

# Get the alarm time from the user
alarm_input = input("Set alarm time (HH:MM:SS): ")

# Parse and validate the input
try:
    alarm_hour, alarm_minute, alarm_second = map(int, alarm_input.split(":"))
    if not (0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59 and 0 <= alarm_second <= 59):
        raise ValueError
except ValueError:
    print("Invalid time format. Please use HH:MM:SS with 0 <= HH <= 23, 0 <= MM <= 59, 0 <= SS <= 59")
    exit()

# Create alarm time object
alarm_time = datetime.time(alarm_hour, alarm_minute, alarm_second)

# Get current datetime
now = datetime.datetime.now()

# Create alarm datetime for today
alarm_datetime = datetime.datetime.combine(now.date(), alarm_time)

# If alarm time has already passed today, set for tomorrow
if alarm_datetime < now:
    alarm_datetime += datetime.timedelta(days=1)

# Confirm the alarm time to the user
print(f"Alarm set for {alarm_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

# Calculate the time difference
delta = (alarm_datetime - now).total_seconds()

# Wait until the alarm time
if delta > 0:
    time.sleep(delta)

# Trigger the alarm
print("Alarm!")
# Play a beeping sound 10 times (500ms beep, 500ms pause)
for _ in range(10):
    winsound.Beep(1000, 500)  # 1000 Hz frequency, 500ms duration
    time.sleep(0.5)