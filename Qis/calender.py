from calendar import TextCalendar

ano = int(input("Digite o ano: "))  # Corrected prompt for clarity

cal = TextCalendar()
print(cal.formatyear(ano, 2, 1, 8, 3))  # Prints the formatted calendar for the year
