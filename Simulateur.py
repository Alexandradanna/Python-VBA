import matplotlib.pyplot as plt

# Paramètres d'entrée
monthly_saving = 200
annual_interest_rate = 5
years = 10

months = years * 12
monthly_rate = annual_interest_rate / 12 / 100
capital = 0
capital_progression = []

for month in range(1, months + 1):
    capital = capital * (1 + monthly_rate) + monthly_saving
    capital_progression.append(capital)

final_amount = round(capital, 2)
print(f"\n📈 Capital final après {years} ans : {final_amount} €")

plt.figure(figsize=(10, 5))
plt.plot(range(1, months + 1), capital_progression, label="Capital accumulé", color='green')
plt.title("Évolution du capital dans le temps")
plt.xlabel("Mois")
plt.ylabel("Montant (€)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
