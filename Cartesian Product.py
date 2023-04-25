from itertools import product

# Create an empty list
my_list1 = []
my_list2 = []

# Define functions
def list1():
    # Ask for the user's input
    for i in range(5):
        values_list1 = int(input("Please enter an integer number: "))
        my_list1.append(values_list1)
    print("List 1: ", my_list1)
    return my_list1

def list2():
    # Ask for the user's input
    for i in range(5):
        values_list2 = int(input("Please enter an integer number: "))
        my_list2.append(values_list2)
    print("List 2: ", my_list2)
    return my_list2

def reverse_list(my_list1, my_list2):
    # Compute the Cartesian product
    product_list = list(product(my_list1, my_list2))
    print("The Cartesian product output: ", product_list)
    

def main():
    # Call the functions
    list1()
    list2()
    reverse_list(my_list1, my_list2)
    
        
if __name__ == "__main__":
    main()