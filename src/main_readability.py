def place_shape_on_grid(shape_position, grid, current_piece):
    for x, y in shape_position:
        if y > -1:
            grid[y][x] = current_piece.color


def update_locked_positions(shape_position, locked_positions, current_piece):
    for position in shape_position:
        p = (position[0], position[1])
        locked_positions[p] = current_piece.color
