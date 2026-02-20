def detect_intent(text: str):
    text_lower = text.lower()
    
    # ----------------------------
    # 🤖 SELF / INTRO
    # ----------------------------
    if any(w in text_lower for w in [
        "kisne banaya",
        "tumhe kisne banaya",
        "aapko kisne banaya",
        "banaya kisne",
        "who created you",
        "who made you",
        "who make you",
        "who is your creator",
        "who is your maker",
        "who is your developer"
        
    ]):
        return "MADE", None

    # ----------------------------
    # 🤖 SELF / INTRO
    # ----------------------------
    if any(w in text_lower for w in [
        "tum kaun", "aap kaun", "who are you", "introduce yourself", "apne baare mein batao","tell something about yourself","tell me about yourself",
    ]):
        return "SELF", None

    # ----------------------------
    # 🏛️ COMPLAINT + DEPARTMENT DETECTION
    # ----------------------------

    # ⚡ Electricity
    if any(w in text_lower for w in [
        "bijli", "light nahi", "current nahi", "power cut", "electricity", "bijli chali","bijli nhi aa rhi", "light chali", "current chala", "power chala","light","light ki problem"
    ]):
        return "COMPLAINT", "Electricity"

    # 💧 Water
    if any(w in text_lower for w in [
        "pani", "nal band", "ganda pani", "water"
    ]):
        return "COMPLAINT", "Water"

    # 🛣 Road
    if any(w in text_lower for w in [
        "road kharab", "sadak kharab", "gaddha", "khadde", "road ki problem",
    ]):
        return "COMPLAINT", "Road"

    # ----------------------------
    # ℹ️ INFO / OBSERVATION
    # ----------------------------
    if any(w in text_lower for w in [
        "thanda", "garam", "pressure", "slow", "normal"
    ]):
        return "INFO", None

    # ----------------------------
    # 🎓 EDUCATION
    # ----------------------------
    if any(w in text_lower for w in [
        "kaise sikhe", "kaise kare", "tutorial", "guide", "career", "course"
    ]):
        return "EDUCATION", None

    # ----------------------------
    # 📚 GENERAL KNOWLEDGE
    # ----------------------------
    if any(w in text_lower for w in [
        "what is", "who is", "capital", "define", "meaning", "information about", "ka hai",
        "kaun hai", "kya hai", "ka matlab", "batao", "jankari", "kab", "kaise", "kyun", "kaun", "kya","where","when","why","how","kha","location","time","date"
    ]):
        return "GENERAL_KNOWLEDGE", None

    # ----------------------------
    # 👋 GREETING
    # ----------------------------
    if any(w in text_lower for w in [
        "hi", "hello", "namaste", "hey"
    ]):
        return "GREETING", None

    return "OUT_OF_SCOPE", None
