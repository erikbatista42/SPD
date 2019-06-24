def latest(scores):
    return scores[-1]


def personal_best(scores):
    sorted_scores = sorted(scores)
    return sorted_scores[-1]


def personal_top_three(scores):
    sorted_scores_list = sorted(list(scores))
    
    if len(sorted_scores_list) < 3:
        return sorted_scores_list[::-1]
    else:
        return [sorted_scores_list[-1], sorted_scores_list[-2], sorted_scores_list[-3]] # list of top three scores
