
#custom error classes

class NullInputError (Exception):
    def __init__ (self, errorMsg):
        self.errMsg=errorMsg
    def __str__ (self):
        return self.errMsg
    

