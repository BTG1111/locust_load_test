# 使用官方 Python image
FROM python:3.12-slim

# 安裝必要套件
RUN pip install --upgrade pip

# 建立工作目錄
WORKDIR /app

# 把你的檔案複製到容器中
COPY . /app

# 安裝 Python 套件
RUN pip install -r requirements.txt

# 讓容器一啟動就跑 locust
ENTRYPOINT ["locust"]