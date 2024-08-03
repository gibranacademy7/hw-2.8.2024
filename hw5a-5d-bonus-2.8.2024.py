# hw-5a:   מיון רשימה של ערים לפי קריטריונים שונים

cities = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]


# a. אורך שם העיר
sorted_by_length = sorted(cities, key=lambda city: len(city));
# המפתח (key) הוא פונקציה שמקבלת שם עיר ומחזירה את אורך השם שלה. כך הערים ממוינות לפי האורך שלהן מהקצרה לארוכה
print("Sorted by length:", sorted_by_length);

# b. האות האחרונה של שם העיר
sorted_by_last_letter = sorted(cities, key=lambda city: city[-1]);
print("Sorted by last letter:", sorted_by_last_letter);

# c. שם העיר בסדר אותיות הפוך
sorted_by_reverse_name = sorted(cities, key=lambda city: city[::-1]);
print("Sorted by reverse name:", sorted_by_reverse_name);

# -----------------------------------------------------------------------
# d. Bonus: מיון רשימת ערים לפי קריטריונים שונים, כולל מרחק ויבשת
cities_with_details = [
    ["Tokyo", 5760, "Asia"],
    ["New York", 5690, "North America"],
    ["Paris", 2050, "Europe"],
    ["London", 2240, "Europe"],
    ["Sydney", 8780, "Australia"],
    ["Dubai", 1300, "Asia"],
    ["Shanghai", 4920, "Asia"]
]

# א. מיין לפי המרחק מישראל
sorted_by_distance = sorted(cities_with_details, key=lambda x: x[1]);
print("Sorted by distance:", sorted_by_distance);

# ב. מיין לפי המרחק מישראל מהגדול לקטן
sorted_by_distance_desc = sorted(cities_with_details, key=lambda x: x[1], reverse=True);
print("Sorted by distance descending:", sorted_by_distance_desc);

# ג. מיין לפי שם היבשת
sorted_by_continent = sorted(cities_with_details, key=lambda x: x[2]);
print("Sorted by continent:", sorted_by_continent);

# ד. מיין לפי שם היבשת ובמיון השני לפי המרחק
sorted_by_continent_then_distance = sorted(cities_with_details, key=lambda x: (x[2], x[1]));
print("Sorted by continent then distance:", sorted_by_continent_then_distance);
