import psycopg2
import json

def create_connection():
    try:
        with open('db_config.json') as file:
            config = json.load(file)
        cnx = psycopg2.connect(
            host='localhost',
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        print('Conexión exitosa!!')
    except psycopg2.Error as e:
        cnx = None
        print('No se puede conectar:', e)
    return cnx

def create_table():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Candidates (
        CandidateID SERIAL PRIMARY KEY,
        FirstName VARCHAR(255) NOT NULL,
        LastName VARCHAR(255) NOT NULL,
        Email VARCHAR(255) NOT NULL,
        ApplicationDate DATE NOT NULL,
        Country VARCHAR(255) NOT NULL,
        YearsOfExperience INT NOT NULL,
        SeniorityLevel VARCHAR(255) NOT NULL,
        TechnologyStack VARCHAR(255) NOT NULL,
        CodeChallengeScore SMALLINT NOT NULL,
        TechnicalInterviewScore SMALLINT NOT NULL,
        IsHired BOOLEAN NOT NULL
    );
    '''
    cxn = None
    try:
        cnx = create_connection()
        cur = cnx.cursor()
        cur.execute(create_table_query)
        cur.close()
        cnx.commit()
        print('Tabla creada exitosamente')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cnx is not None:
            cnx.close()

def insert_data(df):
    insert_query = """
    INSERT INTO candidates (FirstName, LastName, Email, ApplicationDate, Country, YearsOfExperience, SeniorityLevel, TechnologyStack, CodeChallengeScore, TechnicalInterviewScore, IsHired)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cxn = None
    try:
        cnx = create_connection()
        cur = cnx.cursor()
        for index, row in df.iterrows():
            data = (row["FirstName"], row["LastName"], row["Email"], row["ApplicationDate"], row["Country"],
                    row["YOE"], row["Seniority"], row["Technology"], row["CodeChallengeScore"], row["TechnicalInterviewScore"], row["IsHired"])
            cur.execute(insert_query, data)
        cur.close()
        cnx.commit()
        print("Datos insertados exitosamente desde el DataFrame.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cnx is not None:
            cnx.close()
