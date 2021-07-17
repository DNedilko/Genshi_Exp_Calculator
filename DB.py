
class Data():
    def __init__(self, filename):
        self.filename = filename
        self.levels=None
        self.file=None
        self.load()

    def load(self):
        self.file= open(self.filename, 'r')
        self.levels={}
        for line in self.file:
            level, exp, asc = line.strip().split(',')
            self.levels[level] = (exp, asc)
        self.file.close()

    def get_level_exp(self, level):
        if level in self.levels:
            return self.levels[level][0]
        else:
            return -1

    def get_am_of_asc(self, level1, level2):
        num_of_asc=0
        if self.get_level_exp(level1) & self.get_level_exp(level1) !=-1:
            for asc in range(self.levels[level1], self.levels[level2]):
                num_of_asc+=asc
            return num_of_asc




