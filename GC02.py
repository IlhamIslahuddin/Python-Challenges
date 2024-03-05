HourTime = int((input("What time is it? (hour): ")))
AmPm = input("AM or PM? ")
if AmPm == "PM" or AmPm == "pm":
  HourTime = HourTime + 12
MinuteTime = int(input("Minutes?: "))
print("The time is",HourTime,":",MinuteTime)
