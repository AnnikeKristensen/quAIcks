import random
import Bræt


class Bag:
    """The bag is a collection of tokens the user can choose between. The collection can add tokens (the user buys them).
    In here theres collection (always has all tokens) and a bag (the bag initially copies the collection but then
    the user can choose to continue to play and tokens will be removes from the bag, copies the collection again
    when round is reset)"""
    def __init__(self, playboard):
        self.token_collection = []
        self.bag = []
        self.bagsize = self.get_bag_size()
        self.token_collect=token
        self.playboy = playboard

    def initialize(self):
        """ a newly bag ready for use """
        self.add_to_collection(self.token_collect.white_token(1))
        self.add_to_collection(self.token_collect.white_token(1))
        self.add_to_collection(self.token_collect.white_token(1))
        self.add_to_collection(self.token_collect.white_token(1))
        self.add_to_collection(self.token_collect.white_token(2))
        self.add_to_collection(self.token_collect.white_token(2))
        self.add_to_collection(self.token_collect.white_token(3))
        self.add_to_collection(self.token_collect.orange_token(1))

    def add_to_collection(self, token):
        """adds the token to the collection"""
        self.token_collection.append(token)

    def collection_to_bag(self):
        """copies the collection to the bag. This is used every round when the bag is re-filled"""
        self.bag = self.token_collection

    def get_random_token(self):
        """select a random token from the bag. Remove the token from the bag and add it to the board used tokens"""
        end = self.get_bag_size()-1
        index = random.randint(0,end)
        chosen_color = self.bag[index][0]
        chosen_value = self.bag[index][1]
        chosen_index = index
        data = (chosen_color, chosen_value)
        self.playboy.add_token_to_board(chosen_color, chosen_value)
        self.remove_token_from_bag(chosen_index)


    def remove_token_from_bag(self,index):
        """Helper function to delete a token from bag. Used when random token gets pulled"""
        print("Deleting ", self.bag[index])
        del self.bag[index]
        print(self.bag)


    def get_bag_size(self):
        """counts how many tokens is left in the bag"""
        counter = 0
        for token_color, token_value in self.bag:
            counter += 1
        return counter

    def white_in_bag(self):
        """counts how many white tokens is left in the bag"""
        white_in_bag_counter = 0
        white_in_bag_values = []
        for token_color, token_value in self.token_collection:
            if token_color == "White":
                white_in_bag_counter += 1
                white_in_bag_values.append(token_value)

class token():

    def __init__(self,value):
        pass

    @staticmethod
    def white_token(value):
        """White tokens are used for the boom. The user is allowed up to 7 (but this can be modified) in total.
        User cannot buy more white tokens. White only comes in values 1, 2 and 3"""
        if value == 1:
            value = 1
            price = None
            return("White",1)
        elif value == 2:
            return("White",2)
        elif value == 3:
            return("White",3)
        else:
            print("Faulty value to white (only takes in 1,2,3)")

    @staticmethod
    def orange_token(value):
        """Orange tokens are not calculated towards the boom. The user is allowed any amount of this. User can buy
        more orange tokens for price of 3. Orange only comes in value 1"""
        if value == 1:
            return("Orange",1)
        else:
            print("Faulty value to orange (only takes in 1)")


    def red_token(value):
        pass


    def blue_token(value):
        pass


    def green_token(value):
        pass


    def black_token(value):
        pass


    def purple_token(value):
        pass
