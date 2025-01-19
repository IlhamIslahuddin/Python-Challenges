from datetime import datetime, timedelta

if __name__ == "__main__":
    current_time = datetime.strptime("14:00", "%H:%M")
    n = 51
    duration = timedelta(hours=n)

    # Calculate the time the alarm should go off
    alarm_time = current_time + duration

    # Calculate the number of days later
    days_later = duration.days

    print (f"Starting today at {current_time.hour}:{current_time.minute}...")
    alarm_time_str = alarm_time.strftime("%H:%M")
    print(f"The alarm should go off {days_later} days later at: {alarm_time_str}")
