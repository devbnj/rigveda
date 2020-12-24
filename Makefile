SCODE_INSTALL=/home/dev/python/rigveda

cleanup:
	docker-compose -f $(SCODE_INSTALL)/docker-compose.yaml down --remove-orphans

build:
	docker-compose -f $(SCODE_INSTALL)/docker-compose.yaml up -d --build

run:
	docker-compose -f $(SCODE_INSTALL)/docker-compose.yaml up -d --no-build

prune:
	docker rmi $(docker images -a -q)