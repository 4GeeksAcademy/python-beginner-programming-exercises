

FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pytest mock pytest-testdox && npm i breathecode-cli@1.1.80 -g
