## 1. Python语言发展史

### 起源

​	据说（~~bushi~~）Python语言是大佬`吉多·范罗苏姆`(Guido van Rossum)在1989年圣诞期间为了打发假期空闲时间而开发出来的。起初他只是打算给他之前开发出的脚本语言ABC写一个解释器，但由于他非常具有前瞻性的选择将其开放，从而吸引了世界各地的开发者，建立了Python社区，共同投身于Python语言的建设之中。

​	至于这个语言为什么被命名为Python，听闻是因为吉多本人是*`巨蟒剧团之飞翔的马戏团(Monty Python's Flying Circus)`*这部喜剧的铁粉，所以将其取名为Python。

> Over six years ago, in December 1989, I was looking for a "hobby" programming
>
> project that would keep me occupied during the week around Christmas. My office
>
> (a government-run research lab in Amsterdam) would be closed, but I had a home
>
> computer, and not much else on my hands. I decided to write an interpreter for the
>
> new scripting language I had been thinking about lately: a descendant of ABC that
>
> would appeal to Unix/C hackers. I chose Python as a working title for the project,
>
> being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus).
>
> (原文地址：https://www.python.org/doc/essays/foreword/)

### 当前

全球开发者就业信息网站*DevJobsScanner*分析了超过1400万个就业岗位信息后，从市场需求角度得出了2023年最受欢迎的编程语言排行，Python语言排在第二名。第一是JavaScript和Typescript，第三名是Java。Python的发展势头可见一斑。

> Without making much noise, Python has made its journey to be the second most demanded programming language in 2023. Its versatility, from scripting, running servers or for data analysis, has been key to achieving this milestone. Also, Python has one of the greatest and bigger communities out there.
>
> During these seventeen months we have found 603K job offers that accounts for a total of ~20% of jobs that explicitly required Python as a programming language.
>
> (原文地址：https://www.devjobsscanner.com/blog/top-8-most-demanded-programming-languages/)

## 2. Python语言的特性

1. 完全面向对象的语言

   Python的函数、模块、数字、字符串都是对象。并且完全支持继承、重载、派生、多继承，有益于增强源代码的复用性。Python支持重载运算符，因此Python也支持泛型设计。

2. 解释型语言

   Python 是一种解释型语言，不需要编译和链接，可以节省大量开发时间。

3. 代码简洁易读

   - 高级数据类型允许在单一语句中表述复杂操作
   - 使用缩进，而不是括号实现代码块分组
   - 无需预声明变量或参数

4. 程序模块化

   Python 支持把程序分割为模块，以便在其他 Python 程序中复用。它还内置了大量标准模块，作为开发程序的基础

5. 可拓展性强

   会开发 C 语言程序，就能快速上手为解释器增加新的内置函数或模块，不论是让核心程序以最高速度运行，还是把 Python 程序链接到只提供预编译程序的库（比如，硬件图形库）。只要下点功夫，就能把 Python 解释器和用 C 开发的应用链接在一起，用它来扩展和控制该应用


## 3. VS Code集成Python开发环境

1. 安装解释器
   - 从官网下载[Download Python | Python.org](https://www.python.org/downloads/)当前平台*（windows）*的解释器安装包进行安装
   - 安装好后在命令行或shell里面执行 python.exe*(windows)*查看是否安装成功
2. 安装VS Code插件
   - 打开VS Code插件市场，安装[Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)插件
   - 安装[Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)插件，支持在交互式窗口执行Python代码
   - 新建一个`.py`文件，写入经典代码`print("hello world")`,右键选择在交互窗口运行该文件

