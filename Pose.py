import random
import Bræt


class Bag:
    def __init__(self, playboard):
        self.token_collection = []
        self.bag = []
        self.bagsize = self.get_bag_size()
        self.token_collect=token
        self.playboy = playboard

    def initialize(self):
        self.add_to_collection(self.token_collect.white_token(1))
        self.add_to_collection(self.token_collect.white_token(1))
        self.add_to_collection(self.token_collect.white_token(1))
        self.add_to_collection(self.token_collect.white_token(1))
        self.add_to_collection(self.token_collect.white_token(2))
        self.add_to_collection(self.token_collect.white_token(2))
        self.add_to_collection(self.token_collect.white_token(3))
        self.add_to_collection(self.token_collect.orange_token(1))

    def add_to_collection(self, token):
        self.token_collection.append(token)

    def collection_to_bag(self):
        self.bag = self.token_collection

    def get_random_token(self):
        end = self.get_bag_size()-1
        index = random.randint(0,end)
        chosen_color = self.bag[index][0]
        chosen_value = self.bag[index][1]
        chosen_index = index
        data = (chosen_color, chosen_value)
        self.playboy.add_token_to_board(chosen_color, chosen_value)
        self.remove_token_from_bag(chosen_index)



    def remove_token_from_bag(self,index):
        print("Deleting ", self.bag[index])
        del self.bag[index]
        print(self.bag)


    def get_bag_size(self):
        counter = 0
        for token_color, token_value in self.bag:
            counter += 1
        return counter

    def white_in_bag(self):
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


"""Bag"""

"""Initialize"""

"""Add to bag"""
