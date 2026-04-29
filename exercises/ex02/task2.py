from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider

# Define the configuration for the NLP engine
configuration = {
    "nlp_engine_name": "spacy",
    "models": [
        # TODO find models
    ],
}

# Create the NLP engine based on the configuration
provider = NlpEngineProvider(nlp_configuration=configuration)
spacy_nlp_engine = provider.create_engine()

# Pass the custom NLP engine to the AnalyzerEngine
analyzer = AnalyzerEngine(nlp_engine=spacy_nlp_engine)

# Private text
private_text = "Die Familie zog kurz nach der Geburt Alberts 1880 nach München, wo sein Vater und sein Onkel im Oktober 1880 einen kleinen Betrieb zur Gas- und Wasserinstallation gründeten. Da dieser wirtschaftlich zufriedenstellend lief, beschlossen sie 1885 und mit Unterstützung der gesamten Familie, eine eigene Fabrik für elektrische Geräte (Elektrotechnische Fabrik J. Einstein & Cie) ins Leben zu rufen. Das Unternehmen seines Vaters war erfolgreich und belieferte Kraftwerke in München-Schwabing, Varese und Susa (Italien). Zweieinhalb Jahre nach Albert wurde seine Schwester Maja (* 18. November 1881 in München; † 25. Juni 1951 in Princeton, New Jersey, USA) geboren. Die Familie wohnte im Münchener Stadtteil Isarvorstadt, zunächst von 1880 bis 1885 in einer Wohnung an der heutigen Müllerstraße 54, ab 1885 auf dem Grundstück, das sich heute zwischen Adlzreiterstraße 12 und Lindwurmstraße 127 erstreckt."

# Analyze the text to find PII
results = None # TODO finish
print(results)

# Anonymize the identified PII
anonymizer = AnonymizerEngine()
anonymized_text = anonymizer.anonymize(text=private_text, analyzer_results=results)

print(f"Original: {private_text}")
print(f"Anonymized: {anonymized_text.text}")
