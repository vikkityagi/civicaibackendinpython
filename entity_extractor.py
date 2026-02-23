def extract_entities(text: str):

    text_lower = text.lower()
    entities = {}

    # -------------------
    # 🔹 ISSUE DETECTION
    # -------------------

    # Electricity
    if any(word in text_lower for word in [
        "bijli", "light", "current", "power", "electricity", "voltage"
    ]):
        entities["issue"] = "Electricity"

    # Water
    elif any(word in text_lower for word in [
        "pani", "water", "nal", "tap", "ganda pani", "supply"
    ]):
        entities["issue"] = "Water"

    # Road
    elif any(word in text_lower for word in [
        "road", "sadak", "gadda", "kharab road", "pothole", "rasta"
    ]):
        entities["issue"] = "Road"

    # -------------------
    # 🔹 STATE DETECTION
    # -------------------

    if "up" in text_lower or "uttar pradesh" in text_lower:
        entities["state"] = "UP"
    elif "bihar" in text_lower:
        entities["state"] = "Bihar"
    elif "hp" in text_lower or "himachal" in text_lower:
        entities["state"] = "HP"
    elif "delhi" in text_lower:
        entities["state"] = "Delhi"

    # -------------------
    # 🔹 DISTRICT / CITY DETECTION
    # -------------------

    district_keywords = {
        "Lucknow": ["lucknow"],
        "Kanpur": ["kanpur"],
        "Varanasi": ["varanasi", "benaras", "banaras"],
        "Noida": ["noida"],
        "Ghaziabad": ["ghaziabad"],
        "Patna": ["patna"],
        "Gaya": ["gaya"],
    }

    for name, keys in district_keywords.items():
        if any(k in text_lower for k in keys):
            entities["district"] = name
            break

    return entities
