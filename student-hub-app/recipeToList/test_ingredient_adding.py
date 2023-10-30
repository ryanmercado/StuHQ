import RecipeBook
import GroceryList


def test_recipe():
    meal = RecipeBook.Recipe(["bacon", "eggs", "butter", "cheese"])
    assert(meal.get_ingredients() == ["bacon", "eggs", "butter", "cheese"])


def test_recipe_add_ingredient():
    meal = RecipeBook.Recipe(["bacon", "eggs", "butter", "cheese"])
    assert(meal.get_ingredients() == ["bacon", "eggs", "butter", "cheese"])
    meal.add_ingredient("blue berries")
    assert(meal.get_ingredients() == ["bacon", "eggs", "butter", "cheese", "blue berries"])


def test_recipe_remove_ingredient():
    meal = RecipeBook.Recipe(["bacon", "eggs", "butter", "cheese"])
    assert(meal.get_ingredients() == ["bacon", "eggs", "butter", "cheese"])
    meal.remove_ingredient("bacon")
    assert(meal.get_ingredients() == ["eggs", "butter", "cheese"])


def test_recipe_add_to_grocery_list():
    glist = GroceryList.GroceryList()
    meal = RecipeBook.Recipe(["bacon", "eggs", "butter", "cheese"])
    meal.add_to_grocery_list(glist)
    assert(glist.get_items() == ["bacon", "eggs", "butter", "cheese"])


def test_recipe_book_add():
    breakfast = RecipeBook.Recipe(["bacon", "eggs", "butter", "cheese"])
    lunch = RecipeBook.Recipe(["ham", "cheese", "mayo", "bread"])

    book = RecipeBook.RecipeBook()
    book.add_recipe(breakfast)
    book.add_recipe(lunch)
    assert(book.get_recipes() == [breakfast, lunch])


def test_recipe_book_remove():
    breakfast = RecipeBook.Recipe(["bacon", "eggs", "butter", "cheese"])
    book = RecipeBook.RecipeBook()
    book.add_recipe(breakfast)
    assert(book.get_recipes() == [breakfast])
    book.remove_recipe(breakfast)
    assert(book.get_recipes() == [])


def test_grocery_list_add():
    glist = GroceryList.GroceryList()
    glist.add_item("milk")
    glist.add_item("water")
    assert(glist.get_items() == ["milk", "water"])


def test_grocery_list_remove():
    glist = GroceryList.GroceryList()
    glist.add_item("milk")
    glist.add_item("water")
    assert(glist.get_items() == ["milk", "water"])
    glist.remove_item("milk")
    assert(glist.get_items() == ["water"])
