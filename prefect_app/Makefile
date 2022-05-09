start_server:
	prefect server start

start_agent:
	prefect agent local start --show-flow-logs

create_project:
	prefect create project $(PROJECT_NAME)

register_flows:
	prefect register --project $(PROJECT_NAME) -p .
