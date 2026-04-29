def score(row):
    score = 0
    if row["%Away"] >= -5:
        score += 3
    if row["Volume Spike"]:
        score += 3
    if row["%Away"] >= -2:
        score += 2
    return score

def rank(df):
    df["Score"] = df.apply(score, axis=1)
    return df.sort_values(by="Score", ascending=False)
