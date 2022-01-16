"""Every token has rules
White tokens are used for the boom. The user is allowed up to 7 (but this can be modified) in total.
User cannot buy more white tokens. White only comes in values 1, 2 and 3

Orange tokens are not calculated towards the boom. The user is allowed any amount of this. User can buy
more orange tokens for price of 3. Orange only comes in value 1"""



class Token:
    def __init__(self):
        pass

    def newToken(self, colour, value):
        print("New token: {} with value: {}".format(colour,value))
        return((colour,value))

    def isTokenAllowed(self,colour,value):
        if colour == "Orange":
            if value == 1:
                return True
        if colour == "Blue":
            pass
        if colour == "Yellow":
            pass
        if colour == "Purple":
            pass
        if colour == "Green":
            pass
        if colour == "Red":
            pass

        print("Colour {} and value {} is not allowed")
        return False


    def tokenRules(self, has_stopped,value):
        pass

    def tokenPrices(self):
        pass


