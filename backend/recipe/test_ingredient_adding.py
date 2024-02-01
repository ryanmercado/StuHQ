import RecipeBook
import GroceryList
import Stock


def test_recipe():
    meal = RecipeBook.Recipe("breakfast", ["bacon", "eggs", "butter", "cheese"])
    assert(meal.get_ingredients() == ["bacon", "eggs", "butter", "cheese"])


def test_recipe_add_ingredient():
    meal = RecipeBook.Recipe("meal", ["bacon", "eggs", "butter", "cheese"])
    assert(meal.get_ingredients() == ["bacon", "eggs", "butter", "cheese"])
    meal.add_ingredient("blue berries")
    assert(meal.get_ingredients() == ["bacon", "eggs", "butter", "cheese", "blue berries"])


def test_recipe_remove_ingredient():
    meal = RecipeBook.Recipe("breakfast", ["bacon", "eggs", "butter", "cheese"])
    assert(meal.get_ingredients() == ["bacon", "eggs", "butter", "cheese"])
    meal.remove_ingredient("bacon")
    assert(meal.get_ingredients() == ["eggs", "butter", "cheese"])


def test_recipe_add_to_grocery_list():
    stock = Stock.Stock()
    glist = GroceryList.GroceryList()
    meal = RecipeBook.Recipe("breakfast", ["bacon", "eggs", "butter", "cheese"])
    glist.add_recipe_ingredients(meal, stock)
    assert(glist.get_items() == ["bacon", "eggs", "butter", "cheese"])


def test_recipe_book_add():
    breakfast = RecipeBook.Recipe("breakfast", ["bacon", "eggs", "butter", "cheese"])
    lunch = RecipeBook.Recipe("lunch", ["ham", "cheese", "mayo", "bread"])

    book = RecipeBook.RecipeBook()
    book.add_recipe(breakfast)
    book.add_recipe(lunch)
    assert(book.get_recipes() == [breakfast, lunch])


def test_recipe_book_remove():
    breakfast = RecipeBook.Recipe("breakfast", ["bacon", "eggs", "butter", "cheese"])
    book = RecipeBook.RecipeBook()
    book.add_recipe(breakfast)
    assert(book.get_recipes() == [breakfast])
    book.remove_recipe(breakfast)
    assert(book.get_recipes() == [])


def test_grocery_list_add():
    stock = Stock.Stock()
    glist = GroceryList.GroceryList()
    glist.add_item("milk", stock)
    glist.add_item("water", stock)
    assert(glist.get_items() == ["milk", "water"])


def test_grocery_list_remove():
    stock = Stock.Stock()
    glist = GroceryList.GroceryList()
    glist.add_item("milk", stock)
    glist.add_item("water", stock)
    assert(glist.get_items() == ["milk", "water"])
    glist.remove_item("milk")
    assert(glist.get_items() == ["water"])


def test_stock_add_item():
    stock = Stock.Stock()
    glist = GroceryList.GroceryList()
    glist.add_item("milk", stock)
    glist.purchased_item("milk", stock)
    assert(stock.get_items() == ["milk"])


def test_stock_add_items():
    stock = Stock.Stock()
    glist = GroceryList.GroceryList()
    glist.add_item("milk", stock)
    glist.add_item("water", stock)
    glist.purchased_items(["milk", "water"], stock)
    assert(stock.get_items() == ["milk", "water"])


def test_stock_remove_item():
    stock = Stock.Stock()
    stock.add_item("water")
    assert(stock.get_items() == ["water"])
    stock.remove_item("water")
    stock.remove_item("food")   # removing something that is not in it to make sure it doesn't fail
    assert(stock.get_items() == [])


def test_stock_remove_items():
    stock = Stock.Stock()
    stock.add_items(["water", "milk", "cheese"])
    assert(stock.get_items() == ["water", "milk", "cheese"])
    stock.remove_items(["water", "milk", "food"])   # add one in that doesnt exist to make sure it does not fail
    assert(stock.get_items() == ["cheese"])


def test_add_recipe_ingredients():
    stock = Stock.Stock()
    stock.add_item("milk")
    glist = GroceryList.GroceryList()
    meal = RecipeBook.Recipe("meal", ["water", "milk", "cookies"])
    glist.add_recipe_ingredients(meal, stock)
    assert(glist.get_items() == ["water", "cookies"])