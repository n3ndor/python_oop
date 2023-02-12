
class Player:
    def __init__(self, info):
        self.name = info["name"]
        self.age = info["age"]
        self.position = info["position"]
        self.team = info["team"]

    @classmethod ##NinjaBonus
    def add_player(cls, data):
        new_team = []
        for new in info:
            new_team.append(cls(new))
        return new_team 


    def __repr__(self):
        display = f"Player: {self.name}, age: {self.age}, position: {self.position}, team: {self.team}"
        return display

kevin = {"name": "Kevin Durant", "age":34,"position": "small forward", "team": "Brooklyn Nets"}
jason = {"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"}
kyrie = {"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"}


# Create your Player instances here!
player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)
print(player_jason)
print(player_kevin)
print(player_kyrie)