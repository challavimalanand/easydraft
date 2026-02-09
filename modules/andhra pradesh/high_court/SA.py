# ============================================================
# EasyDraft Module
# High Court – Andhra Pradesh
# Second Appeal (S.A.)
# ============================================================

MODULE_NAME = "High Court – Andhra Pradesh – Second Appeal (S.A.)"

TEMPLATE_FILE = "SA.docx"

# modules/Andhra Pradesh/high_court/second_appeal_sa.py

FIELDS = [
    ("court_name", "Court Name"),
    ("place", "Place"),
    
    ("year", "Year"),
        
    ("pet_name", "Appellant / Petitioner Name"),
    ("res_name", "Respondent Name"),

    ("petitioner", "Petitioner (Full Description)"),
    ("respondent", "Respondent (Full Description)"),

    ("os_case_no", "O.S. Case Number"),
    ("osod", " O.S. Order Date"),
    ("os_court_name", "O.S. Court Name"),


    ("as_case_no", "Case Number"),
    ("asod", "Appeal Suit Order Date"),
    ("as_court_name", "First Appeal Court Name"),

    ("district", "District"),

    ("adv_name", "Advocate Name"),
    ("summons_address", "Summons / Counsel Address"),
    ("address_for_service", "Address for Service"),

    ("aff_oath", "Deponent Name (Affidavit Oath)"),

    ("main_prayer", "Main Prayer"),
    ("interim_prayer", "Interim Prayer"),

    ("dof", "Date of Filing"),
]
