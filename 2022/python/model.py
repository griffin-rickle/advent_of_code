class Elf:
    def __init__(self, calorie_list: list[int]):
        self.calorie_list: list[int] = calorie_list
        self.total_calories: int = sum(calorie_list)
