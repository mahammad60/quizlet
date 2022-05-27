print("welcome to my computer quiz")
playing = input("do you want to play? ")
if playing.lower() != "yes":
    quit()
score = 0
print("okay lets play :)")
num = 2
answer = input("what does CPU stand for? ")
while num <=3 and answer != "central processing unit":
 if num == 3:
     print("hint = central..")
 answer = input("what does CPU stand for? ")
 num += 1
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")

answer = input("what does GPU stand for? ")
while num <=5 and answer != "graphic processing unit":
 if num ==4:
     print("hint = graphic...")
 answer = input("what does GPU stand for? ")
 num+=1
if answer.lower() == "graphic processing unit":
    print("correct!")
    score += 1
else:
   print("incorrect")
answer = input("what does RAM stand for? ")
while num <=7 and answer != "random access memory":
 if num ==6:
     print("hint = random...")
 answer = input("what does RAM stand for? ")
 num+=1
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
   print("incorrect")
answer = input("what does HDD stand for?  ")
while num <=9 and answer != "hard disk drive":
 if num ==9:
    print("hint = disk...")
 answer = input("what does HDD stand for?  ")
 num +=1
if answer.lower()  == "hard disk drive":
    print("correct!")
    score += 1
    num +=1
else:
   print("incorrect")

print("you got " + str(score) + " questions correct!")



















