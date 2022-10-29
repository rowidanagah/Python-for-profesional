1- What ’re the methods that you used ?
  -  split_and_join
  -  mutate_string
  -  count_substring
  -  isalnum
  -  minion_game



2- Explain each method ..
  
  - split_and_join
    - take line as a string parameter and return the concatenated / replaceing every white scpace with "-"
  
 
 -  mutate_string
      - this method takes 3 parameters (s :  str , i : int , c : str)
        ```mutate_string(s, i, c):```
      - to covert this s into list to make it mutable 
        ```s = list(s)```
      - ato assign s[i] with c
        ```s[i]= c```
      - then to return re-convert the list into string foramt and to return it 
        ```return ''.join(s)```
  
  -  count_substring 
      - getting 2 string as a parameters A and B as a substring
      - to print the number of occurance of the given substring , we need to loop over the string 
  
  
  -  isalnum 
      - takes no parameter 
      - returns True if all chr of string_name are Alphanumeric  ::: Alphanumeric:A character that is either a letter or a number
  
  -  minion_game 
      - takes s : str as a parameter to loop over it in order to know the winner
      - loop over ths string and if there is upper , add the len from the index of this vowel char up to the end of the sring to kevin and to do the same with stuart if there is consonant char
      - return a name of the winner else return Draw if both of thm have equl val .


 
      


3- What’s new for you ?
  - Nothing


4- Resources ? 
  - [Geek for Geek tutorail about swap_case in python](https://www.geeksforgeeks.org/python-string-swapcase/)
  - [Geek for Geek tutorail about isalnum in python](https://www.geeksforgeeks.org/python-string-isalnum/)

