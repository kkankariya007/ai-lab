from sklearn.feature_extraction.text import CountVectorizer

# define some sample documents
documents = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]

# create a CountVectorizer object
vectorizer = CountVectorizer()

# fit the vectorizer to the documents and transform the documents into vectors
vectors = vectorizer.fit_transform(documents)

# print the vocabulary and the vectors
print("Vocabulary:", vectorizer.vocabulary_)
print("Vectors:\n", vectors.toarray())