class Search(object):

    def __init__(self, keyword=""):
        self.keyword = keyword

    @classmethod
    def Positive(cls):
        return cls(keyword="my film")

    @classmethod
    def Negative(cls):
        return cls(keyword="sascmcsl")