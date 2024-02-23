def check_lost(positions):
    for position in positions:
        x, y = position
        if y < 1:
            return True
    return False
