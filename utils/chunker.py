def chunk_text(
    text,
    chunk_size=400,
    overlap=50
):
    """
    Split text into overlapping chunks.

    Parameters
    ----------
    text : str
        Input text.

    chunk_size : int
        Number of words per chunk.

    overlap : int
        Number of overlapping words.

    Returns
    -------
    list
        List of text chunks.
    """

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(
            words[start:end]
        )

        chunks.append(chunk)

        start += (
            chunk_size - overlap
        )

    return chunks