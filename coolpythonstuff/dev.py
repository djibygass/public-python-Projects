def function(n):
  l=[]
  for k in range(0,3):
    r=0
    for i in range (0,3):
      r=r+n[i][k]
    l.append(r)
  print(l)
function([[2,3,2],[2,3,1],[2,3,1]])