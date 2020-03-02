FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN  apt-get update && \
    apt-get install -y \
        iproute2 iptables iperf iputils-ping \
        curl stress \
        && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

RUN pip3 install tcconfig flask fastapi fastapi_utils psutil
#RUN curl -fsSL get.docker.com | sh

COPY powerfulseal_agent/main.py powerfulseal_agent/network.py powerfulseal_agent/resource.py ./
COPY powerfulseal_agent/state.py powerfulseal_agent/utils.py powerfulseal_agent/base.py ./


ENTRYPOINT ["uvicorn","main:app","--reload"]