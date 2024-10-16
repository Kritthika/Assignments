#create empty

empty_tup = ()
print(empty_tup)

#reusing the variable name and assign values
empty_tup = (1,2,3)
print(f"Assign values to the previously empty tuple: {empty_tup}")

#creating tuples

str_tup  = ("alpha", "bravo", "charlie")
int_tup = (0,1,2,3,4,5)
mix_tup = (20.50 , True, "Math", -50 , 1+2j)

print(f" A tuple of strings : {str_tup}")
print(f"A tuple of integers: { int_tup}")
print(f"A tuple of mixed data types: {mix_tup}")

#accessing elements
print(f"Third item: {str_tup[2]}")
print(f"First and second items: {int_tup[0:2]}")
print(f"Another way of accessing the 1st and 2nd items: {int_tup[:2]}")
print(f"Last item : {mix_tup[-1]}")
print(f"Accessing in reverse: { int_tup[::-1]}")

#updating tuples:
#mix_tup[-1] = 'complex data type'
#print("Modified mix tuple", mix_tup)

#updating the tuple using the concatenation opertaor

updated_tup = str_tup + int_tup + mix_tup
print("Updated Tuple:", updated_tup)

#using list comprehension

updated_list = [item +100 for item in int_tup]

updated_tuple = tuple(updated_list)
print("Original Tuple:", int_tup)
print("Updated Tuple:", updated_tuple)

#updating a tuple uding append()
#convert tuple to list
new_list = [6, 7, 8, 9, 10]
int_list = list(int_tup)

for element in new_list:
    int_list.append(element)
#converting list back to tuple
int_tup2 = tuple(int_list)
#printing the updated tuple
print("Original Tuple:", int_tup )
print("Updated Tuple 2:", int_tup2)

#Unpack elements in tuples
#unpack tuple items

x, y, z = str_tup
print(f"x: {x}, y: {y}, z: {z}")

x, *y = str_tup
print(f"x: {x} , y : {y}")
print(type(y))

#x, y = str_tup
#x, y, p, q = str_tup

#loop through tuple elements
print("For Loop:")
for num in int_tup2:
    print(num, end = ' ')

#loop through tuple items with while loop

index = 0
print("\n\nWhile Loop:")
while index < len(int_tup2):
    print(int_tup2[index])
    index += 1

#loop through tuple items with index
indices  = range(len(int_tup2))
for i in indices:
    print("tup[{}]: ".format(i), int_tup2[i])

#sorting tuples
def get_first_item(n):
    return n[0]
def sort_list(tuples):
    return sorted(tuples, key = get_first_item)

print(sort_list([('Uniform', 'Charlie'), ('Lima', 'Beta'), ('Zulu', 'Alpha'),('Apple','Mango'),('Banana', 'Olives'),('Cherry', 'Echo')]))
