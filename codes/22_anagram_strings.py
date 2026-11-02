
def is_anagram(first, second):
    first = first.lower().replace(" ", "")
    second = second.lower().replace(" ", "")

    return sorted(first) == sorted(second)


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))
    print(is_anagram("hello", "world"))

