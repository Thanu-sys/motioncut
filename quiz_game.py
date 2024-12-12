print("WELCOME TO FUN QUIZ 🧠")
print("Our quize game put the fun into learing.Your knowledge will be tested on a variety of  fun and intresting topics.")

playing = input("If you are intrested please press yes to begin: ")

if playing.lower()!="yes":
  quit()
print("Okay! lets have fun 😁")

def quiz():
  score=0
  ans=print("Which ocean is the deepest on earth?")
  opt=input("1.Indian Ocean  2.Pacific Ocean  3.Arctic Ocean")

  if opt=='2':
    print("Correct✅")
    score+=1
  else:
    print("Incorrect❎\nPacific Ocean✅ ")

  ans=print("Which animal is most friendly witj humans?")
  opt=input("1.Dog  2.Cat  3.Elephant")
  if opt=='1':
    print("Correct✅")
    score+=1
  else:
    print("Incorrect❎\nDog✅ ")

  ans=print("Who is the current prime minister of India?")
  opt=input("1.A.P.J.Abdul kalam  2.Narendra Modi  3.Indra Ghandi")
  if opt=='2':
    print("Correct✅")
    score+=1
  else:
    print("Incorrect❎\nNarendra Modi✅ ")

  ans=print("Which body part have unique prints other than fingerprits?")
  opt=input("1.Nose 2.Tounge 3.eyes")
  if opt=='2':
    print("Correct✅")
    score+=1
  else:
    print("Incorrect❎\nTounge✅ ")

    ans=print("Which fruit is known for being high in vitamin c?")
  opt=input("1.Watermelon 2.Apple 3.Orange")
  if opt=='3':
    print("Correct✅")
    score+=1
  else:
    print("Incorrect❎\nOrange✅ ")
  return score
score=quiz()
def marks(score):
  if score==5:
    print("Hurray you got ",score,"🥳🎉")
  elif score==4:
    print("Excellent you scored",score,"🎉🎊")
  elif score==3:
    print("Good you scored",score,"🎉")
  elif score==2:
    print("Good try,you scored",score,"🎊")
  elif score==1:
    print("You scored",score,"🙂,Better luck next time👍")
  else:
    print("Oops,You lost😞")

marks(score)



