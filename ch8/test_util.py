def testP1(function, examples):
    passed = 0
    run = 0
    errors = []
    for i, example in enumerate(examples):
        try:
            run += 1
            test_func, inputs, expected = example
            actual = function(test_func)(*inputs)

            if expected == actual:
                passed += 1
            else:
                print(f"Whoops. For example {example}, the function returned {actual}.")
        except Exception as e:
            print(e)
            errors.append((i, e))

    print(f"\n{passed} out of {run} examples worked as expected.")
    if len(errors) > 0:
        for error in errors:
            print(f"Error in trial {error[0]}: ", error[1])
