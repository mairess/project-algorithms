def is_palindrome_iterative(word: str) -> bool:
    if not word:
        return False

    size = len(word)

    for index in range(0, size // 2):
        if word[index] != word[size - index - 1]:
            return False
    return True
