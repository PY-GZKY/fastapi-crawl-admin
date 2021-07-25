# Fastapi Crawl
![Fastapi Crawl](https://img.shields.io/badge/Python-3.8-green)
![Fastapi Crawl](https://img.shields.io/badge/Celery-5.0.5-blue)
![Fastapi Crawl](https://img.shields.io/badge/Fastapi-0.4.9-red)
![Fastapi Crawl](https://img.shields.io/badge/uvicorn-0.2.2-yellow)
![Fastapi Crawl](https://img.shields.io/badge/pydantic-0.2.2-brightgreen)
![Fastapi Crawl](https://img.shields.io/badge/fabric-0.1.13-yellow)
![Fastapi Crawl](https://img.shields.io/badge/Mysql-5.7-yellow)
![Fastapi Crawl](https://img.shields.io/badge/paramiko-0.0-yellow)


-   [x] 登录/注销
-   [x] 远程批量部署和调用
-   [x] `WebSocket` 任务日志
-   [x] 新增节点、测试节点
-   [ ] 展示节点已安装依赖服务/详细指标
-   [ ] `Redis` 缓存
-   [ ] 权限管理
-   [ ] 站内消息推送
-   [ ] `MQ`/`AQS`/`Celery`
-   [ ] `Docker`集成
-   [x] ~~fabric 版本差异过大故放弃~~  `paramiko`
-   [ ] ~~ssh 密码登录~~  `ssh key` 免密登录
-   [ ] `Scrapy` 集成


## 依赖

```
pip install pydantic[email]
pip install uvicorn
pip install fastapi
```


[comment]: <> (<details>)

[comment]: <> (<summary>项目文件结构</summary>)

[comment]: <> (```)

[comment]: <> (/alembic                         // alembic 自动生成的迁移配置文件夹,迁移不正确时 产看其中的env.py文件)

[comment]: <> (alembic.ini                      // alembic 自动生成的迁移配置文件)

[comment]: <> (app)

[comment]: <> (|____core                        )

[comment]: <> (| |______init__.py)

[comment]: <> (| |____config                    // 配置文件)

[comment]: <> (| | |______init__.py             // 根据虚拟环境导入不同配置)

[comment]: <> (| | |____development_config.py   // 开发配置)

[comment]: <> (| | |____production_config.py    // 生成配置)

[comment]: <> (| |____security.py               // token password验证          )

[comment]: <> (|____tests)

[comment]: <> (| |______init__.py)

[comment]: <> (|______init__.py)

[comment]: <> (|____api                         // API文件夹)

[comment]: <> (| |____api_v1                    // 版本区分)

[comment]: <> (| | |____auth                    // auth模块)

[comment]: <> (| | | |______init__.py)

[comment]: <> (| | | |____schemas               // 验证model文件夹)

[comment]: <> (| | | | |____user.py             // user验证)

[comment]: <> (| | | | |______init__.py)

[comment]: <> (| | | |____curd                  // curd 文件夹)

[comment]: <> (| | | | |____user.py             // user curd操作)

[comment]: <> (| | | | |______init__.py)

[comment]: <> (| | | |____views.py              // 各模块视图函数)

[comment]: <> (| | |______init__.py)

[comment]: <> (| | |____api.py                  // 路由函数)

[comment]: <> (| |______init__.py)

[comment]: <> (| |____utils                     // 工具类文件夹)

[comment]: <> (| | |____custom_exc.py           // 自定义异常)

[comment]: <> (| | |____response_code.py        // 统一自定义响应状态)

[comment]: <> (| |____models                    // 项目models 文件&#40;我没像django那样放到各模块下面,单独抽出来了&#41;)

[comment]: <> (| | |______init__.py)

[comment]: <> (| | |____auth.py                 // 用户权限相关的)

[comment]: <> (| | |____goods.py                // 商品相关)

[comment]: <> (| | |____shop.py                 // 店铺相关)

[comment]: <> (| |____extensions                // 扩展文件夹)

[comment]: <> (| | |______init__.py)

[comment]: <> (| | |____logger.py               // 扩展日志 loguru 简单配置)

[comment]: <> (| |____common                    // 通用文件夹)

[comment]: <> (| | |______init__.py)

[comment]: <> (| | |____deps.py                 // 通用依赖文件,如数据库操作对象,权限验证对象)

[comment]: <> (| | |____curd_base.py            // curd_base对象)

[comment]: <> (| | |____model_base.py           // model继承base对象&#40;报错暂时不用&#41;)

[comment]: <> (| |____logs)

[comment]: <> (| |____db                        // 数据库)

[comment]: <> (| | |______init__.py)

[comment]: <> (| | |____base_class.py           )

[comment]: <> (| | |____session.py              // )

[comment]: <> (| | |____base.py                 // 导出全部models 给alembic迁移用)

[comment]: <> (| | |____init_db.py              // 初始化数据)

[comment]: <> (|____utils.py)

[comment]: <> (|____main.py)

[comment]: <> (|____initial_data.py)

[comment]: <> (```)

[comment]: <> (</details>)


## alembic 生成表

### 自动生成迁移文件

```shell
alembic revision --autogenerate -m "init commit"
```

### 生成表
> alembic upgrade head



### 生成初始化账号密码

```shell
cd app
python initial_data.py
```

```shell
username: admin@163.com
password: 123456
```



## PR

> 我当然希望你能够有更好的想法或贡献。

