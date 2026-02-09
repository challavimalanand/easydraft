# ============================================================
# EasyDraft Module
# High Court – Telangana
# Criminal Petition (Crl.P.) – Sec. 528 BNSS
# ============================================================

MODULE_NAME = "High Court – Telangana – Criminal Petition (Crl.P.) Quash"

TEMPLATE_FILE = "quash.docx"

# modules/telangana/high_court/quash.py

FIELDS = [
    ("court_name", "Court Name"),
    ("place", "Place"),
    # --------------------------------------------------------
    # Filing & Case Details
    # --------------------------------------------------------
    ("year", "Year"),
    ("dof", "Date of Filing"),

    

    ("case_no", "Lower Court Case Number"),
    ("lower_court_name", "Lower Court Name"),
    ("lcod", "Lower Court Order Date"),

    ("district", "District"),



    # --------------------------------------------------------
    # Party Details
    # --------------------------------------------------------
    ("pet_name", "Petitioner Name (Short Cause Title)"),
    ("res_name", "Respondent Name (Short Cause Title)"),

    ("petitioner", "Petitioner / Accused (Full Description)"),
    ("respondent", "Respondent (Full Description)"),

    # --------------------------------------------------------
    # Advocate & Address Details
    # --------------------------------------------------------
    ("adv_name", "Advocate Name"),
    ("summons_address", "Address for Service / Counsel Address"),
    ("address_for_service", "Address for Service (Vakalat)"),

    # --------------------------------------------------------
    # Affidavit / Vakalat
    # --------------------------------------------------------
    ("aff_oath", "Name of Deponent (Affidavit Oath)"),

    # --------------------------------------------------------
    # Prayers
    # --------------------------------------------------------
    ("main_prayer", "Main Prayer (Quash Relief)"),
    ("interim_prayer", "Interim / Stay / Dispense Prayer"),
]
