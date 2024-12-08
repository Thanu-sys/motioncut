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
  print(score)


quiz()
