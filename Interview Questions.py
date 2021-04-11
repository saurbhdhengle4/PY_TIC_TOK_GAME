def count(lists,start,end):
    n=start
    k=end
    h=1
    for i in range(n,k+1):
        d= lists.count(lists[i])
        if lists[i] not in lists[:i]:
             print('{} has occurred {} times'.format(lists[i], d))
        if d > h:
            h=d
            g=i
    print('{} has occurred Max {} times'.format(lists[g], h))

        
             
lists = [] 
n = int(input("How many elements do you want to enter in list : ")) 
for i in range(0, n): 
    ele = int(input()) 
    lists.append(ele)   

start=int(input("Enter the starting index: "))
end=int(input("Enter the end index: "))
print("your list {} and your starting and end index {} and {}.".format(lists,start,end))
count(lists,start,end)