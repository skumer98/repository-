# Sara Umer 

class FoodItem:
    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


# Test the FoodItem class with the given input
if __name__ == "__main__":
    default_food = FoodItem()
    custom_food_name = input()
    custom_fat = float(input())
    custom_carbs = float(input())
    custom_protein = float(input())
    custom_servings = float(input())

    custom_food = FoodItem(custom_food_name, custom_fat, custom_carbs, custom_protein)

    default_food.print_info()
    print('Number of calories for 1.00 serving(s): {:.2f}'.format(default_food.get_calories(1)))

    custom_food.print_info()
    print('Number of calories for 1.00 serving(s): {:.2f}'.format(custom_food.get_calories(custom_servings)))





