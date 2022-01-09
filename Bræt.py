gameboard = [(0, 0, 0, 0), (1, 1, 0, 0), (2, 2, 0, 0), (3, 3, 0, 0), (4, 4, 0, 0), (5, 5, 0, 1), (6, 6, 1, 0),
             (7, 7, 1, 0), (8, 8, 1, 0), (9, 9, 1, 1),
             (10, 10, 2, 0), (11, 11, 2, 0), (12, 12, 2, 0), (13, 13, 2, 1), (14, 14, 3, 0), (15, 15, 3, 0),
             (16, 15, 3, 1), (17, 16, 3, 0), (18, 16, 4, 0),
             (19, 17, 4, 0), (20, 17, 4, 1), (21, 18, 4, 0), (22, 18, 5, 0), (23, 19, 5, 0), (24, 19, 5, 1),
             (25, 20, 5, 0), (26, 20, 6, 0),
             (27, 21, 6, 0), (28, 21, 6, 1), (29, 22, 7, 0), (30, 22, 7, 1), (31, 23, 7, 0), (32, 23, 8, 0),
             (33, 24, 8, 0), (34, 24, 8, 1), (35, 25, 9, 0),
             (36, 25, 9, 1), (37, 26, 9, 0), (38, 26, 10, 0), (39, 27, 10, 0), (40, 27, 10, 1), (41, 28, 11, 0),
             (42, 28, 11, 1), (43, 29, 11, 0),
             (44, 29, 12, 0), (45, 30, 12, 0), (46, 30, 12, 1), (47, 31, 12, 0), (48, 31, 13, 0), (49, 32, 13, 0),
             (50, 32, 13, 1), (51, 33, 14, 0),
             (52, 33, 14, 1), (53, 35, 15, 0)]


class Board:
    tokens_on_board = []

    def __init__(self):
        self.amount_of_tokens_on_board = 0
        white_counter = 0
        white_sum = 0
        orange_counter = 0
        orange_sum = 0
        red_counter = 0
        red_sum = 0
        blue_counter = 0
        blue_sum = 0
        green_counter = 0
        green_sum = 0

    def get_position_value(self, index):
        return (gameboard[index])

    def get_white_sum(self):
        white_sum = 0
        for token_color, token_value in self.tokens_on_board:
            if token_color == "White":
                white_sum += white_sum
        return (white_sum)

    def add_token_to_board(self,chosen_color,chosen_value):
        print("adding token to board")
        self.tokens_on_board.append((chosen_color,chosen_value))
        print(self.tokens_on_board)

    def important_last_two_token(self):
        # TODO
        pass

    def amount_token_on_board(self):
        counter = 0
        for token_color, token_value in self.tokens_on_board:
            counter += 1
        return (counter)

    def get_colors_sum(self):
        white_counter = 0
        white_sum = 0
        orange_counter = 0
        orange_sum = 0
        red_counter = 0
        red_sum = 0
        blue_counter = 0
        blue_sum = 0
        green_counter = 0
        green_sum = 0
        for token_color, token_value in self.tokens_on_board:
            if token_color == "White":
                white_counter += 1
                white_sum += token_value
            elif token_color == "Orange":
                orange_counter += 1
                orange_sum += token_value
            elif token_color == "Red":
                red_counter += 1
                red_sum += token_value
            elif token_color == "Blue":
                blue_counter += 1
                blue_sum += token_value
            elif token_color == "Green":
                green_counter += 1
                green_sum += token_value
        return (
            white_counter, white_sum, orange_counter, orange_sum, red_counter, red_sum, blue_counter, blue_sum,
            green_counter,
            green_sum)
