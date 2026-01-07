lkr_amount = float(input("Enter amount in LKR: "))
usd_amount = lkr_amount / 300
eur_amount = lkr_amount / 326
inr_amount = lkr_amount / 3.73

print(f"amount in USD: {usd_amount:.2f}\n"
      f"amount in EUR: {eur_amount:.2f}\n"
      f"amount in INR: {inr_amount:.2f}")

