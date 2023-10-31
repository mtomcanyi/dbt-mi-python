import os
from dbt.cli.main import dbtRunner, dbtRunnerResult

dbt = dbtRunner()


# Command to run
cli_args = [
       "run",                       # Run model 
       "--profiles-dir", ".."       # profiles.yml is located in main directory
]

# Switch to target project directory
work_dir = f"{os.getcwd()}/mi_postgres"
os.chdir(work_dir)


res: dbtRunnerResult = dbt.invoke(cli_args)

if res.result != None:
    for r in res.result:
        print(f"{r.node.name}: {r.status}")
