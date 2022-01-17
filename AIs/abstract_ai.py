class AbstractAI:

    def __init__(self, ai_name="Unnamed_ai", verbose=True):
        self.ai_name = ai_name
        self.verbose = verbose

    def make_decision(self, args):
        choice = self.do_ai(args)
        if self.verbose:
            print(f"{self.ai_name} made decision {choice}.")
        return choice

    def do_ai(self, args):
        raise NotImplementedError
