#QUESTION 1

# The code of my program.
import sys
def countdown(n):
  if n <= 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n-1)
    
def countup(n):
  if n >= 0:
    print('Blastoff!')
  else:
    print(n)
    countup(n+1)
 
if sys.version_info[0] == 3:
  number = int(input('Enter an interger: '))
else:
  number = int(input('Enter an interger: '))


if number> 0:
  countdown(number)
elif number < 0:
  countup(number)
else:
  countup(number)

# Output for the following input: 
# a positive number,  once the user enter positive int 3 you get the below resuls
        # 3
        # 2
        # 1
        # Blastoff!

# a negative number, once a user enter negative int -3 you get the below results
        # -3
        # -2
        # -1
        # Blastoff!


# and for zero.
        # enter the number 0
        # Blastoff!

# the zero digit does not belong either from positive or negative therefore once you enter the same number will display weather you call countup or countdown in your program


