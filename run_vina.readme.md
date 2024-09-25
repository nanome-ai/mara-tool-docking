# build docker image

WORKDIR /opt/
RUN git clone https://github.com/nanome-ai/mara-tool-docking.git
WORKDIR /opt/mara-tool-docking/
