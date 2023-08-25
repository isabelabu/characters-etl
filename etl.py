import pandas as pd

df = pd.read_csv('characters.csv')
chara_IDs = df['ID'].tolist()
print(chara_IDs)

insert_statements = []
for index, row in df.iterrows():
    values = ', '.join([f"'{value}'" for value in row])
    insert_statement = f"INSERT INTO character (character_id, character_name, character_model, character_hp, character_atk, character_def, character_weapon) VALUES ({values})"
    insert_statements.append(insert_statement)

with open('game-db.sql', 'w') as file:
    file.write("CREATE TABLE character")
    
    for statement in insert_statements:
        file.write(statement + '\n')
