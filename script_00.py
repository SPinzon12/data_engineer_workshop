import mysql.connector
import pandas as pd
import json

def create_connection(host='localhost', user='', password='', database=''):
    try:
        cnx = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print('Conexion exitosa!!')
    except mysql.connector.Error as e:
        cnx = None
        print('No se puede conectar:', e)
    return cnx

def create_table(cnx):
    cursor = cnx.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Candidates (
        CandidateID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        FirstName VARCHAR(255) NOT NULL,
        LastName VARCHAR(255) NOT NULL,
        Email VARCHAR(255) NOT NULL,
        ApplicationDate DATE NOT NULL,
        Country VARCHAR(255) NOT NULL,
        YearsOfExperience INT NOT NULL,
        SeniorityLevel VARCHAR(255) NOT NULL,
        TechnologyStack VARCHAR(255) NOT NULL,
        CodeChallengeScore TINYINT NOT NULL,
        TechnicalInterviewScore TINYINT NOT NULL,
        IsHired BOOLEAN NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    cnx.commit()
    cursor.close()
    print('Tabla creada exitosamente')

def calculate_is_hired(row):
    return row["CodeChallengeScore"] >= 7 and row["TechnicalInterviewScore"] >= 7

def insert_data(cnx, df):
    cursor = cnx.cursor()
    insert_query = """
    INSERT INTO candidates (FirstName, LastName, Email, ApplicationDate, Country, YearsOfExperience, SeniorityLevel, TechnologyStack, CodeChallengeScore, TechnicalInterviewScore, IsHired)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for index, row in df.iterrows():
        data = (row["FirstName"], row["LastName"], row["Email"], row["ApplicationDate"], row["Country"],
                row["YOE"], row["Seniority"], row["Technology"], row["CodeChallengeScore"], row["TechnicalInterviewScore"], row["IsHired"])
        cursor.execute(insert_query, data)
    cnx.commit()
    cursor.close()
    print("Datos insertados exitosamente desde el DataFrame.")

if __name__=="__main__":
    with open('db_config.json') as file:
        config = json.load(file)
    cnx = create_connection(user=config["user"], password=config["password"], database='mydatabase')
    if cnx:
        create_table(cnx)
        candidates_df = pd.read_csv("./data/candidates.csv", delimiter=';')
        candidates_df.columns = candidates_df.columns.str.replace(' ', '')
        candidates_df["IsHired"] = candidates_df.apply(calculate_is_hired, axis=1)
        insert_data(cnx, candidates_df)
        cnx.close()    