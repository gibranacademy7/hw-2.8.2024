# יצירת רשימה של הוצאות והכנסות חודשיות
monthly_transactions = [
    [10000, 7000],
    [300, 5000],
    [2000, 8000]
];

# חישוב המאזן החודשי
monthly_balances = [income - expense for income, expense in monthly_transactions];
print("Monthly balances:", monthly_balances);

#or:
monthly_balances = list(map(lambda x: x[0] - x[1], monthly_transactions));
print("Monthly balances:", monthly_balances);

#or:
for item in map (lambda x: x[0] - x[1], monthly_transactions):
    print(item);

