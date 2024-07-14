import json 

async def open_account(user):
    users=await get_bank_data()
    if str(user) in users:
        return False
    else:
        users[str(user)]={}
        users[str(user)]["Feed"]=0
        users[str(user)]["Pet"]=0
        users[str(user)]["Excerise"]=0
        users[str(user)]["Count"]=0
        users[str(user)]["Coin"]=0
        users[str(user)]["Coin_S"]=0
        users[str(user)]["Sleep"]=0
    with open(r"./data/users.json","w") as f:
        json.dump(users,f,indent=2)
    return True
        

async def get_bank_data():
    with open (r"./data/users.json","r") as f:
        users=json.load(f)
        return users 