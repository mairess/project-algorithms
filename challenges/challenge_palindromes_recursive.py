def is_palindrome_recursive(
    word: str, low_index: int, high_index: int
) -> bool:
    if not word or word[low_index] != word[high_index]:
        return False
    elif low_index >= high_index:
        return True
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
