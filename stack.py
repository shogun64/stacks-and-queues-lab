def is_valid_parentheses(s: str) -> bool:
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for character in s:
        if character in matching.values():
            stack.append(character)
        elif character in matching:
            if not stack or stack[-1] != matching[character]:
                return False
            stack.pop()

    return not stack