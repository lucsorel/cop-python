from convert import capitalize

# invalid case (text is expected)
try:
    capitalize(42)
except AssertionError as error:
    print(f"an error occurred: '{error}'")
else:
    print('an error should have occurred')
