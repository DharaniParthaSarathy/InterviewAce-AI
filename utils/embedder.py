from sentence_transformers import SentenceTransformer

# Load embedding model only once
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def get_embedding(text):
    """
    Generate embedding for a single text.
    """

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding


def get_embeddings(chunks):
    """
    Generate embeddings for multiple chunks.
    """

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings