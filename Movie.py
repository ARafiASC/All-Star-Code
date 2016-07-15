from random import *
list1=["Guns","Monsters","Avengers", "Gods","Jerks","Nerds","Apples","Racers","Players","Computers"]
list2=["Return", "TheGetBack","Redemption","Curse","Matrix","Gladiator","Building","Hate","Watchful","Millions"]
list3=["Of","By","With","The","And","Through","Or","A","To","From"]
a = list1[randrange(0,10)]
b = list2[randrange(0,10)]
c = list3[randrange(0,10)]
x=a+b+c
print(x)
i=0
while i<11:
    a = list1[randrange(0,10)]
    b = list2[randrange(0,10)]
    c = list3[randrange(0,10)]
    y = a + b +c
    i=i+1
    print(y)