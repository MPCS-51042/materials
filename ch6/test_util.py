def test6_equiv(examples):
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


def test63_error(class_def, examples):
    passed = 0
    run = 0

    for example in examples:
        run += 1
        string, error = example
        found = False
        try:
            eval(string, {"Pitch": class_def})
        except ValueError:
            if error == ValueError:
                passed += 1
                found = True
        except TypeError:
            if error == TypeError:
                passed += 1
                found = True
        finally:
            if not found:
                print(f"Whoops. For example {example}, did not get expected {error}.")

    print(f"\n{passed} out of {run} examples worked as expected.")
