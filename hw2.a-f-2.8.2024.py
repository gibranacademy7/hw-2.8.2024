# יצירת רשימת המשחקים
games = ["Grand Theft Auto V", "Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"];

# 2a: כדי לקבל משחקים עם שמות גדולים מ-8 אותיות
filtered_games = list(filter(lambda game: len(game) > 8, games));

print("Games have more than 8 letters are: ", filtered_games);
#------------------------------------------------------------------------------

# 2b: כדי לקבל משחקים עם שמות גדולים מ-8 אותיות
filtered_games = list(filter(lambda game: game.startswith('F'), games));
print("Games start with letter 'F': ", filtered_games);
# or:
result = ', '.join(filtered_games);
print("Games start with letter 'F': ",result);
#------------------------------------------------------------------------------

# 2c: כדי לקבל משחקים ששמם מכיל בדיוק 2 מילים
filtered_games = list(filter(lambda game: len(game.split()) == 2, games));
print("Games consisting of only two words: ", filtered_games);
# or:
result = ', '.join(filtered_games);
print("Games consisting of only two words: ", result);
#---------------------------------------------------------------------------------

# 2d: V כדי לקבל משחקים ששמם מכיל את האות
filtered_games = list(filter(lambda game: 'v' in game.lower(), games));
result = ', '.join(filtered_games);
print("Games containing the letter v: ", result);
#--------------------------------------------------------------------------------------
# 2e:  ":!^&*" רק משחקים המכילים תוים מיוחדים כגון

special_characters = ":!^&*"
filtered_games = list(filter(lambda game: any(char in special_characters for char in game), games));
print("Games containing special characters: ", filtered_games);

# 2f:  יצירת רשימת המשחקים עם השנים
#
games_with_years = [
    ["Grand Theft Auto V", 2013],
    ["Fortnite", 2017],
    ["The Elder Scrolls V: Skyrim", 2011],
    ["Dark Souls", 2011],
    ["Overwatch", 2016]
]

# סינון המשחקים שיצאו אחרי שנת 2014
filtered_games = [game for game in games_with_years if game[1] > 2014];

# הצגת התוצאה
print("Games with years are: ", filtered_games);



