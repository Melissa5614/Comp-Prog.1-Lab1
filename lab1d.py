
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Melissa Aydin
# Date:16 Sep 2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1d.py 
name=('Melissa') 
name= name.upper()
age=19
print("How are you {}? Happy {}th birthday!".format(name, age))
#TO-DO 2:
# Create a variable called "words".
# The value of words should be "The quick brown fox jumps over the lazy dog".
# Use indexing to return the first and 17th charecters of "words" to the user.
words= 'The quick brown fox jumps over the lazy dog'
print(words[0])
print(words[16])
slice1= words[-23:-18]
print(slice1)
slice3=words[2:15]
print(slice3)
print (words[5:22])
#TO-DO 3:
# Use negative indexing to return the words "jumps" and "quick" from "words" to the user.

