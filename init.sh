# mysql 创建随机密码
# 创建随机密码
export MYSQL_ROOT_PASSWORD=$(openssl rand -base64 12)
# 随机密码存入.env文件
echo "MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD" > .env






# 启动容器
docker-compose up --build -d