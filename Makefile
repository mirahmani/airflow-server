setup:
	docker-compose up -d --force-recreate --remove-orphans
	docker exec airflow-server_airflow-webserver_1 pwd
	docker exec airflow-server_airflow-webserver_1 ls -l
	docker exec airflow-server_airflow-webserver_1 whoami
	docker exec --user root airflow-server_airflow-webserver_1 airflow db init
	
down:
	docker-compose down

testing:
	docker exec --user root airflow-server_airflow-webserver_1 python3 -m unittest discover tests