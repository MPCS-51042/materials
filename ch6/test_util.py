def fraction_equality(self, other):
    return (
        True
        if self.numerator == other.numerator and self.denominator == other.denominator
        else False
    )


def test61(examples):
    passed = 0
    run = 0

    for example in examples:
        run += 1
        actual, expected = example
        if expected == actual:
            passed += 1
        else:
            print(f"Whoops. For example {example}, the function returned {actual}.")

    print(f"\n{passed} out of {run} examples worked as expected.")