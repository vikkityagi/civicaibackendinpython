import uuid
import time

# In-memory store (later DB / Redis)
USER_MEMORY = {}

SESSION_EXPIRY = 24 * 60 * 60   # 24 hours


def create_new_user():
    user_id = str(uuid.uuid4())[:8]   # short unique id
    USER_MEMORY[user_id] = {
        "created_at": time.time(),
        "name": None,
        "state": None
    }
    return user_id


# Simple in-memory store (later DB laga sakte ho)

# memory_store.py

USER_MEMORY = {}

def get_user_memory(user_id: str):
    return USER_MEMORY.get(user_id, {
        "language": None,   # ⭐ add this
        "state": None,
        "issue": None,
        "time": None,
        "stage": "LANGUAGE_SELECTION" # ⭐ start from language
    })

def update_user_memory(user_id: str, key: str, value):
    if user_id not in USER_MEMORY:
        USER_MEMORY[user_id] = {}
    USER_MEMORY[user_id][key] = value
