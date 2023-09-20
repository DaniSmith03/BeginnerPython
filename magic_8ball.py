import random 
name= input("What is your name?: ")
question= input("what is your question?: ")

num= random.randint(1,9)

# print(num)

answer=None



if num==1:
    answer="Yes, definitely."
elif num==2:
    answer="It is decidedly so."
elif num==3:
    answer="Without a doubt."
elif num==4:
    answer="Reply hazy, try again."
elif num==5:
    answer="Ask again later."
elif num==6:
    answer="Better not tell you now."
elif num==7:
    answer="My sources say no."
elif num==8:
    answer="Outlook not so good."
else:
    answer="Very doubtful."


if name or question=="":
    print("I don't have enough information to read your fortune")
else:
    print(name+ ", you wanted to know " + question + ". The 8 ball tells me: " + answer)
