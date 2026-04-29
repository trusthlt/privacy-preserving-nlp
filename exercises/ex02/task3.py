from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern, RecognizerRegistry
from presidio_analyzer.nlp_engine import NlpEngineProvider
from presidio_analyzer.predefined_recognizers import SpacyRecognizer
from presidio_anonymizer import AnonymizerEngine

configuration = {
    "nlp_engine_name": "spacy",
    "models": [
        {"lang_code": "de", "model_name": "de_core_news_sm"}
    ],
}
provider = NlpEngineProvider(nlp_configuration=configuration)
nlp_engine = provider.create_engine()


# Registry
registry = RecognizerRegistry()
# Load ALL defaults (not just "de") to ensure basic PII coverage
registry.load_predefined_recognizers()
# IMPORTANT: Add the SpacyRecognizer for German.
# This allows Presidio to use the German NLP model to find NAMES and LOCATIONS.
german_spacy_recognizer = SpacyRecognizer(supported_language="de")
registry.add_recognizer(german_spacy_recognizer)


# Custom patterns
full_date_pattern = Pattern(
    name="german_full_date",
    regex=r"TODO",
    score=0.8
)

year_pattern = Pattern(
    name="year_only",
    regex=r"TODO",
    score=0.4
)

# Custom recognizer
german_date_recognizer = PatternRecognizer(
    supported_entity="DATE_TIME",
    patterns=[full_date_pattern, year_pattern],
    supported_language="de",
)

# need to add our custom recognizer
registry.add_recognizer(german_date_recognizer)

# Init engines
analyzer = AnalyzerEngine(nlp_engine=nlp_engine, registry=registry)

# Our target text
private_text = "Die Familie zog kurz nach der Geburt Alberts 1880 nach München, wo sein Vater und sein Onkel im Oktober 1880 einen kleinen Betrieb zur Gas- und Wasserinstallation gründeten. Da dieser wirtschaftlich zufriedenstellend lief, beschlossen sie 1885 und mit Unterstützung der gesamten Familie, eine eigene Fabrik für elektrische Geräte (Elektrotechnische Fabrik J. Einstein & Cie) ins Leben zu rufen. Das Unternehmen seines Vaters war erfolgreich und belieferte Kraftwerke in München-Schwabing, Varese und Susa (Italien). Zweieinhalb Jahre nach Albert wurde seine Schwester Maja (* 18. November 1881 in München; † 25. Juni 1951 in Princeton, New Jersey, USA) geboren. Die Familie wohnte im Münchener Stadtteil Isarvorstadt, zunächst von 1880 bis 1885 in einer Wohnung an der heutigen Müllerstraße 54, ab 1885 auf dem Grundstück, das sich heute zwischen Adlzreiterstraße 12 und Lindwurmstraße 127 erstreckt. "

results = analyzer.analyze(text=private_text, entities=None, language='de')
print(results)

# 4. Anonymize the identified PII
anonymizer = AnonymizerEngine()
anonymized_text = anonymizer.anonymize(text=private_text, analyzer_results=results)

print(f"Original: {private_text}")
print(f"Anonymized: {anonymized_text.text}")
