i started with
stacks = int(input("How tall should the pyramid be? "))
if stacks > 8:
    print ("That is out of range, exit the program")

for stacks in range (8):
    print (stacks, end='')
print()
for i in range(10):
  for j in range(10):
    if j >= i:
      print(j, end='')
  print()
the answer was : 01234567
0123456789
123456789
23456789
3456789
456789
56789
6789
789
89
9
I put # after end = but the answer turned in to 5#6#7#8#9#
6#7#8#9#
7#8#9#
8#9#
9#
I couldn't fix it
