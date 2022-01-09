class stats:
    """ Stats are used to create a state.
    State is given to AI to let it orient it in the game. """
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
        self.bagsize = self.playbag.get_back_size()


    def updateStats(self):
        """Updates all attributes"""
        pass

    def stats_bag(self):
        """Checking all tokens in bag to see the distribution of available tokens"""
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
        """Checking all tokens on the board and looking at the distribution of those token"""
        pass

    def prob_next_move_is_white(self):
        """Estimates the probability of next random token is a white"""
        prob = (self.amount_white_in_bag/self.bagsize)*100

    def prob_next_move_is_boom(self):
        """Estimates the probability of next random token is going to boom"""
        pass

    def we_see_green(self):
        """Checks if the last 2 spots were a green"""
        pass

    def positionstats(self):
        """Checks for buying points, points and if it landed on a rubin."""
        pass




