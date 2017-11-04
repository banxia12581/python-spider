前言
开发环境：python2.7
1. scrapy框架

1.1 scrapy 框架

文件名:scrapy

1.1.1 搜狗微信公众号

    1. 链接地址
    http://weixin.sogou.com/
    2.文件名(开始链接做文件名):
    weixin.sogou.com
    3.功能
    1)将数据保存为json和csv格式,其中csv即为Excle格式的文件
    2)是否分页:是

1.1.2 西刺代理网站

    1. 链接地址
    http://www.xicidaili.com/nt/
    2.文件名(开始链接做文件名):
    www.xicidaili.com
    3.功能
    1)将数据保存为json和csv格式,其中csv即为Excle格式的文件
    2)是否分页:是
    3)是否加入数据库:是,mongodb

1.1.3 腾讯招聘网站

1)不解析详情页

    1. 链接地址
    http://hr.tencent.com/position.php?start=
    2.文件名(开始链接做文件名):
    hr.tencent.com-position/1
    3.功能
    1)将数据保存为json和csv格式,其中csv即为Excle格式的文件
    2)是否分页:是
    3)是否解析详情页:否

2)解析详情页

    1. 链接地址
    http://hr.tencent.com/position.php?start=
    2.文件名(开始链接做文件名):
    hr.tencent.com-position/2
    3.功能
    1)将数据保存为json和csv格式,其中csv即为Excle格式的文件
    2)是否分页:是
    3)是否解析详情页:是
    4)是否加入数据库:是,同步数据库(异步数据库有点问题待解决)
    5)使用crawlScrapy



1.1.4 博客园网站

    1. 链接地址
    www.cnblogs.com
    2.文件名(开始链接做文件名):
    www.cnblogs.com
    3.功能
    1)将数据保存为json和csv格式,其中csv即为Excle格式的文件
    2)是否分页:是
    3)是否解析详情页:是
    4)是否加入数据库:是,同步数据库
    
    注意:博客园网站的实际分页并不是地址栏里展示的那个规则,应该是做过地址重定向,实际的分页是鼠标悬浮在分页上面的时候展示出来的地址:https://www.cnblogs.com/sitehome/p/%d

1.1.5 网易名博网站

    1. 链接地址
    http://blog.163.com/blogger.html
    2.文件名(开始链接做文件名):
    blog.163.com-blogger
    3.功能
    1)将数据保存为json
    2)是否分页:是
    3)是否解析详情页:是
    
    注意:网易名博需要提交表单:scrapy.FormRequest,其中c0-param0变量是详情页的前9个数字

1.1.6 豆瓣网站

    1. 链接地址
    https://accounts.douban.com/login
    2.文件名(开始链接做文件名):
    www.douban.com-accounts
    3.功能
    1)将数据保存为json:否
    2)是否分页:否
    3)是否解析详情页:否
    4)实现登录

1.1.7 人人网站

    1. 链接地址
    http://www.renren.com/PLogin.do
    2.文件名(开始链接做文件名):
    www.renren.com-PLogin
    3.功能
    1)将数据保存为json:否
    2)是否分页:否
    3)是否解析详情页:否
    4)实现登录:两种方式,提取cookie和直接发送账号密码

1.1.8 珍爱网

    1. 链接地址
    http://search.zhenai.com/v2/search/pinterest.do
    2.文件名(开始链接做文件名):
    www.zhenai.com
    3.功能
    1)将数据保存为json:否
    2)是否分页:是
    3)是否解析详情页:否
    4)是否加入数据库:是,加入redis,最终存入mysql数据库中

1.1.9 去哪网-连锁酒店

    1. 链接地址
    http://pinpai.hotel.qunar.com/
    2.文件名(开始链接做文件名):
    hotel.qunar.com
    3.功能
    1)将数据保存为json:否
    2)是否分页:是
    3)是否解析详情页:否
    4)是否加入数据库:是

1.1.10 中植集团-经济金融动态

    1. 链接地址
    http://www.zhongzhi.com.cn/pages/zz/hydt.html
    2.文件名(开始链接做文件名):
    www.zhongzhi.com.cn
    3.功能
    1)将数据保存为json:是
    2)是否分页:是



