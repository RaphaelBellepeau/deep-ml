import math

def softmax(scores: list[float]) -> list[float]:
    maxi = max(scores)
    S = sum(math.exp(x - maxi) for x in scores)
    return [math.exp(score-maxi)/S for score in scores ]