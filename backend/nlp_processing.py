from transformers import pipeline
from transformers import pipeline

def perform_ner_on_text(text):
    nlp_pipeline = pipeline("ner", model="dslim/bert-base-NER")
    ner_results = nlp_pipeline(text)
    return ner_results
