# Jobmaster

## 描述

## 部署

### 参考教程

- [我如何使用 Django + Vue.js 快速构建项目](https://zhuanlan.zhihu.com/p/25080236)
- [整合 Django + Vue.js 框架快速搭建 web 项目](https://cloud.tencent.com/developer/article/1005607)
- [跨过 Nginx 上基于 uWSGI 部署 Django 项目的坑](https://www.cnblogs.com/qingspace/p/6838747.html)
- [使用 uWSGI 和 nginx 来设置 Django 和你的 web 服务器](https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/tutorials/Django_and_nginx.html)
- [在 CentOS 云服务器上使用 Nginx + uWSGI 部署 Flask 程序](http://brucezz.itscoder.com/nginx-uwsgi-flask-deploy-on-centos)

### 需求

- Ubuntu 16.04
- nginx
- uwsgi
- 8.x NodeJS、npm（用于前端 vue 框架）
- mysql-server
- redis-server

### 步骤

修改 Ubuntu 软件源为国内源：<https://mirrors.ustc.edu.cn/help/ubuntu.html>

NodeJS、NPM，Ubuntu 源太旧，使用官网脚本：

```bash
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
```

修改 nodesource 为国内源，将 `/etc/apt/sources.list.d/nodesource.list` 改为：

```/etc/apt/sources.list.d/nodesource.list
deb https://mirrors.ustc.edu.cn/nodesource/deb/node_8.x xenial main
deb-src https://mirrors.ustc.edu.cn/nodesource/deb/node_8.x xenial main
```

安装 nginx gcc python3-dev mysql-server nodejs redis-server，gcc 和 python3-dev 用于编译 uwsgi：

```bash
sudo apt install -y nginx gcc python3-dev mysql-server nodejs redis-server
```

Ubuntu 源的 pip 不好，手动安装 pip：

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && sudo python3 get-pip.py && pip install --upgrade pip
```

修改 pip 源为国内源：<https://mirrors.ustc.edu.cn/help/pypi.html>

修改 npm 源为国内源：

```bash
sudo npm install -g cnpm --registry=https://registry.npm.taobao.org && sudo cnpm install npm@latest -g
```

安装 uwsgi：

```bash
sudo pip install uwsgi
```

克隆项目：

```bash
git clone https://github.com/PostRecommenderProject/Jobmaster.git && cd Jobmaster
```

创建虚拟环境：

```bash
python3 -m venv jmvenv
```

进入虚拟环境：

```bash
source jmvenv/bin/activate
```

在虚拟环境下安装 django、scrapy、PyMySQL：

```bash
pip install django scrapy PyMySQL scrapy-djangoitem django-rq rq-scheduler sklearn pandas jieba gensim
```

在 `Jobmaster/frontend` 下：

```bash
cnpm install
cnpm run build
```

编辑 `/etc/mysql/my.cnf`：

``` my.cnf
[client]
default-character-set=utf8mb4

[mysqld]
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
init_connect='SET NAMES utf8mb4'
skip-character-set-client-handshake = true

[mysql]
default-character-set = utf8mb4
```

创建 `jobmaster` 数据库后，在 `Jobmaster` 下：

```bash
python manage.py migrate
python manage.py collectstatic
```

编辑合适的 `uwsgi.ini` 和 `nginx-jobmaster.conf`。

link nginx 配置文件并确认可运行：

```bash
sudo ln -s /home/vagrant/jobmaster/nginx-jobmaster.conf /etc/nginx/sites-enabled/jobmaster.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
```

载入配置：

```bash
sudo service nginx restart
```

创建 uwsgi socket 文件夹（根据 uwsgi.ini），可以在 `/etc/rc.local` 里写入，每次启动自动创建：

```bash
sudo mkdir /var/run/uwsgi
```

启动 uwsgi：

```bash
sudo uwsgi -i uwsgi.ini
```

启动 redis：

```bash
redis-server
```

启动 rqworker：

```bash
python manage.py rqworker default
```