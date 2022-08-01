# passing user input as integer value
num=int(input())
# passing list values from user upto range
stmt=list(map(int, input().split()))[:num]
# creating an empty list
greater=[]
# appending element count with more than 2 into the greater list
for i in stmt:
    if stmt.count(i)>=2:
        greater.append(i)
# checking length of list with length of set of list inorder to avoid duplicate element in count
if len(stmt)==len(set(stmt)):
    # if true then using max function largest element is printed
    print(max(stmt))
else:
    # else it will print greater element from set of counted list
    print(max(list(set(greater))))


# NB: This can also be implemented using counter function with sets for increased performance.