## What ’re the methods that you used ?

- seach

- match

- group

- isalnum

## Explain each method ..
    
- seach -> dict
    - ***Syntax*** : ` re.search(pattern, string, flags=0  :: modifiers)`.
    - ***Parameters*** : **pattern** , **string** and   **flags**  as a modifiers . 
    - ***Returns*** : return a corresponding match object. Return None if no position in the string matches the pattern;
    - It searches for the whole string even if the string contains multi-lines and tries to find a match of the substring in all the lines .
    
- match -> dict
    - ***Syntax*** : ` re.match(pattern, string, flags=0  :: modifiers) `.
    - ***Parameters*** : **pattern** , **string** and   **flags**  as a modifiers . 
    - ***Returns*** :  return a corresponding match object. Return None.
    - Ut searches only the beginning of the string even in MULTILINE mode, re.match() will only match at the beginning of the string

- group 
    - ***Syntax*** : ` Match.group([group1, ...]) `.
    - ***Parameters*** : **number**  (optional parameter) return the wwhole match group if it's not given else return the number of subgroup 
    - ***Returns*** : Returns one or more subgroups of the match .
 
- isalnum
    - ***Syntax*** : ` string_name.isalnum() `.
    - ***Parameters*** : takes no parameters
    - ***Returns*** : Returns True: If all the string are alphanumeric else False .
    - Checks whether all the characters in a given string is alphanumeric or not.
        - alphanumeric means letter or a number
 

## What’s new for you ?
- The whole content .

## Resources ? 

- [python documentation about re module](https://docs.python.org/3.7/library/re.html)

- [Google  tutorial about re module](https://developers.google.com/edu/python/regular-expressions?fbclid=IwAR31xKoW9Cn0x-NaWIe0BVLmVSjPEEPGr8Xe52sqFTC4dKlJhX-L0CrSgn8)

- [Geek for Geeks tutorial about fillter function](https://www.geeksforgeeks.org/filter-in-python/)
