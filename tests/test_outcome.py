from src.outcome import Outcome

def test_outcome():
    outcome_0 = Outcome(0)
    outcome_1 = Outcome(1)
    outcome_2 = Outcome(2)
    assert outcome_0.__dict__ == {'prediction': 0, 'outcome': 'Donald Feelz'}
    assert outcome_1.__dict__ == {'prediction': 1, 'outcome': 'Eric Feelz'}
    assert outcome_2.__dict__ == {'prediction': 2, 'outcome': 'Eric/Donald Feelz'}