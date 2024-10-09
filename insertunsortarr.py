def insertEnd(arr, a):
    arr.append(a)      #TC = O(1)

def insert_at_position(arr, pos, e):
    if(0<= pos <= len(arr)):
        arr.insert(pos, e)
    else:
        print("Invalid position! Please enter a position between 0 and", len(arr))

def insert_at_start(arr, e):
    arr.insert(0, e)

def insert_at_middle(arr, e):
    m_index = len(arr//2)
    arr.insert(m_index, e)

def delete_from_start(arr):
    if arr:
        return arr.pop(0)
    else:
        return None

def delete_from_position(arr, position):
    if 0 <= position < len(arr):
        return arr.pop(position)
    else:
        print("Invalid position! Please enter a position between 0 and", len(arr) - 1)
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
    for index, value in enumerate(arr):    #TC=O(n)
        if value == element:
            return index
    return -1

#array input
if __name__ == '__main__':
    arr = []
    n = int(input("array size:"))
    print("Enter elements:\n")
    for i in range(0,n):         #TC=O(n)
        e = int(input())
        arr.append(e)
    #key = int(input("key:"))

    while True:
        print("\nChoose an operation:")
        print("1. Insert at start")
        print("2. Insert at end")
        print("3. Insert at middle")
        print("4. Insert at position")
        print("5. Delete from start")
        print("6. Delete from end")
        print("7. Delete from middle")
        print("8. Delete from position")
        print("9. Search element")
        print("10. Print array")
        print("11. Exit")

        choice = int(input("Enter your choice (1-11): "))
        if choice == 1:
            element = int(input("Enter the element to insert at start: "))
            insert_at_start(arr, element)
        elif choice == 2:
            element = int(input("Enter the element to insert at end: "))
            insertEnd(arr, element)
        elif choice == 3:
            element = int(input("Enter the element to insert at middle: "))
            insert_at_middle(arr, element)
        elif choice == 4:
            position = int(input("Enter the position to insert the element: "))
            element = int(input("Enter the element to insert: "))
            insert_at_position(arr, position, element)
        elif choice == 5:
            deleted_element = delete_from_start(arr)
            if deleted_element is not None:
                print("Deleted element from start:", deleted_element)
            else:
                print("Array is empty, nothing to delete.")
        elif choice == 6:
            deleted_element = delete_from_end(arr)
            if deleted_element is not None:
                print("Deleted element from end:", deleted_element)
            else:
                print("Array is empty, nothing to delete.")
        elif choice == 7:
            deleted_element = delete_from_middle(arr)
            if deleted_element is not None:
                print("Deleted element from middle:", deleted_element)
            else:
                print("Array is empty, nothing to delete.")
        elif choice == 8:
            position = int(input("Enter the position to delete the element from: "))
            deleted_element = delete_from_position(arr, position)
            if deleted_element is not None:
                print("Deleted element from position", position, ":", deleted_element)
        elif choice == 9:
            element = int(input("Enter the element to search: "))
            index = search_element(arr, element)
            if index != -1:
                print(f"Element {element} found at index {index}.")
            else:
                print(f"Element {element} not found in the array.")
        #elif choice == 10:
        #    print_array(arr)
        elif choice == 11:
            break
        else:
            print("Invalid choice, please try again.")

    
    a = int(input("Enter element to be inserted at end:"))
    insertEnd(arr, n, a)
    print("After inserting at the end:\n")
    print(arr)



    