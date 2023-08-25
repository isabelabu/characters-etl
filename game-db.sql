CREATE TABLE character(
    character_id INT PRIMARY KEY,
    character_name VARCHAR(40),
    character_model VARCHAR(20),
    character_hp INT,
    character_atk INT,
    character_def INT,
    character_weapon VARCHAR(30)
);

INSERT INTO character (character_id, character_name, character_model, character_hp, character_atk, character_def, character_weapon) VALUES ('1', ' Tulip', ' Girl', '100', '60', '75', ' Bow');
INSERT INTO character (character_id, character_name, character_model, character_hp, character_atk, character_def, character_weapon) VALUES ('2', ' Pupa', ' Woman', '100', '80', '50', ' Sword');
INSERT INTO character (character_id, character_name, character_model, character_hp, character_atk, character_def, character_weapon) VALUES ('3', ' Dux', ' Boy', '100', '80', '60', ' Shotgun');
INSERT INTO character (character_id, character_name, character_model, character_hp, character_atk, character_def, character_weapon) VALUES ('4', ' Vyn', ' Man', '100', '50', '80', ' Darts');
