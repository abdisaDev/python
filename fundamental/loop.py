#!/usr/bin/python3
user = {"abdizaDev": "developer", "abdisa": "human", "abdiza": "programmer"}

for name, role in user.copy().items():
    if role == "human":
        del user[name]
print(user)
