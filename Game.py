class Game():
    """The actual gameplay"""
    def __init__(self, bag, board, stats):
        self.bag = bag
        self.board = board
        self.score = 0
        self.rubin = 0
        self.drop = 0
        self.boomvalue = 7
        self.bag= self.bag.bag
        self.boardtokens = self.board.tokens_on_board
        self.color_on_board = self.board.get_colors_sum()[2]
        self.position = 0
        self.statistik = stats
        self.stop = False



    def turn(self):
        """defines a turn"""
        #get stats
        # give stats to ai
        # give possibilities of choice to ai
        # let ai decide
        # if continue: get random token
            # get_colors sum (bræt)
            # did boom?-update
                #self.stop = true
            # update position
            # token rules apply
        #if stop:
            # self.stop = true

        #if self.stop = true
            # temp_end_turn()
        pass

    def temp_end_turn(self):
        """ For now while roundB hasnt been made, if AI chooses to stop, this will happen.
        Scores get accumulated, all tokens get back into the bag"""
        #token_rules_apply (self.stop er nu true)
        #get position fra bræt
        #stands on rubin?
        #did boom?
            #if yes:
            # AI skal vælge imellem buying points og score
        #+ score
        #list of available tokens to buy
        #købsprocess
        #køb for rubiner?
        # +1 runde
        # collection_to_bag
        #empty token_on_board
        pass

    def token_rules_apply(self, latest_token):
        if self.stop == False: # If game continues
            if self.board.last_token_was_colored: # and the last token was colored
                if self.board.last_token_color == "Red": #If it was red, if theres already orange, move position accordingly (see token:red)
                    if self.board.orange_counter == 1 or 2:
                        self.position += 1
                    elif self.board.orange_counter >= 3:
                        self.position += 2
                if self.board.last_token_color == "Blue":
                    #TODO En hel beslutningsprocess - bruger må tage value mængde tokens op og vælge imellem dem
                    pass
                if self.board.last_token_color == "Yellow":
                    if self.board.tokens_on_board[-2] == "White":
                        temp = self.board.tokens_on_board[-2]
                        self.board.delete_token_from_board(-2)
                        self.bag.add_to_bag(temp)
        if self.stop:
            amount_purple= self.board.get_colors_sum()[10]
            if amount_purple > 0: #amount of purple
                if amount_purple == 1:
                    self.score += 1
                if amount_purple == 2:
                    self.score += 1
                    self.rubin += 1
                else:
                    self.score += 2
                    self.drop += 1
            if self.statistik.we_see_green:
                greencounter = 0 #amount of green in the last two spots
                lasttwo = self.board.tokens_on_board[-2:]
                for token_color, token_value in lasttwo:
                    if token_color == "Green":
                        greencounter += 1
                self.rubin += greencounter
            amount_black =  self.board.get_colors_sum()[11]
            if amount_black > 0:
                #TODO - sandsynlighed for om man har flere sorte end "modstanderen".
                pass


    def list_of_available_tokens_for_buy(self):
        pass
