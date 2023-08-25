import pandas as pd

df = pd.read_csv('characters.csv')

insert_statements = []
for index, row in df.iterrows():
    values = ', '.join([f"'{value}'" for value in row])
    insert_statement = f"INSERT INTO character (character_id, character_name, character_model, character_hp, character_atk, character_def, character_weapon) VALUES ({values});"
    insert_statements.append(insert_statement)

with open('game-db.sql', 'w') as file:
    file.write('''CREATE TABLE character(
    character_id INT PRIMARY KEY,
    character_name VARCHAR(40),
    character_model VARCHAR(20),
    character_hp INT,
    character_atk INT,
    character_def INT,
    character_weapon VARCHAR(30)
);

''')
    
    for statement in insert_statements:
        file.write(statement + '\n')
