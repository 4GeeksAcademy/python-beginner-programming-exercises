FROM gitpod/workspace-full:latest

USER gitpod

RUN pyenv update && pyenv install 3.10.7 && pyenv global 3.10.7

RUN pip3 install pytest==6.2.5 pytest-testdox mock
RUN npm i @learnpack/learnpack@2.1.20 -g && learnpack plugins:install @learnpack/python@1.0.0
