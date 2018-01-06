# W-server


> * 项目基于 [Django](https://www.djangoproject.com/) + [AdminLTE](https://www.almsaeedstudio.com/) 构建，建议Ubuntu 14.04 上测试调试；建议使用 Chrome 浏览器。
> * 为了后续扩展方便，请使用 [Tengine](http://tengine.taobao.org/) 替代 Nginx 服务

## 项目地址
https://github.com/vspark/wserver

## 运行
* 克隆代码
```
mkdir -p /app  
git clone https://github.com/vspark/wserver.git /app/wserver
cd /app/wservere
```
* 卸载 nginx
```
apt-get -y purge nginx-* nginx*
apt-get -y autoremove
```
* 安装 tengine
```
git submodule update --init --recursive
cd resource/nginx/tengine
apt-get install -y build-essential libssl-dev libpcre3 libpcre3-dev zlib1g-dev
./configure --user=www-data --group=www-data --prefix=/etc/nginx --sbin-path=/usr/sbin --error-log-path=/var/log/nginx/error.log --conf-path=/etc/nginx/nginx.conf --pid-path=/run/nginx.pid
make
make install
mkdir -p /etc/nginx/conf.d
echo "daemon off;" >> /etc/nginx/nginx.conf  
```
* 安装依赖
```
apt-get install -y python-dev python-pip iptables libcurl4-openssl-dev
pip install -r requirements.txt  
```
* 初始化数据库
```
python manage.py makemigrations  
python manage.py migrate  
```
* static 目录下文件配置
````
windows本地：
    bootstrap 文件内容 ../resource/AdminLTE/bootstrap
    dist 文件内容 ../resource/AdminLTE/dist
    plugins 文件内容 ../resource/AdminLTE/plugins
    
linux & MAC:
    ln -s ../resource/AdminLTE/bootstrap bootstrap
    ln -s ../resource/AdminLTE/dist dist
    ln -s ../resource/AdminLTE/plugins plugins
````
* 启动服务
```
service supervisor restart  
```
* 登录系统
```
http://[IP]:8000/  
```
> 首次登陆会要求创建管理员用户，如需修改，可在系统配置中重置管理员用户



