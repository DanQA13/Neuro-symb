from pyDatalog import pyDatalog

# Define terms for pyDatalog
pyDatalog.create_terms('risk_clause')

# Function to check if text contains a high-risk clause
def check_risk_clause(text):
    # Convert text to lowercase for case-insensitive search
    text_lower = text.lower()
    
    # List of high-risk terms or patterns to flag
    high_risk_terms = [
        "aggravated assault", "battery", "assault", "weapon", "firearm",
        "drug-related", "possession of controlled substance", "cocaine",
        "intent to distribute", "domestic violence", "child abuse", "violation of probation"
    ]
    
    # Check if any high-risk term is present in the text
    for term in high_risk_terms:
        if term in text_lower:
            return f"High-risk clause detected: {term}"
    
    return "No high-risk clause detected"



