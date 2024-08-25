temperature = float(input("Enter the temperature in degrees Celsius: "))

if temperature < 10:
  print("Wear a warm coat, scarf, and gloves.")
elif temperature < 15:
  print("Wear a jacket and sweater.")
elif temperature < 20:
  print("Wear a light jacket or sweater.")
else:
  print("Wear light clothes like a T-shirt and shorts.")