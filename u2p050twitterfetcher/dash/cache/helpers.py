from flask import session

def get_session_key(key):
    session_id = session.sid
    return f"{session_id}_{key}"

def store_data_frame(cache, key, data_frame):
    session_key = get_session_key(key)
    cache.set(session_key, data_frame)

def load_data_frame(cache, key):
    session_key = get_session_key(key)
    value = cache.get(session_key)
    if value is None:
        raise Exception(f"{key} not found in cache")
    return value
