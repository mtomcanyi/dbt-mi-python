from dbt.cli.main import dbtRunner, dbtRunnerResult

dbt = dbtRunner()
cli_args = ["--version"]

res: dbtRunnerResult = dbt.invoke(cli_args)

if res.result != None:
    for r in res.result:
        print(f"{r.node.name}: {r.status}")
