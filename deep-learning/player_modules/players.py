import uuid
import torch
import player_modules.data_modules.stats as st
import player_modules.data_modules.errors as err
from typing import Dict
from enum import Enum

class PlayerType(Enum):
    qb = 1
    rb = 2
    wr = 3
    te = 4
    k = 5
    de = 6

class Player:
    # Player::__init__ -> Initialize a New Player Object
    # Parameters:
    #   name_in: string representing player name
    #   team_in: string representing team name
    #   pos_in: PlayerType representing player position
    # Modifies:
    #   self.num_weeks
    #   self.num_ff_weeks
    #   self.stats: map int(week#) -> statistics object
    #   self.ff_stats: numpy array -> week_index - 1 corresponds to fantasy points from a particular week
    def __init__(self, name_in, team_in, pos_in):
        self.id = uuid.uuid1()
        self.name = name_in
        self.team = team_in
        self.position = pos_in
        self.num_weeks = 0
        self.num_ff_weeks = 0
        self.stats: Dict[int:st.Stats] = {} 
        self.ff_stats = torch.zeros(18)

    # Player::__load_weekly_stats__ -> Load NFL(non-fantasy) stats from a stats object
    # Parameters:
    #   wk_index: integer corresponding to week number
    #   wk_stats: statistics object
    # Modifies:
    #   self.stats
    def set_weekly_stats(self, wk_index, wk_stats):
        self.stats[wk_index] = wk_stats
        self.num_weeks = self.num_weeks if wk_index < self.num_weeks else wk_index

    # Player::__load_weekly_ff_stats__ -> Load Fantasy stats from an integer
    # Parameters:
    #   wk_index: integer corresponding to week number
    #   wk_stats: float corresponding to number of fantasy points
    # Modifies:
    #   self.ff_stats
    def set_weekly_ff_stats(self, wk_index, wk_stats):
        self.ff_stats[wk_index-1] = wk_stats

    def get_weekly_stats(self, wk_begin, wk_end):
        try:
            if(self.num_weeks < wk_end):
                raise err.WeekError(wk_end, self.name)
            
            weeks = []
            for i in range(wk_begin, wk_end):
                weeks.append((self.stats[i]).stats_tensor())
            
            return torch.cat(tuple(weeks))

        except Exception as e:
            print(e.__str__())