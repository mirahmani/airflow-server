setup:
	docker-compose up -d --force-recreate --remove-orphans
	docker exec airflow-server_airflow-webserver_1 ls -l /logs
	
down:
	docker-compose down

testing:
	docker exec airflow-server_airflow-webserver_1 pytest -v