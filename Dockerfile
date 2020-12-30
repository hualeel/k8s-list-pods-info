FROM centos:7.7
MAINTAINER Henry li
# 环境变量
ENV SERVICE_PORT=33333 \
SERVICE_DIR=app \
PYPI=https://mirrors.aliyun.com/pypi/simple/
# 创建工作目录
RUN mkdir -p /$SERVICE_DIR
COPY . /$SERVICE_DIR
WORKDIR /$SERVICE_DIR
# 添加apk国内源，安装扩展包
RUN pip install -i $PYPI --upgrade pip && \
    pip install -i $PYPI -r requirements.txt && \
    chmod 700 ./run.sh
# 端口
EXPOSE $SERVICE_PORT
CMD sh ./run.sh