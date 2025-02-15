import pyquotes

def test_get():
    quote = pyquotes.get()
    assert isinstance(quote, str)  # Ensure it returns a string
    assert len(quote) > 0  # Ensure it's not empty

if __name__ == "__main__":
    test_get()
    print("All tests passed!")