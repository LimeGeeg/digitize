from digitize import discharge, Language

def test_basic():
    assert discharge(100000000, True, Language.EN) == "100,000,000 million"
