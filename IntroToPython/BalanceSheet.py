def balance_sheet(assets, liabilities, equity):
  total_assets = sum(assets.values())
  total_liabilities = sum(liabilities.values())
  total_equity = sum(equity.values())
  total_liabilities_and_equity = total_liabilities + total_equity
  
  print("ASSETS:")
  for asset in assets:
    print(f"{asset}: {assets[asset]}")
  print(f"Total Assets: {total_assets}")
  print()
  
  print("LIABILITIES:")
  for liability in liabilities:
    print(f"{liability}: {liabilities[liability]}")
  print(f"Total Liabilities: {total_liabilities}")
  print()
  
  print("EQUITY:")
  for eq in equity:
    print(f"{eq}: {equity[eq]}")
  print(f"Total Equity: {total_equity}")
  print()
  
  print(f"Total Liabilities and Equity: {total_liabilities_and_equity}")

# Prompt the user to enter the assets
assets = {}
print("Enter assets:")
while True:
  asset_name = input("Asset name (enter 'done' when finished): ")
  if asset_name.lower() == "done":
    break
  asset_value = float(input("Asset value: "))
  assets[asset_name] = asset_value

# Prompt the user to enter the liabilities
liabilities = {}
print("\nEnter liabilities:")
while True:
  liability_name = input("Liability name (enter 'done' when finished): ")
  if liability_name.lower() == "done":
    break
  liability_value = float(input("Liability value: "))
  liabilities[liability_name] = liability_value

# Prompt the user to enter the equity
equity = {}
print("\nEnter equity:")
while True:
  eq_name = input("Equity name (enter 'done' when finished): ")
  if eq_name.lower() == "done":
    break
  eq_value = float(input("Equity value: "))
  equity[eq_name] = eq_value

# Display the balance sheet
balance_sheet(assets, liabilities, equity)
