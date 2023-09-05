import random

print("\n-----------------------------------\n")
print(".:GissaTalet.")

print("Gissa ett tal mellan 1-10, you get thre treys!\n")
slumptal = random.randint(1, 10)
print(slumptal)
i = 0
hittat = False

while i <3:
    gissatal = input ("mata in tal: ")
    
    if slumptal == int(gissatal):
        hittat= True
        print("\n rätt svar! \n")
        break
    i = 1
    if hittat:
      print("\nbra jobbat, här får du fem spänn ")
    else:
      print("\n Bättre lycka till nästa gång ")
    



if hittat:
    print("\nbra jobbat, här får du fem spänn ")
else:
    print("\n EMOTINAL DAMAGE  ")



print("\n--------------------------------------------------------------------------------------\n")