FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pytest==4.6.0 pytest-testdox mock
RUN npm i @learnpack/learnpack -g && learnpack plugins:install learnpack-python@0.0.35
