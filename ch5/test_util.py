def test51(examples):
    passed = 0
    run = 0

    for i, example in enumerate(examples):
        run += 1
        actual, expected = example

        if expected == actual:
            passed += 1
        else:
            print(
                f"Whoops. For example {i}, the function returned {actual} and should've returned {expected}."
            )

    print(f"\n{passed} out of {run} examples worked as expected.")