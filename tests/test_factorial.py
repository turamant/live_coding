# TEST

# factorial(0) должно вернуть 1
# factorial(5) должно вернуть 120 (поскольку 5! = 5 × 4 × 3 × 2 × 1)


from factorial.main import factorial


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
