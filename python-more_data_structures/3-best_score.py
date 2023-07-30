def best_score(a_dictionary):
    if not a_dictionary:
        return None
    bestScore = 0
    bestScore_key = ""
    for key, value in a_dictionary.items():
        if value > bestScore:
            bestScore = value
            bestScore_key = key
    return bestScore_key
