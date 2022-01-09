class stats:
    def __init__(self,playboard,playbag):
        self.playboard = playboard
        self.playbag = playbag
        self.bag = self.playbag.bag
        self.amount_token_in_bag = 0
        self.amount_white_in_bag = 0
        self.sum_white_in_bag = 0
        self.values_white = []
        self.sum_colors_in_bag=0
        self.amount_orange_in_bag = 0
        self.amount_red_in_bag=0
        self.amount_blue_in_bag=0
        self.amount_green_in_bag=0
        self.amount_black_in_bag=0
        self.state=0
        self.bagsize = self.playbag.get_bag_size()


    def updateStats(self):
        pass

    def stats_bag(self):
        for token_color, token_value in self.bag:
            self.amount_token_in_bag +=1
            if token_color == "White":
                self.amount_white_in_bag +=1
                self.sum_white_in_bag += token_value
                self.values_white.append(token_value)
            if token_color == "Orange":
                self.amount_orange_in_bag +=1
                self.sum_colors_in_bag += token_value
            if token_color == "Red":
                self.amount_red_in_bag += 1
                self.sum_colors_in_bag += token_value
            if token_color == "Blue":
                self.amount_blue_in_bag += 1
                self.sum_colors_in_bag += token_value
            if token_color == "Green":
                self.amount_green_in_bag += 1
                self.sum_colors_in_bag += token_value
            if token_color == "Black":
                self.amount_black_in_bag += 1
                self.sum_colors_in_bag += token_value


    def stats_board(self):
        pass

    def prob_next_move_is_white(self):
        prob = (self.amount_white_in_bag/self.bagsize)*100

    def prob_next_move_is_boom(self):
        pass

    def we_see_green(self):
        pass




