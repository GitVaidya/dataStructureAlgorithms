""""
import time

nemo = ["NEMO"]
large = ['NEMO'] * 10



def findNemo(nemo):
  start = time.time()
  for x in nemo:
    if x == "NEMO":
      print("Found nemo")
  done = time.time()
  elapsed = done - start
  print('Took ' + str(elapsed) + ' milliseconds')

findNemo(large) # O(n) --> Linear time
"""
""""
box = [0,1,2,3,4,5,6,7,8,9,10]
def firstTwoBoxes(boxes):
  start = time.time()
  print(box[0]) #O(1)
  print(box[1]) #O(2)
  done = time.time()
  elapsed = done - start
  print('Took ' + str(elapsed) + ' milliseconds')


firstTwoBoxes(box)  #)(2)
"""

