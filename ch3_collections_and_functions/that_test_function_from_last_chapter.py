def test(function, examples):
    passed = 0
    run = 0

    for example in examples:
        run += 1
        expected = example[-1]
        actual = function(*example[:-1])

        if expected == actual:
            passed += 1
        else:
            print(f"Whoops. For example {example}, the function returned {actual}.")

    print(f"\n{passed} out of {run} examples worked as expected.")