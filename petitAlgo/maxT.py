def plusGrand(tableau):
  for a in tableau:
    counter=0
    for b in range(0,len(tableau)):
      if a > tableau[b]:
        counter+=1
        if counter == len(tableau)-1:
          maxx=a
  print(maxx)
          


plusGrand([55,1,2,3,25,33,44,85,255,26])
