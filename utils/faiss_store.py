import faiss
import numpy as np


def create_faiss_index(
    embeddings
):
    """
    Create a FAISS index from embeddings.
    """

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        embeddings
    )

    return index