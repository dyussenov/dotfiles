from faker import Faker

fake = Faker('ru_Ru')

with open('db.txt', 'w',encoding='utf8') as f:
    for _ in range(100):
        f.write(fake.name())