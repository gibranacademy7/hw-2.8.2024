import random

# יצירת רשימה של 20 מספרים אקראיים בין -50 ל-50
numbers = [random.randint(-50, 50) for _ in range(20)];
print("Random list: ", numbers);

# הגדרת הפונקציה להפיכת סדר הספרות
def reverse_number(num):
    num_str = str(num);         # ממיר את המספר למחרוזת כדי שנוכל להפוך את סדר הספרות
    if num_str[0] == '-':  # בודק אם המחרוזת מתחילה בסימן מינוס, מה שמעיד על כך שהמספר שלילי
        reversed_str = '-' + num_str[:0:-1];
        # הפיכת החלק המספרי: חלק מהמחרוזת ללא הסימן השלילי, הופך את סדר הספרות
        # '-' + ...: מוסיף חזרה את הסימן השלילי בתחילת המחרוזת
    else:
        reversed_str = num_str[::-1];  # הופך את סדר הספרות של המחרוזת כולה
    return (reversed_str);   # ממיר את המחרוזת חזרה למספר שלם
#or:
    #return int(reversed_numbers);

# שימוש ב-map כדי להפוך את סדר הספרות של כל מספר
reversed_numbers = list(map(reverse_number, numbers));
print("List with numbers in reverse order: ", reversed_numbers);
#or:
for item in map (reverse_number, numbers):
    print(item);
