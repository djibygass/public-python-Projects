def zero(x): return 0
def one(x): return 1
def two(a): return 2
def three(a): return 3
def four(*a): return 4
def five(a): return 5
def six(a): return 6
def seven(a): return 7
def eight(a): return 8
def nine(*a): return 9

def plus(*a): return a
def minus(a): return -a
def times(a): return a
def divided_by(a): return 1/a

print(four(plus(nine())))
