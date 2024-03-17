setup:
	docker-compose up -d --force-recreate --remove-orphans
	sleep 60
	docker exec airflow-server_airflow-webserver_1 airflow users create --username admin --password admin --role Admin --firstname Ademir --lastname Junior --email airflow@example.com
	

down:
	docker-compose down

testing:
	docker exec airflow-server_airflow-webserver_1 pytest -v