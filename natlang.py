from google.cloud import language

def language_analysis(text):
    clinet = language.Client()
    document = client.document_from_text(text)
    sent_analysis = document.analyze_sentiment()
    print(dir(sent_analysis))
    sentiment = sent_analysis.sentiment
    ent_analysis = document.analyze_entities()
    entitites = ent_analysis.entities 
    return sentiment, entities 

sample_text = 'It hasn\'t rained for three months. The trees are prospecting underground, sending reserves of roots into the dry ground, roots like razors open to any artery of water-fat.'

sentiment, entities = language_analysis(example_text)
print(sentiment.score, sentiment.magnitude)

for e in entities:
    print(e.name, e.entity_type, e.metadata, e.salience)

    