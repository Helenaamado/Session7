print(dir("hello"))
print(help("hi".capitalize))

print("i like to go to school".capitalize())
print("IS THIS SUPPOSED TO WORK?".capitalize())
# capitalise = s[:1].upper()

print("hello". center(40, "-"))
print("gmail.com".find("."))
print("gmail.com".find("john")) # if is -1 then it did not find it
s="i see a cat who like to cat while i cat on a cat"
#find all occurrences
poz=0
while True:
    poz= s.find("cat", poz)
    if poz == -1:
        break
    print("found cat on position", poz)
    poz+=1
# join - we will come back later

#lower: lowercase everything
s="I SEE A LOT OF THINGS"
print(s.lower())

#replace
s= "i see a cat that likes to eat a rat. what a good cat"
print(s.replace("c", "r"))
print(s.replace("cat", "lion"))

#split
s= "i like to go shopping"
print(s.split())

#title
s = "i like the mountains"
print(s.title())
splitted= s.split()
print("XX".join(splitted))

#upper
s4 = "i see a lot of things"
print(s4 .upper().capitalize())
