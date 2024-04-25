import sqlite3
"""
We are going to create a database of 3 tables

Table 1: Animal
- ID
- Name
- Type
- Age


Table 2: Owner
- Name
- Animal
- Phone
- Vet

Table 3: Vet Name
- Vet ID
- Vet Name

"""

table1_name = "Animal"

table1_column = "ID INT, Name TEXT, Type TEXT, Age INT"

Table1_data = [
    '11, "Hello", "Cat", 1', 
    '12, "Barkley", "Dog", 12',
    '13, "Lizzy", "Lizard", 5',
    '14, "Sir Ham", "Hamster", 7',
    '15, "Fred", "Cat", 1',
    '16, "Hops Scotch", "Rabbit", 2',
    '17, "Ogg", "Dog", 18',
    '18, "Meowphistopheles", "Cat", 3',
    '19, "Leopold", "Lizard", 4',
]

table2_name = "Owner"

table2_column = "Name TEXT, AnimalID INT, Phone INT, VetID INT"

Table2_data = [
    "'Muffin Clara',    11, '583-246-7562', 1",
    "'Chelsy Abramzon', 12, '719-863-0878', 2",
    "'William Laws',    13, '820-991-5263', 3",
    "'Meriel Hasling',  14, '184-464-0150', 4",
    "'Colleen Peacey',  15, '363-974-6649', 5",
    "'Grace Cuzen',     16, '998-698-1577', 1",
    "'Nyssa Roantree',  17, '262-487-0447', 2",
    "'Peggy MacLaren',  18, '275-819-3445', 4",
    "'Tani Millam',     19, '460-980-7084', 5"
]

table3_name = "Vet"

table3_column = "VetID INT, VetName Text"

Table3_data = [
    '1, "Hello Kittys Vet Shop"',
    '2, "Baker Dozen"',
    '3, "Cat Place by Teresa"',
    '4, "The Cuddle Clinic"',
    '5, "Take Paws and Enjoy Medicine"'
]



def createDatabase(path):
    database = sqlite3.connect(path)
    return database, database.cursor()
    """
    Given the path for the database, create the database and 
    pass back the connection to the database and cursor to the database. 
    """
    # TODO


def createTable(cursor, tableName, columns):
    cursor.execute(f'CREATE TABLE {tableName} ({columns})')
    """
    Given the cursor, the table, and the string with the columns, create the table in the database. 

    This will also handle REMOVING the table if it already exists. 

    columns example:
    str = "c1 TEXT, c2 INT, c3 INT"
    """
    # TODO


def insertValues(cursor, tableName, valueString):
    cursor.execute(f'INSERT INTO {tableName} VALUES ({valueString})')
    """
    Given the database cursor, the table name, and the values to add
    """
    # TODO



def queryStatement(theSelect, theFrom, theWhere=""):
    query = f'SELECT {theSelect} FROM {theFrom}'
    if theWhere != "":
        query += f' WHERE {theWhere}'
    return query
    """
    Given a query to run on the database, return the results.

    You are potentially given queries that do not have a where statement
    """
    # TODO



if __name__ == "__main__":
    path = "Laboratory/Lab10/ourDB.db"
    ### Creating the Database
    db_connection, theCursor = createDatabase(path)

    ### Creating the Tables
    createTable(theCursor, table1_name, table1_column)
    createTable(theCursor, table2_name, table2_column)
    createTable(theCursor, table3_name, table3_column)



    ### Inserting the values
    #### Table 1
    for values in Table1_data:
        insertValues(theCursor, table1_name, values)

    

    #### Table 2
    for values in Table2_data:
        insertValues(theCursor, table2_name, values)


    #### Table 3 
    for values in Table3_data:
        insertValues(theCursor, table3_name, values)


    ### Random Query Statements
    

    print("Query 1")
    print("~"*40)
    # TODO, we need to get a query that:
    # - gets the owner name, the animal name 
    # - from the corresponding tables
    # - if the animal is a "Cat"
    # - And the animal belongs to the owner

    query = queryStatement("Owner.Name, Animal.Name", "Owner, Animal", "Owner.AnimalID == Animal.ID AND Animal.Type == 'Cat'") # TODO: Fill this in
    for x in theCursor.execute(query):
        print(x)
    
    print("\n"*3)

    ################################################################

    print("Query 2")
    print("~"*40)
    # TODO, we need to get a query that:
    # - gets the owner name and the animal name
    # - from the corresponding tables
    # - under the condition that the animal is <= 3
    # - and the animal belongs to that owner

    query = queryStatement("Owner.Name, Animal.Name", "Owner, Animal", "Animal.Age<=3 AND Owner.AnimalID ==Animal.ID") # TODO: Fill this in
    for x in theCursor.execute(query):
        print(x)
    
    print("\n"*3)


    ################################################################
    print("Query 3")
    print("~"*40)

    # TODO, we need to get a query that:
    # - gets the number (i.e. count) of vets
    # - from the corresponding tables
    # - under the condition that the vet hosts at least two clients
    # - and these clients are distinct

    query = queryStatement("COUNT(DISTINCT Vet.VetID)", "Vet, Owner o1, Owner o2", "Vet.VetID == o1.VetID AND Vet.VetID == o2.VetID AND o1.Name != o2.Name") # TODO: Fill this in
    for x in theCursor.execute(query):
        print(x)
    
    print("\n"*3)