# Exercise #2

# Find the mistake in the following code snippet and correct it:

# corrected snippet
def compute_patterns(inputs=None, pattern="new pattern"):
    if inputs is None:
        inputs = []
    inputs.append(pattern)
    patterns = ["a list based on "] + inputs
    return patterns


# just some tests - you can remove them if you want
print("".join(compute_patterns()))
print("".join(compute_patterns()))
print("".join(compute_patterns()))
test_inputs = []
print(" ".join(compute_patterns(test_inputs, "very new pattern")))
print(" ".join(compute_patterns(test_inputs, "super new pattern")))
print(" ".join(compute_patterns(test_inputs, "super duper new pattern")))
print("".join(compute_patterns()))
