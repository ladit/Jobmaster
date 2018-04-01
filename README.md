# Jobmaster

## 描述

## 部署

### 参考教程

- <https://zhuanlan.zhihu.com/p/25080236>
- <https://cloud.tencent.com/developer/article/1005607>
- <https://www.cnblogs.com/qingspace/p/6838747.html>
- <https://uwsgi-docs-zh.readthedocs.io/zh_CN/latest/tutorials/Django_and_nginx.html>
- <http://brucezz.itscoder.com/nginx-uwsgi-flask-deploy-on-centos>

### 需求

- Ubuntu 16.04
- nginx
- uwsgi
- nodejs、npm（用于前端 vue 框架）
- mysql-server

### 步骤

修改 Ubuntu 软件源为国内源：<https://mirrors.ustc.edu.cn/help/ubuntu.html>

安装 nginx nodejs npm gcc python3-dev mysql-server，gcc 和 python3-dev 用于编译 uwsgi：

```bash
sudo apt install nginx nodejs npm gcc python3-dev mysql-server
```

Ubuntu 源的 pip 不好，手动安装 pip：

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py
```

修改 pip 源为国内源：<https://mirrors.ustc.edu.cn/help/pypi.html>

修改 npm 源为国内源，在 `~/.bashrc` 加上：

```bash
alias cnpm="npm —registry=https://registry.npm.taobao.org —cache=$HOME/.npm/.cache/cnpm —disturl=https://npm.taobao.org/dist —userconfig=$HOME/.cnpmrc"
```

安装 uwsgi：

```bash
sudo pip install uwsgi
```

创建虚拟环境：

```bash
git clone https://github.com/PostRecommenderProject/Jobmaster.git
cd Jobmaster
python3 -m venv jmvenv
```

进入虚拟环境：

```bash
source jmvenv/bin/activate
```

在虚拟环境下安装 django、scrapy：

```bash
pip install django scrapy
```

uwsgi socket 文件夹配置（根据 uwsgi.ini）：

```bash
sudo mkdir /var/run/uwsgi
sudo chown www-data:www-data /var/run/uwsgi
sudo chmod 777 /var/run/uwsgi
```

启动 uwsgi：

```bash
sudo uwsgi -i uwsgi.ini
```

link nginx 配置文件并确认可运行：

```bash
sudo ln -s /home/vagrant/jobmaster/nginx-jobmaster.conf /etc/nginx/sites-enabled/jobmaster.conf
nginx -t
```

载入配置：

```bash
sudo rm -f /etc/nginx/sites-enabled/default
sudo service nginx restart
```
