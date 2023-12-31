# Data Engineer Workshop

Welcome to the "Data Engineer Workshop" repository. This project presents a solution to an interview challenge for the Python Data Engineer role. The challenge aims to evaluate your data management skills and your ability to create meaningful visualizations.

## Challenge

The core challenge revolves around creating an application that migrates data from a CSV file to a relational database. Subsequently, the objective is to generate visualizations using the data stored in the database. The visualizations requested include pie charts, bar charts, and line charts.

## About the CSV

The included CSV file contains simulated data from candidates who participated in selection processes. It's important to note that this data was generated randomly and is meant to simulate real-world scenarios.

## Solution Overview

### Tools Used

- **Database Management System:** PostgreSQL was chosen for its familiarity and capabilities.

- **Visualizations:** Power BI was employed to create impactful and connected charts directly from the PostgreSQL database.

### Repository Contents

The repository consists of the following components:

- **Notebooks Folder:**
  - `candidates_eda.ipynb:` Jupyter notebook for exploratory data analysis.
  - `candidates_visualizations.ipynb:` This notebook contains SQL queries designed to generate graphs. While the original plan was to use libraries like matplotlib or seaborn, this notebook ensured that the data visualized in Power BI were consistent with the results obtained here. The prior exploration of visualizations helped validate the accuracy and consistency of results in the final Power BI platform.

- `requirements.txt:` Lists the library versions utilized in the project.

- `main.py:` The main script that invokes functions from `db_operations.py` and `data_transformation.py`.

- `db_operations.py:` This file simplifies interaction with PostgreSQL by offering essential functions. It includes `create_connection()` for establishing a database connection using configuration from `db_config.json`, `create_table()` for generating a "Candidates" table if absent, and `insert_data(df)` for inserting DataFrame content into the table via parameterized queries. This module streamlines PostgreSQL tasks from connection to data insertion.

- `data_transformation.py:` This file eases data transformation through crucial functions. It features `calculate_is_hired(row)` to determine if a candidate is hired based on code challenge and technical interview scores. Additionally, `transform_data(filename)` loads and adjusts data from a CSV file, renames columns, and adds the "IsHired" column using the aforementioned function. These operations are vital for preparing data in a suitable format for subsequent analysis.

## Getting Started

To start using the project, follow these steps:

1. **Clone the Repository:**
   - Clone the project repository in your development environment.

2. **Install the Required Libraries:**
   - Install the necessary libraries listed in the `requirements.txt` file. You can do this using a package manager like `pip` in Python. Run the following command:
     ```
     pip install -r requirements.txt
     ```

3. **Configure the PostgreSQL Database Connection:**
   - In the `db_config.json` file, configure the connection to the PostgreSQL database. Ensure that you provide the necessary connection details such as host, port, database name, username, and password.

4. **Run `main.py`:**
   - Execute the `main.py` script to perform data migration and transformation processes. This is the main script that carries out the data processing tasks specified in your project.

5. **Utilize the Generated Data and Visualizations:**
   - After running `main.py`, the processed data and generated visualizations will be available for use. You can use them as needed in your project, whether for analysis, reports, or other applications.

---

Follow these steps in order to get started and work effectively on your project.


