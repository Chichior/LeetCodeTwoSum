# LeetCodeTwoSum

### This is my solution to the TwoSum Leet Code Challenge. The program takes in nums: a list of integers, and target: a single integer. The program checks for two elements in nums that add up to equal target then it returns the indices that the elements are located at. The same element is never used twice and each input only has one solution. 
### I did this by looping through the range length of nums then within that for loop, looping through the range length of nums but starting at the next index so long as it is less than the length of nums. This avoids an IndexError for being out of range of the list. If the element from the first loop plus the element from the second loop add to equal target, I append each index to an empty list and return that list.
### Upon testing the progam in Leet Code, it passed the three test cases. When the program was submitted, it passed all the test cases, but needs to be optomized for a quicker runtime. 
