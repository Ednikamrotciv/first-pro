# class classname:
#     def __init__(self):
#         self.Attribute=0
#     def Anotherfunction(self):
#         Action(s)
class team:
    def __init__(self,name='name',origin='origin'):
        self.teamname = name
        self.teamorigin = origin
    def DefineTeamname(self,name):
        self.teamname = name
    def DefineTeameorigin(self,origin):
        self.teamorigin = origin


Team1 = team('tigers','ohio')
Team2 = team()
print(Team1.teamname)
Team1.DefineTeamname('dolphin')
print(Team1.teamname)
print(Team1.teamorigin)
Team1.DefineTeameorigin('chicago')
print(Team1.teamorigin)
print(Team2.teamname)
print(Team2.teamorigin)