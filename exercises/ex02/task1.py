from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# Initialize the engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# Our target text
private_text = "Hi, my name is John Wick and you can reach me at john.wick@continental.com or 555-0199."

# Analyze the text to find PII
results = analyzer.analyze(text=private_text, language='en')
print(results)

# Anonymize the identified PII
anonymized_text = anonymizer.anonymize(text=private_text, analyzer_results=results)

print(f"Original: {private_text}")
print(f"Anonymized: {anonymized_text.text}")
