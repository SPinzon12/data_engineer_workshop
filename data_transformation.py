import pandas as pd

def calculate_is_hired(row):
    return row["CodeChallengeScore"] >= 7 and row["TechnicalInterviewScore"] >= 7

def transform_data(filename):
    print("Leyendo datos desde el archivo CSV:", filename)
    candidates_df = pd.read_csv(filename, delimiter=';')
    candidates_df.columns = candidates_df.columns.str.replace(' ', '')
    candidates_df["IsHired"] = candidates_df.apply(calculate_is_hired, axis=1)
    print("Transformación de datos completada.")
    return candidates_df