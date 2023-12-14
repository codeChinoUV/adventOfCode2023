class GameDesigner:

    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name

    def load_bag(self, red_cubes: int, green_cubes: int, blue_cubes: int) -> None:
        self.red_cubes = red_cubes
        self.green_cubes = green_cubes
        self.blue_cubes = blue_cubes

    def play(self) -> int:
        self.games = {}
        
        with open(self.__file_name) as file:
            for index, line in enumerate(file.readlines()):
                current_game = str(index + 1)
                self.games[current_game] = {"red": 0, "green": 0, "blue": 0}
                game_separator = line.find(":")
                game = line[game_separator+1:]
                sets = game.split(";")

                for set in sets:
                    plays = set.split(",")
                    
                    for play in plays:
                        if "blue" in play:
                            clean = play.replace(" blue", "")
                            if int(clean) > self.games[current_game]["blue"]:
                                self.games[current_game]["blue"] = int(clean)

                        if "red" in play:
                            clean = play.replace(" red", "")
                            if int(clean) > self.games[current_game]["red"]:
                                self.games[current_game]["red"] = int(clean)

                        if "green" in play:
                            clean = play.replace(" green", "")
                            if int(clean) > self.games[current_game]["green"]:
                                self.games[current_game]["green"] = int(clean)

    def get_posible_games_id_sum(self) -> int:
        sum = 0

        for key in self.games.keys():
            current_game = self.games[key]
            is_valid = True

            if current_game["blue"] > self.blue_cubes:
                is_valid = False

            if current_game["red"] > self.red_cubes:
                is_valid = False
            
            if current_game["green"] > self.green_cubes:
                is_valid = False

            if is_valid:
                sum += int(key)

        return sum
    
    def get_power_sum_of_game(self) -> int:
        sum = 0

        for key in self.games.keys():
            current_game = self.games[key]
            game_power = current_game["blue"] * current_game["red"] * current_game["green"]

            sum += game_power

        return sum
    
if __name__ == "__main__":
    game = GameDesigner("cubeConundrumInput.txt")
    game.load_bag(12, 13, 14)
    game.play()

    print("Posible games ID sum: ", game.get_posible_games_id_sum())
    print("Games power sum: ", game.get_power_sum_of_game())