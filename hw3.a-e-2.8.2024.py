# hw-3a:
import random
"""  
 יצירת רשימה של 20 מספרים אקראיים בין -50 ל- 50
"""

numbers = [random.randint(-50, 50) for _ in range(20)];
print("random_list: ", numbers);

# שימוש ב-map וב-lambda כדי לקבל רשימה חדשה שבה כל מספר הוא בחזקת 3
cubed_numbers = list(map(lambda x: x ** 3, numbers));
print("List with numbers to the 3rd power:", cubed_numbers);
#------------------------------------------------------------------------

# hw-3b:  ספרת האחדות של כל מספר
units_digits = list(map(lambda x: abs(x) % 10, cubed_numbers));
print("The numbers are: ", numbers); # תוספת/ לא הכרחי
print("The unity digit of any number in the 3rd power: ", units_digits);
#--------------------------------------------------------------------------

# hw-3c:  כל מספר בפרנהייט. כלומר להכפיל ב - 9/5 ולהוסיף 32
fahrenheit_numbers = list(map(lambda x: (x * 9 / 5) + 32, numbers));
print("List with numbers in Fahrenheit: ", fahrenheit_numbers);

# or: כל מספר בחזקת 3 בפרנהייט
# fahrenheit_numbers = list(map(lambda x: (x * 9 / 5) + 32, cubed_numbers));
# print("List with numbers ** 3 in Fahrenheit: ", fahrenheit_numbers);
#----------------------------------------------------------------------------

# hw-3d: כל מספר חיובי יהפוך למילה "positive "וכל מספר שלילי יהפוך למילה - "negative"
labels = list(map(lambda x: "positive" if x > 0 else "negative", numbers));
print("List with positive or negative labels: ", labels);
#or:
for item in map(lambda x: "positive" if x > 0 else "negative", numbers):
    print(item);
#----------------------------------------------------------------------------

# hw-3e:(מיין) היתר יישאר אותו דבר המספר הכי גדול יוחלף במילה (מאקס) והכי קטן במילה
max_value = max(numbers);
min_value = min(numbers);

# : המרת המספר הכי גדול ל-"max" והכי קטן ל-"min", היתר נשארים כפי שהם
replaced_values = list(map(lambda x: "max" if x == max_value else "min" if x == min_value else x, numbers));
print("List with the largest and smallest converted numbers: ", replaced_values);

# or:
for item in map (lambda x: "max" if x == max_value else "min" if x == min_value else x, numbers):
    print(item);
#----------------------------------------------------------------------------------



