from string import ascii_letters
import random

code = "+1(91)dd-dd-dd-dd"
code = "".join([str(random.randint(0, 9)) if c in ascii_letters else c for c in code])
print(code)
