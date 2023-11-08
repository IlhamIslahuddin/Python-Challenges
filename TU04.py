LeonardoDiCaprioBorn = 1974
MyAge = int(input('When were you born?: '))
AgeDiff = MyAge - LeonardoDiCaprioBorn


if AgeDiff > 0:
    print ("Leonardo DiCaprio is", AgeDiff,"year(s) older than you")
elif AgeDiff == 0:
    print ("You are the same age as Leonardo DiCaprio")
elif AgeDiff < 0:
    print ("You are",(AgeDiff-2*AgeDiff),"year(s) older than Leonardo DiCaprio")
