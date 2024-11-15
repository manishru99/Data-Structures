
def insert_at_start(arr, e):
    arr.insert(0,e)

def insert_at_end(arr, element):
    arr.append(element)

def insert_at_middle(arr, element):
    middle_index = len(arr) // 2
    arr.insert(middle_index, element)

def insert_at_position(arr, position, element):
    if 0 <= position <= len(arr):
        arr.insert(position, element)
    else:
        print("Invalid position! Please enter a position between 1 and ", len(arr))

def delete_from_start(arr):
    if arr:
        return arr.pop(0)
    else:
        return None

def delete_from_end(arr):
    if arr:
        return arr.pop()
    else:
        return None

def delete_from_middle(arr):
    if arr:
        middle_index = len(arr) // 2
        return arr.pop(middle_index)
    else:
        return None

def search_element(arr, element):
    for index, value in enumerate(arr):
        if value == element:
            return index
    return -1

def insert_in_sorted_order(arr, element):
    if not arr or element >= arr[-1]:
        arr.append(element)
    else:
        for i in range(len(arr)):
            if arr[i] >= element:
                arr.insert(i, element)
                break

def binary_search(arr, e):
    left, right = 0, len(arr)-1
    while(left<=right):
        middle = (left+right)//2
        if(arr[middle]==e):
            return middle
        elif(arr[middle]<e):
            left=middle+1
        else:
            right=middle-1
    return -1

def delete_from_position(arr, position):
    if 0 <= position < len(arr):
        return arr.pop(position)
    else:
        print("Invalid position! Please enter a position between 0 and", len(arr) - 1)
        return None



def print_array(arr):
    print("Current array:", arr)

def main():
    arr = []
    while True:
        print("\nChoose an operation:")
        print("1. Insert at start")
        print("2. Insert at end")
        print("3. Insert at middle")
        print("4. Insert at position")
        print("5. Insert in sorted order")
        print("6. Delete from start")
        print("7. Delete from end")
        print("8. Delete from middle")
        print("9. Delete from position")
        print("10. Search element (Linear Search)")
        print("11. Search element (Binary Search)")
        print("12. Print array")
        print("13. Exit")

        choice = int(input("Enter your choice (1-13): "))

        if choice == 1:
            element = int(input("Enter the element to insert at start: "))
            insert_at_start(arr, element)
        elif choice == 2:
            element = int(input("Enter the element to insert at end: "))
            insert_at_end(arr, element)
        elif choice == 3:
            element = int(input("Enter the element to insert at middle: "))
            insert_at_middle(arr, element)
        elif choice == 4:
            position = int(input("Enter the position to insert the element: "))
            element = int(input("Enter the element to insert: "))
            insert_at_position(arr, position, element)
        elif choice == 5:
            element = int(input("Enter the element to insert in sorted order: "))
            insert_in_sorted_order(arr, element)
        elif choice == 6:
            deleted_element = delete_from_start(arr)
            if deleted_element is not None:
                print("Deleted element from start:", deleted_element)
            else:
                print("Array is empty, nothing to delete.")
        elif choice == 7:
            deleted_element = delete_from_end(arr)
            if deleted_element is not None:
                print("Deleted element from end:", deleted_element)
            else:
                print("Array is empty, nothing to delete.")
        elif choice == 8:
            deleted_element = delete_from_middle(arr)
            if deleted_element is not None:
                print("Deleted element from middle:", deleted_element)
            else:
                print("Array is empty, nothing to delete.")
        elif choice == 9:
            position = int(input("Enter the position to delete the element from: "))
            deleted_element = delete_from_position(arr, position)
            if deleted_element is not None:
                print("Deleted element from position", position, ":", deleted_element)
        elif choice == 10:
            element = int(input("Enter the element to search: "))
            index = search_element(arr, element)
            if index != -1:
                print(f"Element {element} found at index {index}.")
            else:
                print(f"Element {element} not found in the array.")
        elif choice == 11:
            element = int(input("Enter the element to search: "))
            index = binary_search(arr, element)
            if index != -1:
                print(f"Element {element} found at index {index}.")
            else:
                print(f"Element {element} not found in the array.")
        elif choice == 12:
            print_array(arr)
        elif choice == 13:
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()