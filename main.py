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

