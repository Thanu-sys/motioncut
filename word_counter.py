def wordcount(b):
  count=1
  for i in range(1,len(b),1):         #for loop used to count the number of words present in sentence or paragraph.
    count+=1
  return count

user=input("Please enter a sentence or a paraghraph: \n")
b=user.split()                       #split() methond coverts the string into list for esay counting.
result=wordcount(b)                  # it stores the return value from wordcount function.
print(b)                             #words for debugging for proper undersanding.
print("WORD COUNT: ",result) 