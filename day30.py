#Regular Expression (Reg Ex)
#---------------------------
'''

--> This regular expression or RegEx is a sequence of charcters that forms a searching pattern
--> To use this we have to import re, which will unlock the

Functions
----------
1.Findall
--> By using this function it will find all the sequence of characters in the string
syntax -> re.findall("metachar",variable_name)

Eg.

import re
any = "python is a language"
so= re.findall("a",any)
print(so)


2.Search
--> By using this function , it will only find the first sequence in the string
syntax -> re.search("metachar",variable_name)

Eg.

import re
any = "python is a language"
so= re.search("a",any)
print(so)


# Metacharacters
-------------
--> Metacharcters are used to form searching pattern 

1.[] --> in this metacharcters we can search for [a-z],[A-Z],[0-9]
-----
Eg.

import re
any = "a lot was left unsaid"
so= re.findall("[a-z]",any)
the=re.search("a",any)
print(so)
print(the)

import re
any = "a lot was left unsaid"
so= re.findall("[aes]",any)
print(so)

import re
any = "a 0lot was 4 left 1unsaid 8"
so= re.findall("[0-9]",any)
print
(so)

import re
any = "a 0lot was 4 left 1unsaid 8"
so= re.findall("[0-9a-z]",any)
print(so)


2.dot(.)
--------

Eg.
---
import re
we="hello"
the=re.findall("h...o",we)
some=re.search("h...o",we)
print(the)
print(some)

3. cap(^) -> This is used to find the string is starting with the sequence or  
--------- 
syntax -> re.findall("metachar",variable_name)

Eg.
----
import re
many="dream inspire focus motivate improve creative positive"
so=re.findall("^dream",many)
then=re.search("^dream",many)
print(many)
print(then)

4. dollar($) ->  This is used to find the string is ending with the sequence
-------------
syntax -> re.findall("metachar",variable_name)

Eg.
---

import re
out="This is used to find the string is ending with the sequence   "
one=re.findall("sequence   $",out)
two=re.search("This$",out)
print(one)
print(two)


5. (*) --> This meta character will form a searching pattern as it will take any zero or more charcter for (*)
--------

Eg.
----

import re
dimple="  This is used to find the string is ending with the sequence "
gk=re.findall("T.*s",dimple)
mk=re.search("T.*",dimple)
print(gk)
print(mk)


6.(+) --> This meta character will form a searching pattern as it will take any one or more charcter for (+)
------
'''
'''
import re
dimple="  This is used to find the string is ending with the sequence "
gk=re.findall("en.+g",dimple)
mk=re.search("t.+",dimple)

print(gk)

print(mk)
'''


#7.(?)
'''
----
-> This meta charcter will form a searching patterms as it will take any zero or one charcter for(?)
syntax --> re.findall(".?",variable_name)

import re
any=" This meta charcter "
an=re.findall("Th.?",any)
so=re.search("Th.?",any)
print(an)
print(so)

'''
#8.{}
'''
------
--> This meta charcter will form a searching patterns as we can mentioned the size in the {}

import re
any=" This meta charcter will form a searching patterns as it will take any zero or one charcter  "
an=re.findall(".{50}",any)
print(an)

'''

#9. (|)
'''
--------
--> This meta charcter will form a searching patterns as it consider right or left any string is present or not for (|)

import re
any=" This meta charcter will form "
an=re.findall("that|will",any)
print(an)

'''

#special sequence
'''
-----------------
A special sequence is a followed by one of the charcter are at the beginning of the string

1.\A
------
returns a match if the specified charcter are at the beginning of the string

EG: "\AThe"

import re
txt="The rain is spain"
#check if the string starts with "The":
x=re.findall("\AThe",txt)
print(x)

if x:
    print("yes, there is match!")
else:
    print("No match")

2.\b
------
return a match where the specified charcter are at the beginning or at the end of word

EG: r"\bain"


import re
txt = "The rain in spain"
#check if is present at the beginning of WORD:

x=re.findall(r"\bspain",txt)
print(x)

if x:
    print("yes, there is atleast one match!")
else:
    print("No match")


3.\d
-----
--> returns a match if the string contains any digits (numbers from 0-9) 

EG: "\d"

import re
txt = "The rain in 56 spain"
#check if the string contains any digits (numbers from 0-9)

x=re.findall("\d",txt)
y=re.search("\d",txt)
print(x)
print(y)
if x:
    print("yes, there is atleast one match!")
else:
    print("No match")


3.\D
-----
--> returns a match where the string DOES NOT contain digits

EG:"\D"

import re
txt = "The rain in 56 spain"
#Return a match at every no digit charcter:

x=re.findall("\D",txt)
print(x)

if x:
    print("yes, there is atleast one match!")
else:
    print("No match")


4.\s
-----
--> returns a match where the string contains a white space character

EG: "\s"

import re
txt = "The rain in spain"
#Return a match at every white space character:

x=re.findall("\s",txt)
print(x)

if x:
    print("yes, there is atleast one match!")
else:
    print("No match")


'''
# Time and DATE 
# ---------------------
'''

%d --> Day
%m --> Month
%Y --> Year
%H --> Hour
%M --> Min
%S --> Sec
%p --> AM/PM
%A --> Day name
%B --> Month name


import datetime
today = datetime.date.today()

print(today.strftime("%d-%m-%Y"))
print(today.strftime("%A"))
print(today.strftime("%B"))


'''



