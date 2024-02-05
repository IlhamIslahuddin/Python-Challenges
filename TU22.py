import datetime


def timed_proc():
    x = "the lazy fox jumped over the brown dog"
    usertest = str(input("please type 'the lazy fox jumped over the brown dog' as fast as you can: "))
    if x == usertest:
      print ("done")
    else:
      print ("that was not the correct text, try again")
      timed_proc()
      

start_time = datetime.datetime.now()  # Starts the timer, by putting the time into start_time variable
timed_proc()  # Whatever you want to time
time_taken = datetime.datetime.now()-start_time  # Current time - start time
print(time_taken)  # Printing the time it took
