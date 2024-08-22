"""zip_list.py

This assignment is to gain knowledge on quick sort using linked list.
As implementation scenario, shopping list have been reselected.
The program stores zip codes in a linked list.
Each storing mechanism are separated to a separate file “linked_list_zip_list_manager.py” 
Note that “zip_list.py” with the “main” method has been already implemented,
and you are assigned to implement other classes/methods. As part of assignment, compare actual runtime of
quick sort operation over different N sizes and experiment/analyze the performance as N grows.

"""
# file name: linked_list_zip_list_manager.py
# class name: LinkedListZipListManagerClass
from linked_list_zip_list_manager import LinkedListZipListManagerClass # type: ignore 
import time
# pip install Faker for Faker installation in your computer
from faker import Faker # type: ignore 

# We need to populate the # of items for search operation to compare performance based on different N sizes
# total number of samples. Your task is to compare on those 5 or more N values
# N = {10, 100, 1_000, 10_000, 100_000, 300_000 ... (You need to get some coffee to wait, :-))}

N = 10
item_list = [] # empty list for zip codes

Faker.seed(0)
fake = Faker()
# store random zip codes
for i in range(0, N):
        item_list.append(fake.zipcode())

def main():

        print("------ Linked list ------")
        ll = LinkedListZipListManagerClass()
        
        #insert operation
        for i in range(len(item_list)):
                ll.insert_item(item_list[i])
        print("Current list:\t", end = " ")
        ll.print_items()

        #sort operation
        linked_list_sort_start_time = time.perf_counter()
        ll.quick_sort()
        linked_list_sort_end_time = time.perf_counter()
        print("Sorted(a to z):\t", end = " ")
        ll.print_items()
        
        #time summary:
        llSortOp= linked_list_sort_end_time - linked_list_sort_start_time
        print("-sort: %s" %(llSortOp))

if __name__ == "__main__":
        main()

