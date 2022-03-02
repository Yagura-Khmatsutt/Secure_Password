'''Secure Password'''
import random
from string import digits
from string import punctuation
from string import ascii_letters

symbols = ascii_letters + digits + punctuation
secu_random = random.SystemRandom()
password = "".join(secu_random.choice(symbols)
                   for i in range(20))

print(password)
