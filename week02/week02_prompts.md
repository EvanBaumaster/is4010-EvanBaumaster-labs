# Problem 1
## Original Prompt:

#### Debugging a buggy function

This function is supposed to calculate the sum of all **even** numbers in a list, but it contains a logical error.

**Your task**: Craft a prompt that asks the AI to find and fix the bug.

**Buggy code**:
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total

## My Prompt
"""I need you to find and correct the bug or bugs in this python prompt: def sum_of_evens(numbers):
    Calculate the sum of all even numbers in a list.
    '''
    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    '''
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total
"""

#### AI's Response:
"""The bug is on this line:
(27)
The condition checks if num % 2 == 1 (odd numbers), but the function should sum even numbers. It should be num % 2 == 0:"""

## Corrected Function:
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0: 
            total += num
    return total



# Problem 2
## Original Prompt
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results

## My Prompt:
"""I need you to make the following code to be more clear, concise, and idiomatic: def get_names_of_adults(users):
    '''Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    '''
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
"""