## 说明
CMDB管理系统,基于Ansible最新版开发

## 项目主要结构
```
./
├── ansible_client  # ansible_client客户端
│   └── monitor
│       ├── cpu.py  # 监控cpu
│       └── memory.py  # 监控内存
├── api  # api部分
│   ├── api_urls.py  # api相关的url
│   ├── serializers  # 序列化相关
│   │   ├── ansible.py  # ansible
│   │   ├── disk.py  # 磁盘
│   │   ├── hostinfo.py  # 主机详细信息
│   │   ├── host.py  # 主机信息
│   │   └── network.py  # 网络信息
│   ├── utils
│   │   ├── ansible  # ansible相关
│   │   │   ├── check_ip.py  # 检测ip可用性
│   │   │   ├── exec_ansible.py  # ansible的API,用来执行ansible命令
│   │   │   ├── extract_setup.py  # 检测硬件信息
│   │   │   ├── hosts_fm.py  # ansible的hosts文件写入
│   │   │   ├── login_host.py  # 远程登录主机
│   │   │   └── remotExect.sh  # 输入密码
│   │   ├── auth.py  # 认证
│   │   ├── response.py  # 统一code返回值
│   │   └── serialization_general.py  # 标准序列化返回值
│   └── views
│       ├── ansible.py  # ansible相关
│       ├── disk.py  # 磁盘相关
│       ├── hostinfo.py  # 主机详情
│       ├── host.py  # 主机
│       ├── monit  # 监控相关
│       │   ├── cpu.py
│       │   └── memory.py
│       └── network.py  # 网卡相关
├── AutoCmdb
│   ├── settings.py  # 项目配置文件
│   ├── urls.py  # 总入口
├── cron
│   └── test_orm.py  # 测试脚本
├── db.sqlite3  # 数据库
├── manage.py  # 启动文件
├── README.md
├── repository
│   └── models.py  # 数据库文件
└── web  # 前端展示部分
    ├── static  # 静态目录
    │   ├── css
    │   ├── img
    │   ├── js
    │   └── plugins
    │       ├── bootstrap-3.3.7  # bootstrap
    │       ├── font-awesome-4.7.0  # 图标库插件
    │       ├── Highcharts-6.1.2  # 图表插件
    │       └── sweetalert  # 弹框插件
    ├── templates  # 模板相关
    │   ├── ansible_add_host.html  # 添加ansible主机
    │   ├── ansible_add.html  # 添加ansible组
    │   ├── ansible_list.html  # ansible列表
    │   ├── base.html  # 母版
    │   ├── default.html  # 默认首页的右侧部分
    │   ├── host_info.html  # 主机详情
    │   ├── host_list.html  # 主机列表
    │   ├── index.html  # 首页主体部分,包含左侧边栏和头部
    │   └── monitor  # 监控图表相关
    │       ├── cpu.html
    │       └── memory.html
    ├── views
    │   ├── ansible.py  # ansible相关
    │   ├── host.py  # 主机相关
    │   └── index.py
    └── web_urls.py  # web页面相关路由
```

## 运行环境

| Project | version | Description |
|---------|--------|-------------|
| python  | 3.6.5 | 无 |
| django  | 1.11 | 必须此版本 |
| djangorestframework  | 3.8.2 | 无 |
| ansible  |2.7.0 | 不能低于此版本 |

## 功能说明
```
1. 服务器资产信息收集
2. server监控
3. cmdb API
```


## 效果
首页：

![Image text](IMG/01.png)

ansible管理：

![Image text](IMG/ansible主机管理.png)

ansible主机：

![Image text](IMG/ansible%E4%B8%BB%E6%9C%BA%E7%AE%A1%E7%90%86.png)

主机详情：

![Image text](IMG/主机详情.png)


## 运行方式
###ansible主控端
```
首先需要编译安装python3,请参考链接:

做到显示版本为止,添加软连接
ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3.6 /usr/bin/pip3

安装python相关模块
pip3 install django==1.11
pip3 install djangorestframework
pip3 install ansible

最后切换到项目目录,使用以下命令运行
python3 manage.py runserver 0.0.0.0:8000
```
###ansible被控端
```
编译安装python3,参考上面的操作
安装python相关模块
pip3 install psutil

将项目中的ansible_client拷贝到opt目录中,设置任务计划

# 监控cpu和内存
* * * * * python3 /opt/ansible_client/monitor/cpu.py
* * * * * python3 /opt/ansible_client/monitor/memory.py
```

## 网页操作
```
请务必安装以下操作进行：
访问页面： http://ip地址/web/
1. 进入首页,点击左侧ansible管理。必须先添加组
2. 添加组之后,再点击添加主机
3. 最后点击左侧ansible主机,就可以查看主机详情和监控图表了
```


## 备注
本项目只是一个demo,请勿直接用于生产环境!


Copyright (c) 2018-present, john966
