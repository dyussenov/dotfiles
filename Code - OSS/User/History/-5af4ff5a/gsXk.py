from faker import Faker

fake = Faker('en_US')

with open('db.txt', 'w',encoding='utf8') as f:
    for _ in range(100):
        f.write(f'{fake.name()[0]},{fake.name()[1]},{fake.phone_number()},{fake.ascii_email()}'+'\n')