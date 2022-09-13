from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    words = ["the", "man"]
    expected = [50865, 9799]
    for index in range(len(words)):
        assert count_ocurrences(path, words[index]) == expected[index]
