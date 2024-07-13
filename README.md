# SecKnowledge-Crawler

## Introduction

SecKnowledge-Crawler是一个将网络安全社区公开的安全知识爬取工具，能够将知识本地化保存，便于搜索使用。目前爬取范围包括先知社区，后续持续更新以支持更多社区。

## Config

### 依赖库

```
selenium
toollib		#用来自动下载本地浏览器对应版本的ChromeDriver
markdownify
beautifulsoup4
```

### ChromeDriver

#### 推荐方法

初次运行需要使用如下代码下载匹配的ChromeDriver

```python
from toollib import autodriver
driver_path = autodriver.chromedriver()
```

#### 其他方法

ChromeDriver镜像站：http://npm.taobao.org/mirrors/chromedriver/

- Windows和Mac用户在[下载Chrome](https://www.google.cn/chrome/)并安装后，下载对应chrome版本的ChromeDriver并在配置文件`config.yml`中指定ChromeDriver的路径
- Linux用户在下载Chrome（链接如下）并安装后，同上编辑配置文件
  - [Debian/Ubuntu(64位.deb)](https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb)
  - [Fedora/openSUSE(64位.rpm)](https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm)

> Chrome浏览器可以访问`chrome://version/`查看版本

> 命令行可以使用`google-chrome-stable --version`查看版本

## Usage

```
python main.py
```

