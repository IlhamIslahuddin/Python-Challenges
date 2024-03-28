import random

Roasted = str(input("Who is getting roasted? "))

Roasts = [" you are not cool"," you are not swag"," you are less cool than me"," you are not the best"]

Roast = Roasted+(",")+random.choice(Roasts)

print (Roast)
