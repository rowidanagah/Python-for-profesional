1- What ’re the methods that you used ?
  - average
  - symmetric_difference 
  - add
  - remove & pop & discard
  - union




2- Explain each method ..
  - average
      - take an arr as a parameter and covert this arr to set to delet duplicate  
      - to return the sum of this set divided by its len to get the avrage of distinct val in arr
  
  - symmetric_difference
       - This in-built function of Python Set to return the elements that present in either of the two sets, but not common to both the sets.
       - takes no parameters
       - syntax ::: set_A.symmetric_difference(set_B)
       - this method is equal to ^ operator

  - add 
       - The set add() method adds a given element to a set if the element is not present in the set else do nothing
       - this method take only elm as a parameter and no matter what is the type of  this elm if it's list , int or str
  
  
  
  - union()
       - jest to return the union of sets in a new set
  
  - intersection
       - Given set A nad B , return the common elements to both the set A and set B
       - syntax :: set1.intersection(set2, set3, set4….) and it's an in parameters method 
  
  - difference 
       - returns a set that is the difference between two sets . ex  (set A – set B) will be the elements present in set A but not in B and (set B – set A) will be the elements present in set B but not in set A. A-B != B-A .
       - syntax :: setA.difference(setB) for (setA - setB)

  - intersection_update
       - syntax :: setA.intersection_update(setB, setC ... etc)

       - Remove the items that is not present in both SetA, and setB:
  
  - update 
       - parameters ::: only takes one elm as a parameter and no matter what the type of this elm , it will be converted to set .
       - syntax :: setA.update(setB)
       - This method adds setB to setA and returns nothing.






3- What’s new for you ?
   - Nothing

4- Resources ? 
 - [Geek for Geek tutorial about sets](https://www.geeksforgeeks.org/python-sets/)
