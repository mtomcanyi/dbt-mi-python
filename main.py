import os
import json
from dbt.cli.main import dbtRunner, dbtRunnerResult


    


dbt = dbtRunner()


# Command to run
cli_args = [
       "run",                       # Run model 
       "--profiles-dir", ".."       # profiles.yml is located in main directory
]

# Switch to target project directory
repository_path = "/data/repository"
work_dir = f"{repository_path}/mi_postgres"
os.chdir(work_dir)

# Parse config
with open('/data/config.json') as f:
    json_data = json.load(f)
    DB_HOST = json_data['parameters']['DB_HOST']
    DB_PORT= json_data['parameters']['DB_PORT']
    DB_NAME = json_data['parameters']['DB_NAME']
    DB_USER = json_data['parameters']['DB_USER']
    DB_PASS = json_data['parameters']['DB_PASS']
    DB_SCHEMA = json_data['parameters']['DB_SCHEMA']



# Initialize environment variables
os.environ["DBT_DEV_HOST"] = DB_HOST
os.environ["DBT_DEV_PORT"] = DB_PORT
os.environ["DBT_DEV_USER"] = DB_USER
os.environ["DBT_DEV_PASS"] = DB_PASS
os.environ["DBT_DEV_DBNAME"] = DB_NAME
os.environ["DBT_DEV_SCHEMA"] = DB_SCHEMA


res: dbtRunnerResult = dbt.invoke(cli_args)

if res.result != None:
    for r in res.result:
        print(f"{r.node.name}: {r.status}")
