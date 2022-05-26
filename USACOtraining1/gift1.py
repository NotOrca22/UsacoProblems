"""
ID: orcawha1
LANG: PYTHON3
TASK: gift1
"""
if __name__ == "__main__":
    with open("gift1.in", "r") as f1:
        n = int(f1.readline().strip())
        users = {}
        for i in range(n):
            name = f1.readline().strip()
            users[name] = 0
        # print(users)
        while True:
            try:
                name = f1.readline().strip()
                info = f1.readline().strip().split(" ")
                money, people = int(info[0]), int(info[1])
                try:
                    moneyPerPerson = money//people
                except:
                    moneyPerPerson = 0
                print(money, people, moneyPerPerson)
                recipents = []
                for i in range(people):
                    recipents.append(f1.readline().strip())
                # print(name in users.keys())
                users[name] = users[name] - moneyPerPerson * people
                for recipent in recipents:
                    users[recipent] += moneyPerPerson
            except:
                break
        with open("gift1.out", "w") as f2:
            for person in users.keys():
                f2.write(person + " " + str(users[person]) + "\n")