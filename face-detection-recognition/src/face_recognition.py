import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def load_face_embeddings(embedding_path):
    # Load face embeddings from a file
    try:
        data = np.load(embedding_path)
        return data['embeddings'], data['names']
    except Exception as e:
        print(f"Error loading embeddings: {e}")
        return None, None

def recognize_faces(embeddings, known_face_encodings, known_face_names):
    # Recognize faces based on embeddings
    recognized_names = []
    for embedding in embeddings:
        similarities = cosine_similarity([embedding], known_face_encodings)
        best_match_index = np.argmax(similarities)
        recognized_names.append(known_face_names[best_match_index] if similarities[0][best_match_index] > 0.5 else "Unknown")
    
    return recognized_names

def save_face_embeddings(embeddings, names, output_path):
    # Save face embeddings to a file
    try:
        np.savez(output_path, embeddings=embeddings, names=names)
    except Exception as e:
        print(f"Error saving embeddings: {e}")