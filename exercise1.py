def funChallenge(input):
  a = 10      #O(1)
  a = 50 + 3  #O(1)

  for i in input:     #O(n)
    anotherFunction() #O(n)
    stranger = True   #O(n)
    a = a + 1         #O(n)
    return a          #O(1)

def anotherFunction():
  print()

input = ["vaidya", "Nemo", "abc", "def"]
result = funChallenge(input) 
print(result)     

# BigO(3+4n) => O(n)

