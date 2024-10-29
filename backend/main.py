from pdf_processing import extract_text_from_pdf
from nlp_processing import perform_ner_on_text
from symbolic_logic import check_risk_clause

def analyze_pdf(file_path):
    # Step 1: Extract text from PDF
    text = extract_text_from_pdf(file_path)
    
    # Step 2: Perform NER on extracted text
    entities = perform_ner_on_text(text)
    
    # Step 3: Apply symbolic reasoning to find risk clauses
    has_risk_clause = check_risk_clause(text)
    
    return {
        "entities": entities,
        "risk_clauses": has_risk_clause
    }

# Placeholder for testing - load a sample PDF and run analysis
if __name__ == "__main__":
    result = analyze_pdf("/Users/danielcornier/Desktop/bookings.pdf")
    print(result)

