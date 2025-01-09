from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec

def extract_tfidf_features(corpus):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    return tfidf_matrix, vectorizer

def extract_word_embeddings(corpus):
    tokenized_corpus = [doc.split() for doc in corpus]
    model = Word2Vec(tokenized_corpus, vector_size=100, window=5, min_count=1, workers=4)
    return model

def get_feature_vectors(corpus, method='tfidf'):
    if method == 'tfidf':
        return extract_tfidf_features(corpus)
    elif method == 'word2vec':
        return extract_word_embeddings(corpus)
    else:
        raise ValueError("Unsupported feature extraction method: {}".format(method))