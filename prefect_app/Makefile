start_server:
	prefect server start

start_agent:
	prefect agent local start --show-flow-logs

create_project:
	prefect create project $(PROJECT_NAME)

register_flows:
	prefect register --project $(PROJECT_NAME) -p .

run_flow:
	prefect run --project $(PROJECT_NAME) -n $(FLOW_NAME)

format:
	black .
