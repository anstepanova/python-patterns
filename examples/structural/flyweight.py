import weakref


class Score:
    _scores: weakref.WeakValueDictionary = weakref.WeakValueDictionary()

    def __new__(cls, percent: int):
        score_value = 'Unknown'
        if percent <= 25:
            score_value = 'D'
        elif percent <= 50:
            score_value = 'C'
        elif percent <= 75:
            score_value = 'B'
        elif percent <= 100:
            score_value = 'A'
        score_obj = cls._scores.get(score_value)
        if score_obj is not None:
            return score_obj
        score_obj = object.__new__(Score)
        cls._scores[score_value] = score_obj
        score_obj.score_value = score_value
        return score_obj

    def __repr__(self):
        return f'Score = {self.score_value}'


if __name__ == '__main__':
    score_90 = Score(90)
    print(f'90% is {score_90}')
    score_100 = Score(100)
    print(f'100% is {score_100}')
    print(f'90% has the same score as 100% - {score_90 is score_100}')
    score_70 = Score(70)
    print(f'70% is {score_70}')
    print(f'70% has the same score as 100% - {score_70 is score_100}')
    del score_70
    print(f'scores = {list(Score._scores.keys())}')
