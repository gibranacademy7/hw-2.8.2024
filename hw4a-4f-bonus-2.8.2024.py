#hw.4a:

fruits = ["Mango", "Orange", "Banana", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"]

#  כדי להפוך את סדר האותיות של כל פרי
reversed_fruits = list(map(lambda fruit: fruit[::-1], fruits))
print("Fruit`s names in revers are: ", reversed_fruits);

#or:
for item in map(lambda fruit: fruit[::-1], fruits):
    print(item);

#----------------------------------------------------------------------------------
#hw.4b:
#fruits = ["Mango", "Orange", "Banana", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"]

first_letters = list(map(lambda fruit: fruit[0], fruits));
print("first letter of every fruit is: ", first_letters);
#-----------------------------------------------------------------------------------
#hw.4c:
#fruits = ["Mango", "Orange", "Banana", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"]

uppercase_fruits = list(map(lambda fruit: fruit.upper(), fruits));
print("Fruits`s names in upper: ", uppercase_fruits);
#------------------------------------------------------------------------------

#hw.4d:
#fruits = ["Mango", "Orange", "Banana", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
lengths_of_fruits: int = list(map(lambda fruit: len(fruit), fruits));
print(lengths_of_fruits);
#-------------------------------------------------------------------------------

#hw.4e:
#fruits = ["Mango", "Orange", "Banana", "Apple", "Strawberry", "Pineapple", "Grapes", "Watermelon"]

updated_fruits = list(map(lambda fruit: fruit + '!' if fruit.endswith('s') else fruit, fruits));
print(updated_fruits);
#--------------------------------------------------------------------------------------------------

#hw.4f-1     יצירת רשימה חדשה שתכיל רק את מספר הקלוריות

fruit_calories = [["Apple", 52], ["Banana", 89], ["Orange", 47], ["Mango", 60], ["Strawberry", 32], ["Pineapple", 50], ["Grapes", 69], ["Watermelon", 30]]

calories_list = list(map(lambda fruit: fruit[1], fruit_calories));

print("Calories only: ", calories_list);
#--------------------------------------------

#hw.4f-2    יצירת רשימה חדשה עם שם הפרי ומספר הקלוריות מחוברים
# שימוש ב-map ו-lambda כדי לחבר את שם הפרי ומספר הקלוריות
combined_list = list(map(lambda fruit: fruit[0] + str(fruit[1]), fruit_calories));

print(combined_list);
#----------------------------------------------

#hw.4f-3    יצירת רשימה זהה אבל אם הפרי מעל 50 קלוריות הוסף סימן קריאה לשם שלו אחרת אותו דבר

combined_list_with_exclamation = list(map(lambda fruit: fruit[0] + str(fruit[1]) + '!' if fruit[1] > 50 \
    else fruit[0] + str(fruit[1]), fruit_calories))

print(combined_list_with_exclamation);
#--------------------------------------------------------------------------------------------------------------