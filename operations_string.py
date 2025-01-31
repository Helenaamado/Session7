s1= "hello"
s2= "world"
print(s1 +" "+ s2) # the quotes are used to generate space  between the words
print(s1, "hello")
print(3*s2)
print((10//2)*s1) # this makes the math and then multiplies the string
print(s1, len(s1))
print(3*s2, len(3*s2))
for c in s2:
    print(c)
    print(c*4, end= " ")
print(4* s1[0],4* s1[1], 4* s1[2], 4*s1[3], 4*s1[4] )

new_string = " "
for c in s2:
    new_string+= c*4
    print( new_string)

print(new_string)
#it can be used to check if one string is inside another
print("h" in s1) #true
print("d" in s2) #true
print("x" in s2) #false
print("wor" in s2) #true
