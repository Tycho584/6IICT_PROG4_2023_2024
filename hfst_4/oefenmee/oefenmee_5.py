lengte_m = "1.4" # Lengte opgegeven door gebruiker.

try:
    lengte_cm = int(lengte_m)*100
except ValueError:
    "TODO: voeg hier code toe om het probleem op te lossen."

print(f"Je bent {lengte_cm} centimeter lang.")