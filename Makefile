.PHONY: build
build:
	docker build -t dgzlopes/powerfulseal-agent:v0.0.1 -t dgzlopes/powerfulseal-agent:latest .

.PHONY: run
run:
	docker run -it \
    --network host \
    --cap-add NET_ADMIN \
    --restart always \
	-p 8000:8000 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /proc/sysrq-trigger:/sysrq \
    dgzlopes/powerfulseal-agent:latest

.PHONY: clean
clean:
	docker stop $$(docker ps -a -q)
	docker rm $$(docker ps -a -q)  