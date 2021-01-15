class user:
    def __init__(self, name):
        self.moviesReviewed = set()
        self.reviewCount = 0
        self.name = name
    def isCritic(self):
        return self.reviewCount > 3 