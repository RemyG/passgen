import re
import string
from random import SystemRandom

nb = input("How many words will the password contain?  > ")
pad = raw_input("What character should separate the words?  > ")
print("Generating a " + str(nb) + " words password, with >" + str(pad) + "< as separator.")

with open("diceware.wordlist.asc", "r") as words_file:
    lines = [line.strip() for line in words_file]
    word_map = {string.split(x)[0]: string.split(x)[1] for x in lines if re.match("^[1-6]{5}\s+[a-zA-Z]+", x)}

pass_list = []

while(len(pass_list)<nb):
    cryptogen = SystemRandom()
    vals = [cryptogen.randrange(1, 7) for k in range(5)]
    key = ''.join(str(e) for e in vals)
    if(key in word_map and len(word_map[key]) > 3):
        pass_list.append(word_map[key])

password = pad.join(e for e in pass_list)
print(password)
