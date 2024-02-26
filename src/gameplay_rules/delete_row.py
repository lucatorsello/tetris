def clear_rows(grid, locked):

    inc = 0
    valid_y_positions = {}

    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        valid_y_positions.update({i: inc})
        if (0, 0, 0) not in row:
            inc += 1
            del valid_y_positions[i]
            for j in range(len(row)):

                try:
                    del locked[(j, i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y in valid_y_positions.keys():
                newKey = (x, y + valid_y_positions[y])
                locked[newKey] = locked.pop(key)

    return inc
