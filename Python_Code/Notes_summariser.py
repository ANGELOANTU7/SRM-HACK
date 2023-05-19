from gensim import corpora, models
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Read the class notes from the text file
with open('Files\\notes_txt\module1.txt', 'r',encoding='utf-8') as file:
    notes = file.read()

# Preprocess the text (example: tokenization)
preprocessed_docs = [note.split() for note in notes.split('\n')]

# Create a dictionary from the preprocessed documents
dictionary = corpora.Dictionary(preprocessed_docs)

# Convert the documents to a bag-of-words (BoW) representation
bow_corpus = [dictionary.doc2bow(doc) for doc in preprocessed_docs]

# Train the LDA model on the BoW corpus
lda_model = models.LdaModel(bow_corpus, num_topics=10, id2word=dictionary, passes=10)

# Get the topics and their top words
topics = lda_model.print_topics(num_words=5)
for topic in topics:
    print(topic)

# Summarize the class notes using LexRank algorithm from sumy
parser = PlaintextParser.from_string(notes, Tokenizer("english"))
summarizer = LexRankSummarizer()
summary = summarizer(parser.document, 2)  # Number of sentences in the summary
print("\nSummary:")
for sentence in summary:
    print(sentence)
