from hashlib import sha256

# This project won't include a database, let's just pretend that hash set is blasingly fast in-memory database
authorized_users = set()

# This one is bad too
PASSWORD = "The most secure password ever!!!11!1"

def is_authorized(user_id: int):
    return user_id in authorized_users

def authorize(user_id: int, password: str) -> bool:
    if password != PASSWORD:
        return False
    
    authorized_users.add(user_id)
    return True