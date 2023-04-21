from src.models.ingredient import Ingredient
from src.models.dish import Dish
import pandas as pd


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = dict()
        self.file_CSV()

    def file_CSV(self):
        result = pd.read_csv(self.source_path)
        # OBS: 
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html
        for dish, price, ingredient, recipe_amount in result.itertuples(
            index=False
        ):
            if dish not in self.dishes:
                self.dishes[dish] = Dish(dish, price)
            self.dishes[dish].add_ingredient_dependency(
                Ingredient(ingredient), recipe_amount
            )
        self.dishes = set(self.dishes.values())
