def initialisation_du_tableau(t=[],n=0):
   for x in range(0,n):
      t.append(1)
   return print(t)


initialisation_du_tableau([],5)


def barrer_les_multiple_de(k,t=[],n=0):
   t=initialisation_du_tableau([],n)
   for x in range(0,len(t)-1):
      if x%k == 0:
         print('jap')

#barrer_les_multiple_de(10,[],5)