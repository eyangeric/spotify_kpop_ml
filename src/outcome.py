class Outcome:
    outcomes = {0: 'Donald Feelz', 1: 'Eric Feelz', 2: 'Eric/Donald Feelz'}
    def __init__(self, prediction = int):
        self.prediction = prediction
        self.outcome = self.outcomes[self.prediction]