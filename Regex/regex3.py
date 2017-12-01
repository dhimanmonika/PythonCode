"""             r'^\w+',     # word at start of string
                r'\A\w+',    # word at start of string
                r'\w+\S*$',  # word at end of string, with optional punctuation
                r'\w+\S*\Z', # word at end of string, with optional punctuation
                r'\w*t\w*',  # word containing 't'
                r'\bt\w+',   # 't' at start of word
                r'\w+t\b',   # 't' at end of word
                r'\Bt\B',    # 't', not start or end of word"""
import re
example="This is string with some -- punctuation."

print("string  : {}".format(example))

print("\n Character at the starting of string")
print(re.findall(r'^\w',example))

print("\n word at the starting of string")
print(re.findall(r'^\w+',example))

print("\n word at the end of string with optional punctuation")
print(re.findall(r'\w+\S*$',example))

print("\n word containing t ")
print(re.findall(r'\w*t\w+',example))

print("\n word starting with s ")
print(re.findall(r'\bs\w+',example))

print("\n word ending with e ")
print(re.findall(r'\w+e\b',example))

print("\n word containing  e excluding start and end of word ")
print(re.findall(r'\w+i\w+',example))