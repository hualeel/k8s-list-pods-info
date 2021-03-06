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
@app.route('/', methods=["GET"])
@cross_origin()
def get_pod_ip():
    k8s_api_server = os.getenv("K8S_API_SERVER")
    k8s_api_auth = os.getenv("K8S_API_AUTH")
    k8s_namespace = os.getenv("K8S_NAMESPACE")

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
