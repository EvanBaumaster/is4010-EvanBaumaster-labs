# Problem 1
 ## Prompt for AI
 Can you tell me which python data structure would be best for the following problem, then can you write the code for the function: 
 def find_common_elements(list1, list2):
    """Find the common elements between two lists.

    This function should take two lists and return a new list containing
    only the elements that are present in both input lists. The final
    list can be in any order.

    Parameters
    
    list1 : list
        The first list of elements.
    list2 : list
        The second list of elements.

    Returns
    
    list
        A list of elements common to both list1 and list2.
    """
    pass

 ## AI's Response
 Best Data Structure: Sets

    For this problem, sets are the optimal choice. Here's why:

    Fast lookup: Sets have O(1) average lookup time vs O(n) for lists
    Built-in intersection: Python sets support the & operator for efficient intersection
    Automatic deduplication: Removes duplicates automatically
    Time complexity: O(n + m) instead of O(n × m) for nested loops
    Implementation:
    def find_common_elements(list1, list2):
        """Find the common elements between two lists.

        This function should take two lists and return a new list containing
        only the elements that are present in both input lists. The final
        list can be in any order.

        Parameters
        ----------
        list1 : list
           The first list of elements.
        list2 : list
            The second list of elements.

        Returns
        -------
        ist
            A list of elements common to both list1 and list2.
        """
        return list(set(list1) & set(list2))

    How it works:

    set(list1) converts list1 to a set
    set(list1) & set(list2) finds the intersection (common elements)
    list(...) converts the result back to a list
    Example:
    find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])  # Returns [3, 4] or [4, 3]

    Alternative (more explicit):
    return list(set(list1).intersection(set(list2)))

    Both are equally efficient; the & operator is just more concise.
# Problem 2
 ## Prompt for AI
 Can you tell me which python data structure would be best for the following problem, then can you write the code for the function:
 def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data.

    Parameters
    
    users : list of dict
        A list of dictionaries, where each dictionary represents a user
        and has 'name', 'age', and 'email' keys. It is recommended to
        convert this list into a more efficient data structure for lookups.
    name : str
        The name of the user to find.

    Returns
    
    dict or None
        The dictionary of the found user, or None if no user is found.
    """
    pass

 ## AI's Response
 Best Data Structure: Dictionary
 For this problem, a dictionary is optimal. Here's why:
 O(1) lookup: Dictionary key lookup is constant time vs O(n) for list iteration
 Direct mapping: Store users by name as key for instant retrieval
 Handles None case naturally: Dictionary .get() returns None if key doesn't exist
 One-time conversion cost: Convert list to dict once, then all lookups are fast
 Implementation:
 def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data.

    Parameters
    
    users : list of dict
        A list of dictionaries, where each dictionary represents a user
        and has 'name', 'age', and 'email' keys. It is recommended to
        convert this list into a more efficient data structure for lookups.
    name : str
        The name of the user to find.

    Returns
    
    dict or None
        The dictionary of the found user, or None if no user is found.
    """
    user_dict = {user['name']: user for user in users}
    return user_dict.get(name)
 How it works:
 {user['name']: user for user in users} creates a dictionary with names as keys
 user_dict.get(name) looks up the name and returns the user dict or None
 Example:
 users = [
    {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'},
    {'name': 'Bob', 'age': 25, 'email': 'bob@example.com'}
 ]
 find_user_by_name(users, 'Alice')  # Returns {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}
 find_user_by_name(users, 'Charlie')  # Returns None
 Alternative (if list is only used once):
 return next((user for user in users if user['name'] == name), None)
 Use this if the function is called infrequently, as it avoids the conversion overhead.
# Problem 3
 ## Prompt for AI
 Can you tell me which python data structure would be best for the following problem, then can you write the code for the function:
 def get_list_of_even_numbers(numbers):
    """Return a new list containing only the even numbers from the input list.

    The order of the numbers in the output list must be the same as the
    order of the even numbers in the input list.

    Parameters
    
    numbers : list of int
        A list of integers.

    Returns
    
    list of int
        A new list containing only the even integers from the input list.
    """
    pass

 ## AI's Response
 Best Data Structure: List

    For this problem, a list is the ideal choice. Here's why:

    Order preservation: Lists maintain insertion order (required by the problem)
    Natural filtering: Lists are designed for sequential data processing
    List comprehension: Python's list comprehension is efficient and readable for filtering
    Simple and clean: No conversion overhead needed
    Implementation:
    def get_list_of_even_numbers(numbers):
    """Return a new list containing only the even numbers from the input list.

    The order of the numbers in the output list must be the same as the
    order of the even numbers in the input list.

    Parameters
    
    numbers : list of int
        A list of integers.

    Returns
    
    list of int
        A new list containing only the even integers from the input list.
    """
    return [num for num in numbers if num % 2 == 0]
    How it works:

    for num in numbers iterates through each number in order
    if num % 2 == 0 checks if the number is even (remainder 0 when divided by 2)
    Only even numbers are added to the new list
    Order is automatically preserved
    Example:
    get_list_of_even_numbers([1, 2, 3, 4, 5, 6])  # Returns [2, 4, 6]
    get_list_of_even_numbers([10, 15, 20, 25])     # Returns [10, 20]
    get_list_of_even_numbers([1, 3, 5, 7])         # Returns []

    Alternative (using filter()):
    return list(filter(lambda num: num % 2 == 0, numbers))

    This is more functional but less readable. List comprehension is preferred in Python.