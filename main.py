import db_operations
import data_transformation

if __name__ == "__main__":
    db_operations.create_connection()
    candidates_df = data_transformation.transform_data("./dataset/candidates.csv")
    print(candidates_df[["IsHired", "CodeChallengeScore", "TechnicalInterviewScore"]].sample(10))
    db_operations.create_table()
    db_operations.insert_data(candidates_df)