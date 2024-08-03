# צור רשימה של 50 מספרים אקראיים בין 1-100 והדפס אותה
import random
random_numbers = [random.randint(1, 100) for _ in range(50)];
print("50 random numbers of 100: ", random_numbers);

# 1a: לקבל מתוך הרשימה רק מספרים הגדולים מ- 50
filtered_numbers = list(filter(lambda x: x > 50, random_numbers));
print("Numbers up to 50 are: ", filtered_numbers);

# 1b:  לקבל מתוך הרשימה רק מספרים המתחלקים ב - 7 ללא שארית
filtered_division = list(filter(lambda x: x % 7 == 0, random_numbers));
print("Numbers divisible by 7 are: ", filtered_division);
#another option:
filtered_division_2 = list(filter(lambda x: x %7 == 0, filtered_numbers));
print(" Filtered numbers divisible by 7 are: ",filtered_division_2);

# 1c: לקבל מתוך הרשימה רק מספרים דו- ספרתיים
filtered_two_digit_numbers = list(filter(lambda x: 10 <= x <= 99, random_numbers));
print("filtered two digit numbers are: ", filtered_two_digit_numbers);

# 1d: לקבל מתוך הרשימה רק מספרים דו- ספרתיים שספרת האחדות שלהם שווה לספרת העשרות שלהם
filtered_identical_double_digit_numbers = list(filter(lambda x: 10 <= x <= 99 and (x // 10) == (x % 10), random_numbers));
print("Filtered identical double digit numbers are: ", filtered_identical_double_digit_numbers);

# 1e: לקבל מתוך הרשימה רק מספרים שסכום הספרות שלהם הוא 9
filtered_sum_9_numbers = list(filter(lambda x: 10 <= x <= 99 and (x // 10) + (x % 10) == 9, random_numbers));
print("Digits of a two-digit number = 9: ", filtered_sum_9_numbers);

# 1f: לקבל מתוך הרשימה רק מספרים הגדולים מהממוצע 9
average = sum(random_numbers) / len(random_numbers);
filtered_above_average_numbers = list(filter(lambda x: x > average, random_numbers));
print("Average is: ", average); #לא הכרחי אך נחמד לדעת
print("Above average numbers is: ", filtered_above_average_numbers);

# 1g: לקבל מתוך הרשימה רק מספרים הגדולים מחצי של המספר המקסימלי ברשימה
max_number = max(random_numbers);
half_max_number = max_number / 2;
filtered_above_half_max = list(filter(lambda x: x > half_max_number, random_numbers));
print("Maximum Number is: ", max_number); # תוספת מידע
print("Half maximum number is: ", half_max_number); # תוספת מידע
print(" Numbers above half maximum are: ", filtered_above_half_max);

# 1h: חישוב החציון

sorted_numbers = sorted(random_numbers);
n = len(sorted_numbers);
if n % 2 == 1:
    # אם מספר האיברים אי-זוגי, החציון הוא האיבר האמצעי
    median = sorted_numbers[n // 2];
else:
    # אם מספר האיברים זוגי, החציון הוא ממוצע של שני האיברים האמצעיים
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2;

# סינון הרשימה כך שתכיל רק את המספרים הגדולים מהחציון
filtered_above_median = list(filter(lambda x: x > median, random_numbers));

# הדפסת הרשימה המסוננת (מספרים הגדולים מהחציון)
print("Filtered list: numbers greater than the median = ", filtered_above_median);

# ----------------------------------------------------------------------------------
# 1j:

# פונקציה המקבלת מספר ומחזירה אמת אם הוא ראשוני ושקר אם לא
def is_prime(n):
    """Check if a number is a prime number!"""
    if n <= 1:          #בדיקה אם n קטן או שווה ל-1 / מספרים קטנים או שווים ל-1 אינם ראשוניים
        return False
    if n == 2:          # 2 הוא המספר הראשוני הקטן ביותר
        return True
    if n % 2 == 0:      # כל המספרים הזוגיים הגדולים מ-2 אינם ראשוניים
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        """
        מחלקים את n בכל המספרים האי-זוגיים מ-3 ועד לשורש הריבועי של n
אם נמצא מספר שמחלק את n ללא שארית, n אינו ראשוני ומחזירים False        
        אם לא נמצא אף מספר כזה, n ראשוני ומחזירים True
        """

        if n % i == 0:
            return False
    return True;


filtered_prime_numbers = list(filter(lambda x: is_prime(x), random_numbers));
print("Filtered list: prime numbers = ", filtered_prime_numbers);




