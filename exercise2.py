def anotherFunChallenge(input):
  a = 5             #1
  b = 10            #1
  c = 50            #1
  i = 0             
  for i in input:   #n
    x = input[i]+1  #n
    y = input[i]+1  #n
    z = input[i]+1  #n
    i = i+1
    print(x,y,z)

  for j in input:   #n
    p = j * 2       #n
    q = j * 2       #n
  
  whoAmI = "I don't know" #1
  print(p,q,whoAmI)

input = [0,1,2,3,4,5]
anotherFunChallenge(input)

#Big O(4+7n)