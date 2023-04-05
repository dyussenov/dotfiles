from faker import Faker

with open('quotes.txt', encoding='utf8') as f:
    for line in f:
        print(line.strip())