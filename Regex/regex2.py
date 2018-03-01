"""             'ab*?',     # a followed by zero or more b
                'ab+?',     # a followed by one or more b
                'ab??',     # a followed by zero or one b
                'ab{3}?',   # a followed by three b
                'ab{2,3}?', # a followed by two to three b
                '[^-. ]+',  # sequences without -, ., or space
                '[a-z]+',      # sequences of lower case letters
                '[A-Z]+',      # sequences of upper case letters
                '[a-zA-Z]+',   # sequences of lower or upper case letters
                '[A-Z][a-z]+', # one upper case letter followed by lower case letters"""
import re
example2= "aabbbbaababaa"
pattern ="ab"

#multiple matches : findall()
#The findall() function returns all of the substrings of the input that match the pattern without overlapping.
print("given input : aabbbbaababaa ")
print("findall() will return all matches AS STRINGS")
for match in re.findall(pattern,example2):
    print("found {}".format(match))

#finditer() returns an iterator that produces Match instances instead of the strings returned by findall().
print("\n given input : aabbbbaababaa ")
print(" finditer() will return match as instance")
for match in re.finditer(pattern,example2):
    s=match.start()
    e=match.end()
    print(" match fount at {} and end at {}".format(s,e))

#'[^-. ]+',  # sequences without -, ., or space
print("\n given input : This is Line - with Punctuation . ")
print("'[^-. ]+' giving match without -,. space")
example21="This is Line - with Punctuation ."
for match in re.finditer(r'[^-. ]+',example21):
    print(match)


 # sequences of lower case letters
print("\ngiven input : This is Line - with Punctuation . ")
print("'[a-z]+' giving match in lowercase")
for match in re.finditer(r'[a-z]+',example21):
    print(match)


