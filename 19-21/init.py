def game(stones, steps) -> bool:
    if stones >= 129:
        return steps % 2 == 0
    if steps == 0:
        return False
    h = [game(stones + 1, steps - 1),
         game(stones * 2, steps - 1)]
    return any(h) if (steps - 1) % 2 == 0 else all(h)

