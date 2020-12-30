# -*- coding:utf-8 -*-
"""
Author:
名称：kubeovn demo
功能描述：KUBEOVN DEMO
"""

from flask import Flask, current_app, redirect, url_for, render_template
from flask_cors import *
import requests
import json
import os

app = Flask(__name__, template_folder="templates")


# 获取pod ip list
@app.route('/list-pods', methods=["GET"])
@cross_origin()
def get_pod_ip():
    k8s_api_server = str(os.getenv("K8S_API_SERVER"))
    # k8s_api_auth = str(os.getenv("K8S_API_AUTH"))
    k8s_api_auth = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImpMNFdRVzhCOWRuN3BlWjZkbkFRYVUtZDZjN1dhWWd6cHhibTFQMnNuLVUifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi10b2tlbi1qOW5xYyIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJhZG1pbiIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6ImZhZmZlMzEzLWY3YzQtNDhmMC05YTZlLWI1OGUzYjEyNGIyZCIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDprdWJlLXN5c3RlbTphZG1pbiJ9.c_j1Xhl5QORXya-DnHHZSLzMxyg48B0PIuyFIRDU4L-YsN-Etzey55s6m6DVw9YZKvRlY9NtD0On2pS4uYwFabuPjzydJ0U08MixaVMuchb2e29FhsD0buW3tQp8V3OSL4KVmXAO3yMcJr1utd3LQa2aM4YclmO3Os_DRNyKGTm3D5LjUJeXY4CdaikG8-AhC7JPd-idx_akIjeVDUn7ShhAuTOlJEs6vFiYMdkcW_O3yYNuon1ACPQ01zm70eEWsjNXiJZrotCJ2Us2ItqmV93hcVMjPKGROJwjzul7oFIZIWwaZu3xy83oLwOCjzSYypDJOPGHAyovw_clpbaWiA"
    k8s_namespace = str(os.getenv("K8S_NAMESPACE"))

    # url = "https://" + k8s_api_server + ":6443/api/v1/namespaces/" + k8s_namespace + "/endpoints/" + svc_name
    url = "https://" + k8s_api_server + ":6443/apis/apps/v1/namespaces/" + k8s_namespace + "/deployments"

    payload = {}

    headers = {
        "Authorization": "Bearer " + k8s_api_auth
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    print(response.text)
    # ip_list = []
    # for item in json.loads(response.text).get("subsets")[0].get("addresses"):
    #     ip_list.append(item["ip"])
    #
    # ip_str = ""
    # for ip in ip_list:
    #     ip_str = ip_str + ip + ";"
    # ip_str = "Pod IP: " + ip_str
    #
    # return render_template("index.html", pod_ip_list_str=ip_str)
    return response.text


if __name__ == '__main__':
    print(app.url_map)
    service_port = os.getenv("SERVICE_PORT")

    # 启动flask程序
    app.run(host="0.0.0.0", port=service_port)
