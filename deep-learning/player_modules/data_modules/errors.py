class WeekError(Exception):
    def __init__(self, wk_index, name):
        self.value = repr("Data in week " + str(wk_index) + " is unavailable for " + str(name))
    def __str__(self):
        return self.value