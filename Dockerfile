FROM hualeel/python3_flask:latest
MAINTAINER Henry li


# 环境变量
ENV SERVICE_PORT=33333 \
SERVICE_DIR=app \
PYPI=https://mirrors.aliyun.com/pypi/simple/ \
K8S_API_AUTH=eyJhbGciOiJSUzI1NiIsImtpZCI6ImpMNFdRVzhCOWRuN3BlWjZkbkFRYVUtZDZjN1dhWWd6cHhibTFQMnNuLVUifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi10b2tlbi1qOW5xYyIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJhZG1pbiIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6ImZhZmZlMzEzLWY3YzQtNDhmMC05YTZlLWI1OGUzYjEyNGIyZCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDprdWJlLXN5c3RlbTphZG1pbiJ9.c_j1Xhl5QORXya-DnHHZSLzMxyg48B0PIuyFIRDU4L-YsN-Etzey55s6m6DVw9YZKvRlY9NtD0On2pS4uYwFabuPjzydJ0U08MixaVMuchb2e29FhsD0buW3tQp8V3OSL4KVmXAO3yMcJr1utd3LQa2aM4YclmO3Os_DRNyKGTm3D5LjUJeXY4CdaikG8-AhC7JPd-idx_akIjeVDUn7ShhAuTOlJEs6vFiYMdkcW_O3yYNuon1ACPQ01zm70eEWsjNXiJZrotCJ2Us2ItqmV93hcVMjPKGROJwjzul7oFIZIWwaZu3xy83oLwOCjzSYypDJOPGHAyovw_clpbaWiA


ENV K8S_NAMESPACE=tke-poc-test
COPY . /$SERVICE_DIR
WORKDIR /$SERVICE_DIR

# 添加apk国内源，安装扩展包
#RUN pip install -i $PYPI --upgrade pip
#RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt

EXPOSE 33333
CMD [ "python", "./main.py" ]