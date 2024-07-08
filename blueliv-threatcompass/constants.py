"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
MODULES_DICT = {"Hacktivism": "hacktivism", "MobileApps": "mobile_apps", "Credentials": "credentials",
           "DarkWeb": "dark_web", "MediaTracker": "media_tracker", "Malware": "malware",
           "DomainProtection": "domain_protection", "DataLeakage": "data_leakage", "CreditCards": "credit_card"}

set_resource_status_dict = {
    "Positive": "POSITIVE",
    "Negative": "NEGATIVE",
    "Informative": "INFORMATIVE",
    "Not Important": "NOT_IMPORTANT"
}

set_resource_fav_dict = {
    "Not Starred": "NOT_STARRED",
    "User Starred": "USER_STARRED",
    "Group Starred": "GROUP_STARRED",
    "Full Starred": "FULL_STARRED"
}