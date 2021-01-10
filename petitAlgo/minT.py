def plusPetit(tableau):
  z=0
  for a in tableau:
    count=0
    for b in range(0,len(tableau)):
      if a<tableau[b]:
        pp = a
        count+=1
        if count == len(tableau)-1:
          z=pp
  print(z)
plusPetit([55,24,38,54,78])