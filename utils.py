import os
import importlib.util
from datetime import date

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.join(BASE_DIR, "modules")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
DEFAULTS_DIR = os.path.join(BASE_DIR, "defaults")

# ---------------- MODULE LOADER ----------------
def load_python_module(path):
    spec = importlib.util.spec_from_file_location("mod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# ---------------- PLACEHOLDER REPLACER ----------------
def replace_placeholders(doc, data):
    def replace_in_paragraph(paragraph):
        if not paragraph.runs:
            return

        full_text = "".join(run.text for run in paragraph.runs)
        new_text = full_text

        for k, v in data.items():
            new_text = new_text.replace(f"{{{{{k}}}}}", v)

        # No change → do nothing
        if new_text == full_text:
            return

        # Clear run texts ONLY (not runs themselves)
        for run in paragraph.runs:
            run.text = ""

        # Put replaced text into the FIRST run
        paragraph.runs[0].text = new_text

    # Normal paragraphs
    for p in doc.paragraphs:
        replace_in_paragraph(p)

    # Tables
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    replace_in_paragraph(p)


# ---------------- LOADERS ----------------
def load_states():
    return sorted(
        d for d in os.listdir(MODULES_DIR)
        if os.path.isdir(os.path.join(MODULES_DIR, d))
    )

def load_courts(state):
    base = os.path.join(MODULES_DIR, state)
    return sorted(
        d for d in os.listdir(base)
        if os.path.isdir(os.path.join(base, d))
    ) if os.path.isdir(base) else []

def load_cases(state, court):
    base = os.path.join(MODULES_DIR, state, court)
    return sorted(
        f[:-3] for f in os.listdir(base)
        if f.endswith(".py")
    ) if os.path.isdir(base) else []

# ---------------- BENCH / COURT ----------------
def load_benches(state, court):
    profile = load_court_profile(state, court)
    if profile and "benches" in profile:
        return [b.strip() for b in profile["benches"].split(",")]
    return []

def load_court_profile(state, court):
    fname = f"{state}_{court}.txt".replace(" ", "_")
    path = os.path.join(DEFAULTS_DIR, "courts", fname)
    if not os.path.exists(path):
        return None

    profile = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                profile[k.strip()] = v.strip()
    return profile

def get_court_name_for_bench(state, court, bench):
    fname = f"{state}_{court}_{bench}.txt".replace(" ", "_")
    path = os.path.join(DEFAULTS_DIR, "courts", fname)
    if not os.path.exists(path):
        return ""

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("court_name="):
                return line.split("=", 1)[1].strip()
    return ""
