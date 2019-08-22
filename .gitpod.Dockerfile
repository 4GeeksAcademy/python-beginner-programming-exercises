

FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pyunit pytest-testdox && npm i breathecode-cli -g