1.2  crawlscrapy

文件名：crawlspider

1.2.1 hao123网站

    1. 链接地址
    http://www.hao123.com
    2.文件名(开始链接做文件名):
    www.renren.com-PLogin
    3.功能
    1)将数据保存为json:否
    2)是否分页:否
    3)是否解析详情页:否
    4)是否加入数据库:是,加入redis

1.2.2 拉勾网

    1. 链接地址
    http://www.lagou.com
    2.文件名(开始链接做文件名):
    www.lagou.com
    3.功能
    1)将数据保存为json:否
    2)是否分页:是
    3)是否解析详情页:是
    4)是否加入数据库:是,加入redis,最终存入mysql数据库中



2. 不使用框架的爬虫

文件名：spider

2.1 phantomjs

文件名：phantomjs

2.1.1拉勾网

    1.网站地址
    https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=
    2.文件名(开始链接做文件名):
    www.lagou.com-jobs
    3.功能
    1)将数据保存为json:是
    2)是否分页:是
    3)是否解析详情页:否
    4)是否加入数据库:否

2.2.2 斗鱼

    1.网站地址
    https://www.douyu.com/directory/all?
    2.文件名(开始链接做文件名):
    www.douyu.com-directory
    3.功能
    1)将数据保存为json:否，保存的为图片
    2)是否分页:是
    3)是否解析详情页:否
    4)是否加入数据库:否

2.2 多线程

文件名：thread

2.1.1 拉勾网

    1.网站地址
    https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=
    2.文件名(开始链接做文件名):
    www.lagou.com-jobs
    3.功能
    1)将数据保存为json:是
    2)是否分页:是
    3)是否解析详情页:否
    4)是否加入数据库:否

2.2.2 斗鱼

    1.网站地址
    https://www.douyu.com/directory/all?
    2.文件名(开始链接做文件名):
    www.douyu.com-directory
    3.功能
    1)将数据保存为json:是
    2)是否分页:是
    3)是否解析详情页:否
    4)是否加入数据库:否

2.2.3 糗事百科

    1.网站地址
    https://www.qiushibaike.com/8hr/
    2.文件名(开始链接做文件名):
    www.qiushibaike.com-8hr
    3.功能
    1)将数据保存为json:是
    2)是否分页:是
    3)是否解析详情页:否
    4)是否加入数据库:否

2.3 bs4

文件名：bs4

2.3.1 51job

    1.网站地址
    http://search.51job.com/list/010000,000000,0000,00,9,99,python,2.html
    2.文件名(开始链接做文件名):
    search.51job.com
    3.功能
    1)将数据保存为json:是
    2)是否分页:是
    3)是否解析详情页:否
    4)是否加入数据库:否

2.3.2 腾讯招聘

    1.网站地址
    http://hr.tencent.com/position.php?
    2.文件名(开始链接做文件名):
    hr.tencent.com-position
    3.功能
    1)将数据保存为json:是
    2)是否分页:是
    3)是否解析详情页:否
    4)是否加入数据库:否

2.4 其他

文件名：other

2.4.1 百度贴吧

    1.网站地址
    https://tieba.baidu.com/f?
    2.文件名(开始链接做文件名):
    tieba.baidu.com
    3.功能
    1)将数据保存为json:否,保存为图片
    2)是否分页:是
    3)是否解析详情页:否
    4)是否加入数据库:否

2.4.2 西刺代理

    1.网站地址
    http://www.xicidaili.com/nt
    2.文件名(开始链接做文件名):
    www.xicidaili.com
    3.功能
    1)将数据保存为json:否,存为txt文件
    2)是否分页:是
    3)是否解析详情页:否
    4)是否加入数据库:否

2.4.3 有道翻译

    1.网站地址
    http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
    2.文件名(开始链接做文件名):
    fanyi.youdao.com-translate_o
    3.功能
    1)将数据保存为json:否
    2)是否分页:否
    3)是否解析详情页:否
    4)是否加入数据库:否



