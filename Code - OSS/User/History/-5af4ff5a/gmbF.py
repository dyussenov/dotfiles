from faker import Faker

fake = Faker()

with open('db.txt', 'w',encoding='utf8') as f:
    for _ in f:
        f.write(fake.name)