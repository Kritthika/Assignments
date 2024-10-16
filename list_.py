#create
empty_list = []
print(empty_list)
#create a list with strings
str_list = ["alpha", "bravo", "charlie"]
int_list =  [0,1,2,3,4,5]
print(str_list[2])
print(int_list[0:2])
print(str_list[-1])
print(int_list[::-1])

#Access elements
print(f"Original value at index 1: {str_list[1]}")
str_list[1] = 'beta'
print(f"Updates value at index 1: {str_list[1]}")
#Adding elements
str_list.append('delta')
print(str_list)

str_list.append(['echo', 'foxtrot'])
print(str_list)

#insert method
str_list.insert(1, 'bravo')
print(str_list)

#extend method
str_list.extend(('golf', 'hotel', 'india'))
print(str_list)

str_list.extend(int_list)
print(str_list)
#join lists
str_list_1 = ['Juliett', 'kilo', 'Lima']
str_list_2 = list(('Mike', 'November'))
joined_str_list = str_list + str_list_1 + str_list_2
print(f"Joined list: {joined_str_list}")

#Removing 
str_list.remove ('beta')
print(f"After removing 'beta': {str_list}")

#pop method
last_1 = str_list.pop()
print(f"After popping without arguments: {str_list}")
print(f"Popped item: {last_1}")

str_list.pop(-1)
print(f"After popping of item in last index: {str_list}")

zero = str_list.pop(8)
print(f"After popping 0 : {str_list}")
print(f"Popped item: {zero}")

#clear method
int_list.clear()
print(f"Afer clearing the int_list: { int_list}")

#del
del str_list[4]
print(f"After deleting item in index 4: {str_list}")

#using del to delete an entire list
#del int_list
#print(f"After deleting int_list: {int_list}")

#looping through list
print("For Loop:")
for i in str_list:
    print(i)
#list comprehension
print("List Comprehension")
[print(i) for i in str_list]
#sorting
int_list = [10,1,8,20,15,6,47]
print("List before sorting", int_list)

int_list.sort()
print("List after sorting: " , int_list)

#sorted function
int_list_1 = [10,1,20, 15, 6, 47]
print("Unsorted list:" , int_list_1)

sorted_list = sorted(int_list_1)
print("Sorted list: ", sorted_list)

#reverse method
sorted_list.reverse()
print("Reversed list: ", sorted_list)

