# Find the Highest Common Factor (HCF) of 18 and 30.
n = 18
while True:
  if (18/n)% == 0:
    if (30/n)% == 0 :
      print(n)
      break
  else:
    n = n-1  
  
