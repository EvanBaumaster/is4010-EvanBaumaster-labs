import re
from typing import List

_EMAIL_RE = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

def calculate_average_age(users):
    """
    Calculate the average age of users with valid age data.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries, each containing an 'age' key.
        Only users with integer ages are included in the calculation.

    Returns
    -------
    float
        Average age of users with valid (integer) age values.
        Returns 0.0 if no valid ages are found.

    Examples
    --------
    >>> users = [{"age": 30}, {"age": 25}, {"age": 35}]
    >>> calculate_average_age(users)
    30.0
    """
    if not isinstance(users, list):
        raise TypeError(f"Expected list, got {type(users).__name__}")
    if not users:
        raise ValueError("users list cannot be empty")
    
    # Add age validation
    valid_ages = [user["age"] for user in users 
                  if isinstance(user, dict) and isinstance(user.get("age"), int) and 0 <= user["age"] <= 150]
    
    if not valid_ages:
        return 0.0
    
    return sum(valid_ages) / len(valid_ages)


def get_active_user_emails(users, *, deduplicate: bool = True, validate: bool = False) -> List[str]:
    """
    Extract email addresses of all active users.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries, each containing 'is_active' and
        'email' keys. Only active users with non-null emails are included.

    Returns
    -------
    list of str
        Email addresses of active users. Returns empty list if no
        active users with emails are found.

    Examples
    --------
    >>> users = [
    ...     {"is_active": True, "email": "alice@example.com"},
    ...     {"is_active": False, "email": "bob@example.com"}
    ... ]
    >>> get_active_user_emails(users)
    ['alice@example.com']
    """
    if not isinstance(users, list):
        raise TypeError("users must be a list")
    emails = []
    seen = set()
    for item in users:
        if not isinstance(item, dict):
            continue
        if item.get("is_active") is not True:
            continue
        email = item.get("email")
        if not isinstance(email, str) or not email.strip():
            continue
        email = email.strip()
        if validate and not _EMAIL_RE.match(email):
            continue
        if deduplicate:
            if email in seen:
                continue
            seen.add(email)
        emails.append(email)
    return emails


# Main execution
users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]
if __name__ == "__main__":
    average_age = calculate_average_age(users)
    print(f"average user age: {average_age:.2f}")

    active_user_emails = get_active_user_emails(users)
    print(f"active user emails: {active_user_emails}")