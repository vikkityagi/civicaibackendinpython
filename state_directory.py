# state_directory.py

STATE_DEPARTMENTS = {
    "UP": {
        # State-level default contacts
        "Electricity": {
            "contact": "1912",
            "timing": "9 AM - 6 PM",
            "info": "शक्ति भवन 14 अशोक मार्ग\nलखनऊ\n0522 2287525",
            "portal": "https://uppcl.org",
        },
        "Water": {
            "contact": "1800-180-5555",
            "info": "6, Rana Pratap Marg\nLucknow - 226001 U.P.(INDIA)\nPhone No. : (0522) 2620172, 2620272",
            "timing": "10 AM - 5 PM",
            "portal": "https://jn.upsdc.gov.in/",
        },
        "Road": {
            "contact": "0522-4150377 / info@upsha.in",
            "info": "4th Floor, Mandi Bhawan\nVibhuti Khand, Gomti Nagar\nLucknow (U.P.)\nPIN : 226010, India",
            "timing": "9 AM - 5 PM",
            "portal": "https://upsha.in/",
        },
        # District / city specific overrides
        "districts": {
            "Lucknow": {
                "Water": {
                    "contact": "1800-180-5555",
                    "info": "Jal Nigam, Lucknow (District level office)",
                    "timing": "10 AM - 5 PM",
                    "portal": "https://jn.upsdc.gov.in/",
                }
            },
            "Kanpur": {
                "Water": {
                    "contact": "0512-2540410",
                    "info": "Jal Kal Vibhag, Kanpur Nagar Nigam",
                    "timing": "10 AM - 5 PM",
                    "portal": "https://kmc.up.nic.in/",
                }
            },
        },
    },

    # ✅ Bihar
    "Bihar": {
        "Electricity": {
            "contact": "1912 / 18002022813",
            "info": (
                "NBPDCL Vigilance Cell, HelpLine 0612-2504745, Email Id:- nbpdclgmhr@gmail.com\n"
                "NBPDCL Departmental Grievance Redressal Cell, Telephone No. 0612-2504745, "
                "Email Id:- dgrcell@nbpdcl.co.in"
            ),
            "timing": "9 AM - 6 PM",
            "portal": "https://www.nbpdcl.co.in",
        },
        "Water": {
            "contact": "0612-2222079 / 2217696",
            "info": "1st Floor, Sinchai Bhawan, Old Secreatariat, Patna, Bihar\n800014\nGovernment of Bihar",
            "timing": "10 AM - 5 PM",
            "portal": "https://betastate.bihar.gov.in/wrd/",
        },
        "Road": {
            "contact": "0612-2233333",
            "info": "Bihar State Road Development Corporation Limited (BSRDC), Patna-800001, Bihar, India",
            "timing": "9 AM - 5 PM",
            "portal": "https://state.bihar.gov.in/rcd",
        },
        "districts": {
            "Patna": {
                "Water": {
                    "contact": "0612-2222079",
                    "info": "Patna Jal Parishad, Patna",
                    "timing": "10 AM - 5 PM",
                    "portal": "https://patna.nic.in/",
                }
            }
        },
    },
}
