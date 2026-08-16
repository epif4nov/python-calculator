from calculator.memory import Memory

def test_add():
    m = Memory()
    m.add(5)
    assert m.recall() == 5

def test_subtract():
    m = Memory()
    m.subtract(5)
    assert m.recall() == -5

def test_accumulates():
    m = Memory()
    m.add(5)
    m.add(3)
    assert m.recall() == 8

def test_clear():
    m = Memory()
    m.add(5)
    m.clear()
    assert m.recall() == 0


