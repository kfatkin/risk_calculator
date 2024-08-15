futures = input('Trading futures or options (Type "f" for futurues or "o" for options)\n')
if futures.lower() == "f":
  print("Trading futures")
  contract_value = input("Contract value per point?\n")
  contract_value = round(int(contract_value),2)
  total_drawdown = input("Available account drawdown?\n")
  total_drawdown = round(int(total_drawdown), 2)
  if total_drawdown <= 5000:
    risk = round(0.07 * total_drawdown, 2)
    print("Risk is " + str(risk))
  elif total_drawdown > 5000 & total_drawdown <= 10000:
    risk = round(0.05 * total_drawdown, 2)
    print("Risk is " + str(risk))
  else:
    risk = round(0.02 * total_drawdown, 2)
    print("Risk is " + str(risk))
  stop_size = input("How many points does your stop need to be?\n")
  stop_size = int(stop_size)
  position_size = round(risk / (contract_value * stop_size))
  print("You can take up to this many contracts:" + str(position_size))
  print("For pyramiding, use " + str(position_size / 2) + "for first pyramid.")
  print("Use " + str(position_size / 4) + "for second pyramid.")
elif futures.lower() == "o":
  print("Trading options")
  contract_value = input("Price of one contract at entry point\n")
  contract_value = round(int(contract_value),2)
  total_drawdown = input("Available account drawdown?\n")
  total_drawdown = round(int(total_drawdown),2)
  if total_drawdown <= 5000:
    risk = round(0.07 * total_drawdown,2)
    print("Risk is " + str(risk))
  elif total_drawdown > 5000 & total_drawdown <= 10000:
    risk = round(0.05 * total_drawdown,2)
    print("Risk is " + str(risk))
  else:
    risk = round(0.02 * total_drawdown,2)
    print("Risk is " + str(risk))
  # CHANGE THIS TO WHAT PERCENTAGE OF CONTRACT ARE YOU RISKING THEN DERIVE # OF PTS BEING RISKED FOR FUTURE CALCULATIONS
  stop_size = input("How many points per contract are you risking?\n")
  stop_size = int(stop_size)
  max_contracts = round(total_drawdown / contract_value)
  position_size = round(risk / stop_size)
  print("Max number of contracts you can afford: " + str(max_contracts))
  print("Max number of contracts based on risk parameters: " + str(position_size))
  print("You will use " + str((position_size / max_contracts) * 100) + "% of the availible accounts capital on this trade")
else:
  print("Invalid input")