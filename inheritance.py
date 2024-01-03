class team:
    def __init__(self,name='name',origin='origin'):
        self.teamname = name
        self.teamorigin = origin
    def DefineTeamname(self,name):
        self.teamname = name
    def DefineTeameorigin(self,origin):
        self.teamorigin = origin

# class inhclassname(parentclass):  #to define inherentance class
#     def __init__(self, input1, input2):
#         parentclass.__init__(self)
#         self.attribute1 =input1
#         self.attribute2 =input2
#         self.attribute3 =0
#         def Anothermtd(self):
#             Action(s)

class player(team):
    def __init__(self, playername, ppoints,teamname, teamorigin):
        team.__init__(self,teamname, teamorigin )
        self.playername =playername
        self.playerpoints=ppoints
    def scoredpoint(self):
        self.playerpoints += 1
    def setname(self,name):
        self.playername= name
    def __str__(self):
        return 'player has scored:' +str(self.playerpoints) +'points'

player1=player('der',50, 'kin', 'chicago')
print(player1.playername)
print(player1.playerpoints)
print(player1.teamname)
print(player1.teamorigin)
# # player1.DefineTeamname('london')
# print(player1.teamname)

player1.scoredpoint()
print(player1.playerpoints)
player1.setname('lee')
print(player1.playername)
print(player1)