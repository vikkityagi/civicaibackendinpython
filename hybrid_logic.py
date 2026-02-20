from intent_detector import detect_intent
from entity_extractor import extract_entities
from memory_store import get_user_memory, update_user_memory
from state_directory import STATE_DEPARTMENTS

LANGUAGE_WORDS = {
    "hi": ["hindi", "हिंदी"],
    "en": ["english"]
}

TIME_WORDS = ["abhi", "subah", "aaj", "kal", "roz", "raat"]
YES_WORDS = ["haan", "ha", "yes", "hanji", "hmm"]
NO_WORDS = ["nahi", "no", "na"]

ISSUE_TIPS = {
        "Electricity": [
            "Neighbour se confirm karein",
            "MCB / main switch check karein",
            "1–2 ghante wait karein"
        ],

        "Water": [
            "Paani supply timing check karein",
            "Tank / motor check karein",
            "Nearby area me bhi problem hai kya confirm karein"
        ],

        "Road": [
            "Location photo lekar complaint register karein",
            "Nearby PWD office me report karein",
            "Online portal par issue submit karein"
        ]
    }






def hybrid_decision(predicted_category: str, text: str, user_id: str):

    text_lower = text.lower().strip()
    intent, _ = detect_intent(text)
    entities = extract_entities(text)
    memory = get_user_memory(user_id)

    # =====================================================
    # 🔥 GLOBAL INTENT HANDLING (ALWAYS FIRST)
    # =====================================================
    # These should trigger regardless of current stage

    # SELF intro
    if intent == "SELF":
        memory.clear()
        return {
            "message": "Main Civic Support AI hoon 🤖. Main bijli, pani, road complaint me help karta hoon."
        }

    # MADE intent
    if intent == "MADE":
        memory.clear()
        return {
            "message": "Mujhe NIC ke ek contractual employee ne banaya hai jinka naam Vikki Tyagi hai 🙂"
        }

    if intent == "OUT_OF_SCOPE" and not memory.get("stage"):
        return {
            "message": "Mujhe sirf bijli, pani ya road complaint me help karne ke liye banaya gaya hai 🙂"
        }

    # =====================================================
    # 🌍 STAGE 0: LANGUAGE SELECTION (FIRST STEP)
    # =====================================================
    if memory.get("stage") == "LANGUAGE_SELECTION":

        # Hindi selected
        if any(w in text_lower for w in LANGUAGE_WORDS["hi"]):
            update_user_memory(user_id, "language", "hi")
            update_user_memory(user_id, "stage", "GREETING")

            return {
                "message": "Namaste 👋 Main Civic Support AI hoon.\nAapko kis problem me help chahiye? (bijli / pani / road)"
            }

        # English selected
        if any(w in text_lower for w in LANGUAGE_WORDS["en"]):
            update_user_memory(user_id, "language", "en")
            update_user_memory(user_id, "stage", "GREETING")

            return {
                "message": "Hello 👋 I am Civic Support AI.\nHow may I help you? (electricity / water / road)"
            }

        # Ask language
        return {
            "message": "Please choose language:\nHindi / English"
        }

    # =====================================================
    # ⚡ NEW ISSUE DETECTION (ONLY IF NO ISSUE YET)
    # =====================================================
    if not memory.get("issue") and entities.get("issue"):
        update_user_memory(user_id, "issue", entities["issue"])
        update_user_memory(user_id, "stage", "ASK_TIME")

        return {
            "message": (
                f"Samajh gaya 👍 Aapko {entities['issue']} ki problem ho rahi hai.\n"
                "Yeh problem kab se hai?\n"
                "(abhi, subah se, ya roz hoti hai?)"
            )
        }
        
    # -----------------------------
    # 👋 GREETING (only if user greets)
    # -----------------------------
    GREETINGS = ["hi", "hello", "namaste", "hey"]

    # -----------------------------
    # 👋 GREETING (language based)
    # -----------------------------
    lang = memory.get("language", "hi")

    if memory.get("stage") == "GREETING" and text_lower in GREETINGS:

        update_user_memory(user_id, "stage", "idle")

        if lang == "hi":
            return {"message": "Namaste 👋 Aap apni problem bata sakte ho 😊"}
        else:
            return {"message": "Hello 👋 You can tell me your problem 😊"}



    # =====================================================
    # 🧠 STAGE 1: ASK_TIME
    # =====================================================
    # =====================================================
