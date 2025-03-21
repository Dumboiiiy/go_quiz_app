import sqlite3

# Connect to the SQLite database
# conn = sqlite3.connect("test.db")
conn = sqlite3.connect(r"C:\My_coding_journey\Final_Projects\GO_Tutorial\go_beginner_project_techwithtim\test.db")
cursor = conn.cursor()


# List of 100 True/False questions with answers
questions = [
    ("The Earth is the third planet from the Sun.", 1),
    ("Humans have four lungs.", 0),
    ("Goldfish only have a three-second memory.", 0),
    ("The Great Wall of China is visible from space.", 0),
    ("Lightning never strikes the same place twice.", 0),
    ("A group of crows is called a murder.", 1),
    ("Bananas are berries.", 1),
    ("The Eiffel Tower grows taller in summer.", 1),
    ("Water expands when it freezes.", 1),
    ("Octopuses have three hearts.", 1),
    ("Honey never spoils.", 1),
    ("There are more stars in the universe than grains of sand on Earth.", 1),
    ("Birds are the only animals that can fly.", 0),
    ("The Amazon rainforest produces 20% of the world’s oxygen.", 0),
    ("Bats are blind.", 0),
    ("Humans share 50% of their DNA with bananas.", 1),
    ("A day on Venus is longer than a year on Venus.", 1),
    ("Sharks are mammals.", 0),
    ("The Moon orbits the Sun.", 0),
    ("The Pacific Ocean is the largest ocean on Earth.", 1),
    ("Mount Everest is the tallest mountain on Earth.", 1),
    ("Diamonds are made of compressed coal.", 0),
    ("Penguins can fly.", 0),
    ("The human body has 206 bones.", 1),
    ("The speed of light is faster than the speed of sound.", 1),
    ("A tomato is a vegetable.", 0),
    ("Humans have five senses.", 0),
    ("Pluto is still classified as a planet.", 0),
    ("The Statue of Liberty was a gift from France.", 1),
    ("Lightning is hotter than the surface of the Sun.", 1),
    ("The largest desert in the world is the Sahara Desert.", 0),
    ("Venus is the hottest planet in the Solar System.", 1),
    ("The Great Pyramid of Giza was built by aliens.", 0),
    ("Whales are fish.", 0),
    ("There are 24 hours in a day.", 1),
    ("An octopus can regrow a lost arm.", 1),
    ("Cows have four stomachs.", 1),
    ("It is impossible to sneeze with your eyes open.", 1),
    ("Sound travels faster in air than in water.", 0),
    ("The Atlantic Ocean is larger than the Pacific Ocean.", 0),
    ("Dolphins sleep with one eye open.", 1),
    ("The blue whale is the largest animal on Earth.", 1),
    ("The capital of Australia is Sydney.", 0),
    ("Pineapples grow on trees.", 0),
    ("Mars is red because of iron oxide (rust).", 1),
    ("The Earth's core is made of solid rock.", 0),
    ("There are seven continents on Earth.", 1),
    ("The human heart is on the left side of the chest.", 0),
    ("Butterflies taste with their feet.", 1),
    ("The Mona Lisa was painted by Vincent van Gogh.", 0),
    ("Jellyfish have brains.", 0),
    ("The speed of light is 299,792,458 meters per second.", 1),
    ("The capital of Canada is Toronto.", 0),
    ("Bamboo is the fastest-growing plant in the world.", 1),
    ("The unicorn is Scotland’s national animal.", 1),
    ("The Sahara Desert is the largest desert in the world.", 0),
    ("Snakes have eyelids.", 0),
    ("Ostriches can run faster than horses.", 1),
    ("A group of lions is called a pride.", 1),
    ("Venus is the only planet that rotates clockwise.", 1),
    ("The human skeleton is made entirely of bones.", 0),
    ("The world's smallest country is Monaco.", 0),
    ("Albert Einstein developed the theory of evolution.", 0),
    ("Bats are the only mammals capable of sustained flight.", 1),
    ("Caterpillars turn into butterflies.", 1),
    ("Horses sleep standing up.", 1),
    ("The longest river in the world is the Nile.", 1),
    ("A bee dies after it stings you.", 1),
    ("The human brain is fully developed at birth.", 0),
    ("Cheetahs are the fastest land animals.", 1),
    ("Sharks can live in freshwater.", 0),
    ("The Great Wall of China was built in a single year.", 0),
    ("Giraffes have the same number of neck vertebrae as humans.", 1),
    ("A year on Earth is exactly 365 days.", 0),
    ("Lightning travels upwards from the ground to the sky.", 0),
    ("The fastest animal in the world is the peregrine falcon.", 1),
    ("The square root of 4 is 3.", 0),
    ("Penguins can breathe underwater.", 0),
    ("The moon has no gravity.", 0),
    ("An ostrich’s eye is bigger than its brain.", 1),
    ("The human brain has four lobes.", 1),
    ("The fastest human can run faster than a car.", 0),
    ("Gold is heavier than lead.", 0),
    ("Venus is the brightest planet in the night sky.", 1),
    ("Some turtles can breathe through their butts.", 1),
    ("Antarctica is the driest place on Earth.", 1),
    ("The Amazon River is the longest river in the world.", 0),
    ("A chameleon changes color to blend with its surroundings.", 0),
    ("A lightning bolt is five times hotter than the surface of the sun.", 1),
    ("Some fish can breathe air.", 1),
    ("Humans and dinosaurs lived at the same time.", 0),
    ("There is gravity in space.", 1),
    ("Watermelons are 92% water.", 1),
    ("Chocolate is toxic to dogs.", 1),
    ("The Olympic Games originated in Greece.", 1),
    ("All tigers have the same stripe pattern.", 0),
    ("The unicorn is the national animal of Wales.", 0)
]


cursor.execute("DELETE FROM questions")  # Clears the table
cursor.executemany("INSERT INTO questions (question, answer) VALUES (?, ?)", questions)

try:
    cursor.executemany("INSERT INTO questions (question, answer) VALUES (?, ?)", questions)
    conn.commit()
    print("100 questions inserted successfully!")
except sqlite3.Error as e:
    print(f"SQLite error: {e}")
finally:
    print("Total questions in database:", cursor.fetchone()[0])
    cursor.execute("SELECT COUNT(*) FROM questions")
    conn.close()


cursor.execute("SELECT COUNT(*) FROM questions")