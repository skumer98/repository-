# Sara Umer 1999495



#Ex: If the input is:
# Ravens
# 13
# 3 
# where Ravens is the team's name, 13 is the number of team wins, and 3 is the number of team losses, 


# the output is:
# Congratulations, Team Ravens has a winning average!
# If the input is Angels 80 82, the output is:
# Team Angels has a losing average.

# You can start with the following class definition:

# class Team: def init(self): 
# self.teamname = 'none' 
# self.teamwins = 0 
# self.team_losses = 0


# Complete the Team class implementation. 
class Team:
    def __init__(self):
        self.teamname = 'none'
        self.teamwins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        if self.teamwins == 0 and self.team_losses == 0:
            return 0.0
        return self.teamwins / (self.teamwins + self.team_losses)


# TODO: Define get_win_percentage()
# For the class method get_win_percentage(), the formula is:
# team_wins / (team_wins + team_losses)
#Note: Use floating-point division.




# Test cases
team1 = Team()
team1.teamname = 'Ravens'
team1.teamwins = 13
team1.team_losses = 3


print(f"Congratulations, Team {team1.teamname} has a winning average!") 




