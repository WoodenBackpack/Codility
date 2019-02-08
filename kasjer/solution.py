# Solution for :
# SM_01_00 - Szyfr
# https://pl.spoj.com/problems/SM_01_00/
#
# https://repl.it/@PiotrWroblewski/SolidRingedTests
#
#

from textwrap import wrap

def solution(input1):
  int_for_A = ord("A")
  for x in input1:
    x = wrap(x, 5)
    for y in x:
      print(chr(int_for_A + int(y,2)),end="")
    print()

input1 = ["00110100010000010011101000101100000000100100100100","000000101100000011000000001010011101001100000","0000101110010110010001010010000101101110010110010001010"]

solution(input1) 
