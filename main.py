import os
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


# Initialize environment variables
os.environ["DBT_DEV_HOST"] = "changeme.meiro.io"
os.environ["DBT_DEV_PORT"] = "5432"
os.environ["DBT_DEV_USER"] = "changeme"
os.environ["DBT_DEV_PASS"] = "changeme"
os.environ["DBT_DEV_DBNAME"] = "changeme"
os.environ["DBT_DEV_SCHEMA"] = "changeme"


res: dbtRunnerResult = dbt.invoke(cli_args)

if res.result != None:
    for r in res.result:
        print(f"{r.node.name}: {r.status}")
