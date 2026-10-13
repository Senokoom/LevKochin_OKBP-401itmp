def script(check, x, y):
    return get_action_to_nearest_gold(check, x ,y)


from collections import deque


def get_action_to_nearest_gold(check, x, y):

    if check("gold", x, y):
        return "take"

    queue = deque([(x, y, None)])
    visited = set()
    visited.add((x, y))

    directions = [
        (0, -1, "up"),
        (0, 1, "down"),
        (-1, 0, "left"),
        (1, 0, "right")
    ]

    while queue:
        cx, cy, first_step = queue.popleft()
        for dx, dy, action in directions:
            nx, ny = cx + dx, cy + dy
            if (nx, ny) not in visited:
                current_first_step = first_step if first_step is not None else action
                if check("gold", nx, ny):
                    return current_first_step
                if not check("wall", nx, ny):
                    visited.add((nx, ny))
                    queue.append((nx, ny, current_first_step))
    return "pass"


