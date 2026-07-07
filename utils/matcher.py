from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(
    resume_embedding,
    jd_embedding
):

    score = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return round(score * 100, 2)