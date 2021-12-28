from numpy import False_
import pandas as pd
import re


df = pd.read_excel("Bundesliga Spectator Statistics.xlsx")
df["Best supported club"][10] = "Borussia Dortmund"
df["Best supported club"][9] = "Bayern Munich"
df["Best supported club"][9].strip("")

dfStyler = df.style.set_properties(subset = ['Best supported club'], ** {
   'text-align': 'left'
})

df.to_excel("Bundesliga Spectator Statistics update.xlsx", index=False)

# The Bundesliga , sometimes referred to as the Fußball-Bundesliga or Bundesliga , is a professional association football league in Germany. At the top of the German football league system, the Bundesliga is Germany's primary football competition. The Bundesliga comprises 18 teams and operates on a system of promotion and relegation with the  Bundesliga.