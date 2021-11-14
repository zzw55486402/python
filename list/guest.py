guest = ["shinyruo", "zzw", "qaq"]
print(guest[0] + " with me eat dinner")
print(guest[1] + " with me eat dinner")
print(len(guest))
print(guest[2] + " with me eat dinner\n")

print(guest[2] + " did not with me eat dinner\n")
guest[2] = "qvq"
print(guest[0] + " with me eat dinner")
print(guest[1] + " with me eat dinner")
print(guest[2] + " with me eat dinner")

print("I want to invite more people eat dinner\n")
guest.insert(0, "otto")
guest.insert(2, "mid")
guest.append("last")
print(guest[0] + " with me eat dinner")
print(guest[1] + " with me eat dinner")
print(guest[2] + " with me eat dinner")
print(guest[3] + " with me eat dinner")
print(guest[4] + " with me eat dinner")
print(guest[5] + " with me eat dinner")

print("Because dinner table so small\n")
p = guest.pop()
print(p + "sorry i can not with you eat dinner")
p = guest.pop()
print(p + "sorry i can not with you eat dinner")
p = guest.pop()
print(p + "sorry i can not with you eat dinner\n")
p = guest.pop()
print(p + "sorry i can not with you eat dinner\n")

print(guest[0] + "i want to eat dinner with you")
print(guest[1] + "i want to eat dinner with you\n")

del guest[0]
del guest[0]
print(guest)