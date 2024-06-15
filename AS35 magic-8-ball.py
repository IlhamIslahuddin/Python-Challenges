import random

def magic_8_ball():
    phrases = ["It is certain.","It is decidedly so.","Without a doubt.","Yes, definitely.","You may rely on it.","As i see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.",
               "Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.",
               "Outlook not so good.","Very doubtful."]
    question = input("What is the yes or no question? ")
    answer = random.choice(phrases)
    print (answer)


if __name__ == "__main__":
    magic_8_ball()
