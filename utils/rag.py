from utils.embedder import get_embedding


def retrieve_context(
    query,
    index,
    chunks,
    top_k=3
):
    """
    Retrieve the most relevant chunks
    using FAISS similarity search.
    """

    query_embedding = get_embedding(
        query
    )

    distances, indices = index.search(
        query_embedding.reshape(1, -1),
        top_k
    )

    context = []

    for rank, idx in enumerate(indices[0]):

        if idx == -1:
            continue

        context.append(
            f"""
========== Context {rank+1} ==========

{chunks[idx]}
"""
        )

    return "\n".join(
        context
    )