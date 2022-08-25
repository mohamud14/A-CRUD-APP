from main import *

#OOP
class Teams(db.Model):
    team_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    team_name = db.Column(db.String(100), nullable=False, unique=True)
    # team_manager = db.Column(db.String(100), nullable=False)
    # stadium = db.Column(db.String(100), nullable=False)
    players = db.relationship('Players', backref='teams', lazy='select')
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name
    # def __init__(self, team_name, team_id, team_manager, stadium):
    #     self.team_name = team_name
    #     self.team_id = team_id
    #     self.team_manager = team_manager
    #     self.stadium = stadium
    def __repr__(self):
        return "<Team ID: {0} |Team Name: {1}".format(self.team_id,
                                                      self.team_name)
    # def __ref__(self):
    #     return "<Team ID: {0} |Team Name: {1} | Team Manager: {2} | \
    #             Stadium: {3}".format(self.team_id, self.team_name,
    #                                  self.team_manager, self.stadium)
#
#
class Players(db.Model):
    player_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    player_name = db.Column(db.String(100), nullable=False)
    plays_for = db.Column(db.Integer,db.ForeignKey('teams.team_id'), nullable=False)
#     nationality = db.Column(db.String(100),nullable=False)
#     position = db.Column(db.String(100), nullable=False)

#
    def __init__(self, player_name, plays_for, player_id):
        self.player_name = player_name
        self.plays_for = plays_for
        self.player_id = player_id
#
    def __repr__(self):
        return "<Player ID: {0} |Player Name: {1} | Team: {2}".format(self.player_id, self.player_name, self.plays_for)
