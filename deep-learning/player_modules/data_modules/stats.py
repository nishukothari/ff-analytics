class Stats:
    def __init__(self):
        NotImplemented

    def stats_tensor(self):
        NotImplemented

class QbStats(Stats):
    def __init__(self, py_in, ptd_in, int_in, ry_in, rtd_in, fum_in):
        self.passing_yards = py_in
        self.passing_tds = ptd_in
        self.interceptions = int_in
        self.rushing_yards = ry_in
        self.rushing_tds = rtd_in
        self.fumbles = fum_in

    def stats_tensor(self):
        NotImplemented

class RbStats(Stats):
    def __init__(self):
        NotImplemented

    def stats_tensor(self):
        NotImplemented

class WrStats(Stats):
    def __init__(self):
        NotImplemented
    
    def stats_tensor(self):
        NotImplemented

class TeStats(Stats):
    def __init__(self):
        NotImplemented

    def stats_tensor(self):
        NotImplemented

class DeStats(Stats):
    def __init__(self):
        NotImplemented

    def stats_tensor(self):
        NotImplemented

class KStats(Stats):
    def __init__(self):
        NotImplemented

    def stats_tensor(self):
        NotImplemented