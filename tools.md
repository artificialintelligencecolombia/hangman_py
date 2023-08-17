# Project Tools

## 17/08

### string library & set() def 

We have this line of code:

´´´
python

import string

alphabet = set(string.ascii_uppercase)
used_letters = set()
´´´.

1. Import string: This line imports the string module, which provides various constants and functions related to strings.

2. alphabet = set(string.ascii_uppercase): This line creates a set called alphabet containing the uppercase letters of the English alphabet. The string.ascii_uppercase attribute from the string module provides a string containing all uppercase letters from 'A' to 'Z'. The set() function is then used to convert this string into a set. Sets are collections of unique elements, so this line ensures that each letter is included only once in the set.

3. used_letters = set(): This line creates an empty set called used_letters, which will be used to store the letters that have been used or processed.



## 13/08

### Create a New Remote Barch - GitHub

1. Create and Switch to a New Branch Locally:

'''bash
git checkout -b new-branch-name
'''
- Create and switch to a new branch.

2. Push the New Branch to the Remote Repository:

'''bash
git push origin new-branch-name
'''
- Push the new branch to the remote repository.