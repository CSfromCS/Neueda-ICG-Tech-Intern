country = input("Please enter your country: ")

if country in ("Netherlands", "Belgium", "Luxembourg"):
  print("Lowlands country");

elif country in ("Norway", "Sweden", "Denmark", "Finland"):
  print("Nordic country")

elif country in ("England", "Scotland", "Wales", "Northern Ireland"):
  print("UK country")

else:
  print("%s isn't classified in this particular application!" % country)
  
