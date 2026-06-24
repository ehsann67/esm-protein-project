from scipy.spatial.distance import cosine

def stability_score(wt, mut, seq):

    similarity = 1 - cosine(wt, mut)

    aromatic = (
        seq.count("F") +
        seq.count("W") +
        seq.count("Y")
    )

    return similarity + 0.02 * aromatic