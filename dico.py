wd = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]

hs = ["hs_l", "hs_m", "hs_me", "hs_j", "hs_v"]

mix = []

for i in range(len(hs)):
    mix.append((wd[i], hs[i]))

print("list of pairs", mix, "\n\n")

dico = dict(mix)

print("dictionnaire", dico)

for day in wd:
    print(f"dico[{day}] = {dico[day]}", "\n")
