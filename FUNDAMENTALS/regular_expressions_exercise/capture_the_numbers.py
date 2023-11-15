    import re

    pattern = r"\d+"

    try:
        while True:
            line = input()
            matches = re.finditer(pattern, line)
            for match in matches:
                print(match.group(), end=" ")
    except EOFError:
        pass  # Catch the EOFError when there is no more input
