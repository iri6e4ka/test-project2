class Film(object):

    def __init__(self, title="", year=""):
        self.title = title
        self.year = year

    @classmethod
    def Negative(cls):
        return cls(title="my film", year="")

    @classmethod
    def Positive(cls):
         return cls(title="my film", year="1989")
