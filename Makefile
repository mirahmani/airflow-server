setup:
	docker-compose up -d --force-recreate --remove-orphans
	docker exec airflow-server_airflow-webserver_1 pwd
	docker exec airflow-server_airflow-webserver_1 ls -l
	docker exec airflow-server_airflow-webserver_1 whoami
	
down:
	docker-compose down

testing:
	docker exec --user root airflow-server_airflow-webserver_1 /bin/bash -c 'cd tests && pwd &&python -m unittest discover tests'