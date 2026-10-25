def greet():
    return "Hello, my name is Pradnya!"
def test_greet():
    assert greet() == "Hello, my name is Pradnya!"
if __name__ == "__main__":
    print(greet())
    test_greet()
    print("Pradnya's DevOps CI/CD test passed!")