# 🧠 STAGE 1: ASK_TIME
# =====================================================
    if memory.get("stage") == "ASK_TIME":

        # ✅ FIRST → expected input (MOST IMPORTANT)
        if any(w in text_lower for w in TIME_WORDS):
            update_user_memory(user_id, "time", text)
            update_user_memory(user_id, "stage", "ASK_STATE")

            return {
                "message": "Apna state ya city batao 😊 (UP / Bihar)"
            }

        # ✅ SECOND → topic change
        intent, _ = detect_intent(text)
        if intent in ["GENERAL_KNOWLEDGE", "EDUCATION"]:
            memory.clear()
            return {
                "message": "Main sirf bijli, pani ya road complaint me help karta hoon 🙂"
            }

        # ✅ LAST → fallback
        return {
            "message": "Kripya bataye problem kab se hai? (abhi / subah se / roz)"
        }



    # =====================================================
    # 🧠 STAGE 2: ASK_STATE
    # =====================================================
    if memory.get("stage") == "ASK_STATE":

        # 1️⃣ expected input → state
        if entities.get("state"):

            state = entities["state"]
            update_user_memory(user_id, "state", state)

            issue = memory.get("issue")
            time = memory.get("time")

            dept = STATE_DEPARTMENTS.get(state, {}).get(issue)

            if dept:

                tips = ISSUE_TIPS.get(issue, [])
                tips_text = "\n".join([f"• {tip}" for tip in tips])

                update_user_memory(user_id, "stage", "ASK_ANOTHER_ISSUE")

                return {
                    "category": issue,
                    "intent": "COMPLAINT_SOLVED",
                    "state": state,
                    "message": (
                        f"{issue.upper()} PROBLEM – {state}\n\n"
                        f"Problem time: {time}\n\n"
                        f"📞 Helpline: {dept['contact']}\n"
                        f"⏰ Timing: {dept['timing']}\n"
                        f"📞 Info: {dept['info']}\n"
                        f"🌐 Portal: {dept['portal']}\n\n"
                        f"Helpful Steps:\n{tips_text}\n\n"
                        "Kya aapko koi aur problem bhi hai? (haan / nahi)"
                    )
                }

            return {"message": "State ke liye department info nahi mila"}

        # fallback
        return {"message": "Apna state ya city batao (UP / Delhi / Bihar)"}





    
    
    # =====================================================
    # 🧠 STAGE: ASK_ANOTHER_ISSUE
    # =====================================================
    if memory.get("stage") == "ASK_ANOTHER_ISSUE":

        if any(w in text_lower for w in YES_WORDS):

            # reset issue flow
            update_user_memory(user_id, "issue", None)
            update_user_memory(user_id, "time", None)
            update_user_memory(user_id, "state", None)
            update_user_memory(user_id, "stage", "idle")

            return {
                "message": "Theek hai 👍 Aap apni problem batao (bijli / pani / road)"
            }

        if any(w in text_lower for w in NO_WORDS):

            # clear memory completely
            memory.clear()

            # next conversation fresh start
            update_user_memory(user_id, "stage", "LANGUAGE_SELECTION")

            return {
                "message": "Dhanyavaad 🙂 Agar future me help chahiye ho to zaroor batana."
            }



    # =====================================================
    # 🧠 STAGE 3: SOLVE
    # =====================================================
    if memory.get("stage") == "SOLVE":
        # check if user reported new issue
        intent, new_issue = detect_intent(text)
        
        # SELF intro
        if intent == "SELF":
            memory.clear()
            return {
                "message": "Main Civic Support AI hoon 🤖. Main bijli, pani, road complaint me help karta hoon."
            }

        # MADE intent
        if intent == "MADE":
            memory.clear()
            return {
                "message": "Mujhe NIC ke ek contractual employee ne banaya hai jinka naam Vikki Tyagi hai 🙂"
            }
            
        if intent == "OUT_OF_SCOPE" and not memory.get("stage"):
            return {
                "message": "Mujhe sirf bijli, pani ya road complaint me help karne ke liye banaya gaya hai 🙂"
            }

        


        if intent == "COMPLAINT" and new_issue and new_issue != memory.get("issue"):
            memory["issue"] = new_issue   # update issue
            memory["stage"] = "ASK_TIME"
            return {
                "message": f"Samajh gaya 👍 Aapko {new_issue} ki problem ho rahi hai. Kab se?"
            }
        issue = memory["issue"]
        state = memory["state"]
        time = memory["time"]

        dept = STATE_DEPARTMENTS.get(state, {}).get(issue)

        if dept:

            tips = ISSUE_TIPS.get(issue, [])
            tips_text = "\n".join([f"• {tip}" for tip in tips])

            # ⭐ next stage set karo
            update_user_memory(user_id, "stage", "ASK_ANOTHER_ISSUE")

            return {
                "category": issue,
                "intent": "COMPLAINT_SOLVED",
                "state": state,
                "message": (
                    f"{issue.upper()} PROBLEM – {state}\n\n"
                    f"Problem time: {time}\n\n"
                    f"📞 Helpline: {dept['phone']}\n"
                    f"⏰ Timing: {dept['timing']}\n"
                    f"🌐 Portal: {dept['portal']}\n\n"
                    f"Helpful Steps:\n{tips_text}\n\n"
                    "Kya aapko koi aur problem bhi hai? (haan / nahi)"
                )
            }



    

    # =====================================================
    # ❓ FINAL FALLBACK (ONLY WHEN NO STAGE)
    # =====================================================
    return {
        "message": (
            "Main aapki baat samajhne ki koshish kar raha hoon 😊\n"
            "Thoda clear likho: bijli nahi aa rahi / pani ganda aa raha / road kharab hai."
        )
    }
