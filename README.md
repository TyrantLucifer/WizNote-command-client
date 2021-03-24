# WizNote-command-client
在命令行下使用的一款WizNote客户端

## 前言
我是一名IT从业者，在职业成长的道路上需要不断地进行学习，可是人的脑容量始终有限，随着年龄的增长，人的记忆力也会随之下降，所以从古时候才会有这么一句话，`好记性不如烂笔头`，时刻记录自己的知识，丰富属于自己的知识库显得十分重要，这就引出来了另外一个概念：`笔记`

现在市面上有很多云笔记产品可以选择，比较出名的有`印象笔记`、`有道云笔记`、`为知笔记`等，这些都是很优秀的笔记产品，今天开源的项目就是关于我使用的笔记产品`为知笔记`进行开发的，我选择`为知笔记`的理由有以下几点：

- 支持Markdown
- 支持全平台
- 价格实惠

Linux平台是我的主力系统之一，所以支持Linux才是我选择一款笔记产品的重要因素，从大学期间就开始使用`为知笔记`，到如今我已经用了三年之久，任何产品只要用户黏性一旦形成，就很难再去适应其他产品，但是`为知笔记`的编辑器一直不太好用，甚至可以说是有点反人类，书写体验很差，久而久之，诸多为知用户因为编辑器流失了很多，虽然近期为知推出了自己家的编辑器`WizNote`，但是用起来和王牌编辑器`Typora`还是差那么点火候，这时候就有人会想了，
如果Typora写笔记，为知存笔记，这么一个工作流不就可以了吗？所以，`WizNote-command-client`应运而生。

## 技术支持

- 为知笔记开放出了丰富的api，可以实现很多功能
- Python脚本语言

## 架构设计

![image-20210223205307920](https://cdn.jsdelivr.net/gh/TyrantLucifer/MyImageRepository/img/image-20210223205307920.png)

目前`0.0.5`版本实现了一下功能：
- 动态获取token，如果token有效期未过，则从本地获取
- 列出当前目录列表
- 列出某个目录的所有笔记
- 上传笔记
- 更新笔记

如果有新的想法可以提issue或者提交pr，欢迎各位为知儿们头脑风暴。

## 安装方式

- 源码安装

```shell
git clone https://github.com/TyrantLucifer/WizNote-command-client.git
cd WizNote-command-client
python(python3) setup.py install
```

- pip安装

```shell
pip(pip3) install wiznote-cli 
```

## 使用方法

```
usage: wiznote-cli [-h] [--set-username username] [--set-password password]
                   [--category category] [--upload file] [--update file]
                   [--doc-guid doc_guid] [--list-category]
                   [--list-note category] [-v]

The wiz note command client based python.

optional arguments:
  -h, --help            show this help message and exit
  --set-username username
                        set wiz username
  --set-password password
                        set wiz password
  --category category   assign note category
  --upload file         assign note file
  --update file         update note
  --doc-guid doc_guid   the doc guid of note
  --list-category       list all valid category
  --list-note category  list all notes in category
  -v, --version         display version

Powered by tyrantlucifer. If you have any questions, you can send e-mail to
tyrantlucifer@gmail.com
```

- 上传笔记

```shell
wiznote-cli --upload 我的笔记.md --category "/Notes/"
```

- 查看目前有哪些日记目录

```shell
wiznote-cli --list-category
```

- 设置为知笔记用户名和密码

```shell
wiznote-cli --set-username 用户名
wiznote-cli --set-password 密码
```

## Todo

- [ ] 创建目录
- [ ] 删除笔记
- [ ] 笔记搜索功能

## 支持开源:heart:, 请作者喝杯星巴克

> 有意愿献爱心的小伙伴，务必将github账号写入捐款备注哦，谢谢大家

| wechat                                                       | alipay                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <a href='#支持开源'><img src="https://cdn.jsdelivr.net/gh/TyrantLucifer/MyImageRepository/img/wechat-pay.png" height="150" width="150" /></a> | <a href='#支持开源'><img src="https://cdn.jsdelivr.net/gh/TyrantLucifer/MyImageRepository/img/alipay.jpg" height="150" width="150" /></a> |

## Tips

如果有好的建议，欢迎发邮件给我，或者关注下方我的个人微信公众号在后台留言，或者加qq群`764374820`反馈

- Email:Tyrantlucifer@gmail.com 
- Blog:https://tyrantlucifer.com
- Personal Wechat

| 微信公众号                                                   |
| ------------------------------------------------------------ |
| <a href='#Tips'><img src="https://cdn.jsdelivr.net/gh/TyrantLucifer/MyImageRepository/img/wechat.jpg" height="300" width="300" /></a> |

