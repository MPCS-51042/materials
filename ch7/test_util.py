def test71(function, examples):
    passed = 0
    run = 0

    for example in examples:
        run += 1
        expected = example[-1]
        actual = function(*example[:-1])

        mistakes = False
        for a, e in zip(actual, expected):
            if a != e:
                mistakes = True
                print(f"Whoops. For example {example}, the function returned {actual}.")
        if not mistakes:
            passed += 1

    print(f"\n{passed} out of {run} examples worked as expected.")


def first_digit(x):
    return int(str(x)[0])