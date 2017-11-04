/*
SQLyog 企业版 - MySQL GUI v7.14 
MySQL - 5.5.5-10.1.13-MariaDB : Database - mydb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`mydb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `mydb`;

/*Table structure for table `cnblogs` */

DROP TABLE IF EXISTS `cnblogs`;

CREATE TABLE `cnblogs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `blogs_name` varchar(32) NOT NULL,
  `blogs_desc` varchar(255) DEFAULT NULL,
  `blogs_title` varchar(255) NOT NULL,
  `blogs_imgpath` varchar(255) DEFAULT NULL,
  `blogs_comment` int(11) DEFAULT NULL,
  `blogs_date` datetime DEFAULT NULL,
  `blogs_view` int(11) DEFAULT NULL,
  `blogs_url` varchar(255) NOT NULL,
  `blogs_cont` mediumtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=387 DEFAULT CHARSET=utf8;

/*Data for the table `cnblogs` */

insert  into `cnblogs`(`id`,`blogs_name`,`blogs_desc`,`blogs_title`,`blogs_imgpath`,`blogs_comment`,`blogs_date`,`blogs_view`,`blogs_url`,`blogs_cont`) values (308,'BenchTse','原文地址：http://www.cnblogs.com/pcxie/p/7750074.html 本文译者水平有限，如发现问题请批评指正 Jerasure 2.0:为方便存储相关应用开发的一个基于C开发的纠删码库 版本2.0 James S.Plank Kevin M.Greenan 技术报告 UT ...','jerasure 2.0译文','full/df178d8009a8c7dbf0c0062d449c2c3f833c4c52.jpg',1,'0000-00-00 00:00:00',16,'http://www.cnblogs.com/pcxie/p/7750074.html','原文地址：'),(309,'孤荷凌寒','近来网络上开始流行一种说法——“人人都需要学点儿编程”，各种正式的，专业的解释非常之多，但那些高大上的说明未必人人都能深刻理会，这几天我在不断反省自己的编程学习之路时，也领悟到，是的，人人都需要学点编程——只是我将以自己学习经历来谈谈。 ...','我眼中的人人都需要学点编程——我的信息之路之八','full/139f182eeeb949ddd56d563f673eb67f241a3467.jpg',0,'0000-00-00 00:00:00',64,'http://www.cnblogs.com/lhghroom/p/7751074.html','　　近来网络上开始流行一种说法——“人人都需要学点儿编程”，各种正式的，专业的解释非常之多，但那些高大上的说明未必人人都能深刻理会，这几天我在不断反省自己的编程学习之路时，也领悟到，是的，人人都需要学点编程——只是我将以自己学习经历来谈谈。'),(310,'Aomi','解控制报文格式是学习MQTT中，笔者认为最为重要的一个知识点。MQTT的所有行为都离不开他。控制报文可以分为三个部分组成，分别为：固定报头、可以变报头、有效载荷部分。 注意：上面的说的报文的类型。是指连接(CONNECT)，发布(PUBLISH)等。而等级是指服务质量 (QoS) 。 固定报头 固定 ...','MQTT——控制报文格式','full/0ae34e3327b50c374a0d42553dc6714447ceed44.jpg',0,'0000-00-00 00:00:00',22,'http://www.cnblogs.com/hayasi/p/7743356.html','解控制报文格式是学习MQTT中，笔者认为最为重要的一个知识点。MQTT的所有行为都离不开他。控制报文可以分为三个部分组成，分别为：固定报头、可以变报头、有效载荷部分。'),(311,'少年张翠山','好久没有更新博客了，偶然间翻开自己的博客列表，最近一篇还是在八月初时候写的。而且最近也没有硬文章或者是干货来放送。再不更新啊，估计博客就真的荒废了。 不经意间，十月份又过去了，现在来为十月份做一份总结。纵使在公司被差别对待，貌似免去了写周报或者月报的麻烦。但公司的x报是拿给领导看的，而我博客的月报是... ...','十月工作总结：勿忘初心，继续前行','full/aeb289f440b574195964785362984a78054b4f3f.jpg',0,'0000-00-00 00:00:00',99,'http://www.cnblogs.com/shizongger/p/7750992.html','好久没有更新博客了，偶然间翻开自己的博客列表，最近一篇还是在八月初时候写的。而且最近也没有硬文章或者是干货来放送。再不更新啊，估计博客就真的荒废了。'),(312,'NingHeChuan','本篇实现Arduino与FPGA交互，当然也没有什么新的协议，还是基于串口通讯，现在学一个串口通信基本上可以驱动大多数模块了，而且和各种单片机无缝数据交互，Arduino由于其强大的库函数支持，在实现很多事情上会方便很多，比如串口通讯，Arduino就两行的代码，Verilog至少也得上百行，但是从 ...','Arduino上传数据至贝壳物联并与FPGA进行交互','full/41b893578aea62e8df7d963845da334c921ad06c.jpg',0,'0000-00-00 00:00:00',13,'http://www.cnblogs.com/ninghechuan/p/7751382.html','         本篇实现Arduino与FPGA交互，当然也没有什么新的协议，还是基于串口通讯，现在学一个串口通信基本上可以驱动大多数模块了，而且和各种单片机无缝数据交互，Arduino由于其强大的库函数支持，在实现很多事情上会方便很多，比如串口通讯，Arduino就两行的代码，Verilog至少也得上百行，但是从学习知识的角度上来说，学Arduino也只不过是学了一门软件操控硬件的方法罢了，而且很多东西都简化了，跟在电脑上编程没什么两样，还不如学学单片机。最起码还能了解其内部各种寄存器的使用。我用Arduino也就是玩玩，当然还是有了很多不一样的体验，都知道Arduino是开源项目，我们可以免费使用别人的代码，当然也要分享出来自己的代码，将开源进行到底。'),(313,'Python学习者','十分钟学会Pandas 这是关于Pandas的简短介绍主要面向新用户。你可以参考Cookbook了解更复杂的使用方法 习惯上，我们这样导入： 创建对象 请参阅数据结构简介部分 通过传递一个列表的值创建一个Series，让Pandas创建一个默认的整数索引： 通过传递的numpy数组创建一个DataF ...','【译】10分钟学会Pandas','full/98aeec975759d762b609068920ca947745158506.jpg',0,'0000-00-00 00:00:00',13,'http://www.cnblogs.com/yan-lei/p/7718744.html','这是关于Pandas的简短介绍主要面向新用户。你可以参考'),(314,'7m鱼','\r\n    上篇文章介绍了如何在ASP.NET MVC项目中引入Identity组件来实现用户注册、登录及身份验证功能，并且也提到了Identity是集成到Owin中的，本章就来介绍一下什么是Owin以及如何使用Owin来增强Identity的功能。 本章的主要内容有： ● 什么是Owin ● 关于Katana ...\r\n    ','ASP.NET没有魔法——Identity与Owin','',1,'0000-00-00 00:00:00',253,'http://www.cnblogs.com/selimsong/p/7743112.html',' 　　上篇文章介绍了如何在ASP.NET MVC项目中引入Identity组件来实现用户注册、登录及身份验证功能，并且也提到了Identity是集成到Owin中的，本章就来介绍一下什么是Owin以及如何使用Owin来增强Identity的功能。'),(315,'Realsdg','前 言 絮叨絮叨 Bootstrap 是基于 HTML、CSS、JAVASCRIPT 的，它简洁灵活，使得 Web 开发更加快捷。 而栅格系统是Bootstrap中的核心，正是因为栅格系统的存在，Bootstrap才能有着如此强大的响应式布局方案。 官方文档中是这样说的： Bootstrap 提供了 ...','Bootstrap的核心——栅格系统的使用','full/fd88ca3a0d5a0ab2298249d725860c777116b393.jpg',1,'0000-00-00 00:00:00',120,'http://www.cnblogs.com/realsdg/p/7750664.html',' '),(316,'博客园团队','最近有用户向我们反馈，修改密码后，怎么也登录不了我们网站，总是提示密码错误。用户确认密码肯定没错，通过用户发给我们的操作截图看，用户修改密码的操作也没问题，而我们这边也没能重现出这个问题。 ...','Chrome 62 的大坑：修改密码后始终使用保存的旧密码登录','full/89a548b57a4673c4633a9233c724c62e073a09bb.jpg',3,'0000-00-00 00:00:00',147,'http://www.cnblogs.com/cmt/p/7750736.html','最近有用户向我们反馈，修改密码后，怎么也登录不了我们网站，总是提示密码错误。用户确认密码肯定没错，通过用户发给我们的操作截图看，用户修改密码的操作也没问题。'),(317,'unclekeith','前端安全之XSS 转载请注明出处：unclekeith: \"前端安全之XSS\" XSS定义 XSS, 即为（Cross Site Scripting）, 中文名为跨站脚本, 是发生在 目标用户的浏览器 层面上的，当渲染DOM树的过程成发生了 不在预期内 执行的JS代码时，就发生了XSS攻击。 跨站脚 ...','前端安全之XSS攻击','full/312e0dc9db33405c04e690c437033703f22e824a.jpg',0,'0000-00-00 00:00:00',69,'http://www.cnblogs.com/unclekeith/p/7750681.html','转载请注明出处：unclekeith: '),(318,'吃鱼大神','Layer layer是一款近年来备受青睐的web弹层组件，她具备全方位的解决方案，致力于服务各水平段的开发人员，您的页面会轻松地拥有丰富友好的操作体验。 在与同类组件的比较中，layer总是能轻易获胜。她尽可能地在以更少的代码展现更强健的功能，且格外注重性能的提升、易用和实用性！ 如果，你初识la ...','一个让你想到即可做到的web弹窗/层----Layer','full/c3d9ac8adc8b610fd5f708f678bc843b9ebfd2a4.jpg',3,'0000-00-00 00:00:00',193,'http://www.cnblogs.com/sunlizheng/p/7750818.html','是一款近年来备受青睐的web弹层组件，她具备全方位的解决方案，致力于服务各水平段的开发人员，您的页面会轻松地拥有丰富友好的操作体验。'),(319,'balahoho','业务背景 在稍微复杂点业务系统中，不可避免会碰到做定时任务的需求，比如淘宝的交易超时自动关闭订单、超时自动确认收货等等。对于一些定时作业比较多的系统，通常都会搭建专门的调度平台来管理，通过创建定时器来周期性执行任务。如刚才所说的场景，我们可以给订单创建一个专门的任务来处理交易状态，每秒轮询一次订单表 ...','采用简易的环形延时队列处理秒级定时任务的解决方案','full/7423e60617e981f4f817af4985b9f916445670c8.jpg',1,'0000-00-00 00:00:00',151,'http://www.cnblogs.com/hohoa/p/7739271.html',' '),(320,'温斯渤','\r\n    距离上次更新文章已经过去一个多月了，实在是很抱歉没有按照进度更新博客。最近主要是在忙秋招，前几天也刚刚结束，所以这篇文章就来和大家一起分享我的秋招之路。 或许大部分朋友都是从这篇文章————[2017腾讯实习生Android客户端开发面试总结](http://wensibo.top/2017/04/... ...\r\n    ','一个三非渣本的安卓秋招之路','',1,'0000-00-00 00:00:00',132,'http://www.cnblogs.com/ghylzwsb/p/interview.html','\n距离上次更新文章已经过去一个多月了，实在是很抱歉没有按照进度更新博客。最近主要是在忙秋招，前几天也刚刚结束，所以这篇文章就来和大家一起分享我的秋招之路。'),(321,'乔雨大魔王','本文章基本全代码敲窗口小球游戏，最后会免费加上源代码，让读者有更清晰的了解 内容主要覆盖： 1> Qtimer计时器的开始和结束，以及显示系统时间等等。。。 2> 多个Qwidget布局和背景颜色调配 3>小球撞板反弹和小球撞板在Qwidget中分数的传递(就是小球撞一次板，分数加一，并且还要显示出 ...','QT---实现小球游戏（零基础入门）','full/ccc5127250363444cc1d7e3799cea7ec94cfbc92.jpg',0,'0000-00-00 00:00:00',8,'http://www.cnblogs.com/meditation5201314/p/7751472.html','　　本文章基本全代码敲窗口小球游戏，最后会免费加上源代码，让读者有更清晰的了解'),(322,'小破孩92','本篇将介绍python中的列表，更多内容请参考： \"Python学习指南\" 一、序列 在python中有六种内建的序列：列表、元祖、字符串、Unicode字符串、buffer对象he xrange对象。 通用序列操作 所有的序列都可以进行某些特定的操作。这些操作包括： 1. 索引(indexing) ...','python列表','full/70b135ad0860adc195d8336bf98f3301a880f806.jpg',0,'0000-00-00 00:00:00',6,'http://www.cnblogs.com/miqi1992/p/7751489.html','本篇将介绍python中的列表，更多内容请参考：'),(323,'SonoFelice','在狼长正式工作一年有余，对于接触到的新技术的学习已经不再有那么多的畏惧感了，总结一下我对新技术的学习思路，希望能给大家提供一个参考。 工作一年接触的新技术： bigpipe AMQ Elasticsearch k8s docker go 新技术学习思路： 1、语言类： 接触任何语言，首先就是在本机配 ...','新技术学习思路——工作一年的总结','full/c2a8fe328dcfe620628e9b913c4fbf40d9539dc9.jpg',0,'0000-00-00 00:00:00',273,'http://www.cnblogs.com/sonofelice/p/7749938.html','在狼长正式工作一年有余，对于接触到的新技术的学习已经不再有那么多的畏惧感了，总结一下我对新技术的学习思路，希望能给大家提供一个参考。'),(324,'tingxins','前言 本文主要翻译今年 The Swift Programming Language (Swift 4) 中新出的章节 《Memory Safety》。在 Swift 4 中，内存安全访问进行很大的优化( \"《What\'s New in Swift 4 ?》\" )。 默认情况下，Swift 会克服代 ...','关于 Swift 4 中内存安全访问','full/4eb531f8493b337c574d9a7e557798e580ed426c.jpg',1,'0000-00-00 00:00:00',73,'http://www.cnblogs.com/tingxins/p/7750026.html','本文主要翻译今年 The Swift Programming Language (Swift 4) 中新出的章节 -《Memory Safety》。在 Swift 4 中，内存安全访问进行很大的优化('),(325,'lavyun','Fastify 系列教程： \"Fastify 系列教程一 (路由和日志)\" \"Fastify 系列教程二 (中间件、钩子函数和装饰器)\" \"Fastify 系列教程三 (验证、序列化和生命周期)\" 验证 Fastify 可以验证请求信息，只有符合验证规则的请求才会被处理。 JSON Schema 什 ...','Fastify 系列教程三 （验证、序列化和生命周期）','full/f44e509a1c64fd16c788b351859f79f42100055c.jpg',0,'0000-00-00 00:00:00',63,'http://www.cnblogs.com/smartXiang/p/7749737.html','Fastify 可以验证请求信息，只有符合验证规则的请求才会被处理。'),(326,'仪式黑刃','其实本应该从一般性的表讲起的，先说顺序表，再说链表 。但顺序表的应用范围不是很广，而且说白了就是数组的高级版本，他的优势仅在于两点：1.逻辑直观，易于理解。2.查找某个元素只需要常数时间——O(1)，而与此同时，因为每个单元的物理内存都是连续的，所以不便于移动，不便于精细化操作，每次插入和删除都会带 ...','Single linked list by pointer','full/accec2dd6ae3bbebbdbc6ca3785e8eddeb0472d9.jpg',0,'0000-00-00 00:00:00',65,'http://www.cnblogs.com/hongshijie/p/7747113.html',' '),(327,'北漂的雷子','最近一段时间，笔者一直在和我们公司的研发童鞋，运维童鞋等一起努力来搞我们公司的接口，每晚的那个点我们就开始了我们的工作，由于是后期补做，所以在时间上也是那么匆忙，闲暇之余，笔者想着怎么对接口进行详细的功能测试，需要进行一系列的工作，来简化我们测试的工作量，要做的太多，只可惜我们测试太少，精力有限。可 ...','开源接口测试框架之公司应用篇','full/fc7ae3740960b01864c1a60795bffd9a288f4ed1.jpg',0,'0000-00-00 00:00:00',438,'http://www.cnblogs.com/leiziv5/p/7747142.html','          '),(328,'Tracey_W','今天给大家分享一个JavaScript OOP中关于分辨this指向对象的小技巧，很实用呦！ 我们先来看一段代码： 大家能判断出func();和obj.func();这两句的this指向吗？ 首先，我们都知道的是，this的指向就是最终调用函数的对象。可是最终调用函数的对象，你能清楚地判断出来吗？  ...','JavaScript OOP 之 this指向','full/f50b8c539e9c200a89d56362405863fcea34bff6.jpg',8,'0000-00-00 00:00:00',168,'http://www.cnblogs.com/Tracey-1023/p/7747372.html',' '),(329,'张璨','F查询（取字段的值） 关于查询我们知道有filter( ) ,values( ) , get( ) ,exclude( ) ,如果是聚合分组，还会用到aggregate和annotate，甚至还有万能的双下划线，但是如果有这样一个需求，查询a表中的aa字段数值大于b表中bb字段数值，应该怎么做呢，D ...','Python数据库查询之组合条件查询-F&Q查询','full/5c2ffaad53d17caca556fcab1d705d822de196b4.jpg',0,'0000-00-00 00:00:00',98,'http://www.cnblogs.com/zhang-can/p/7745809.html','F查询（取字段的值）'),(330,'solenovex','我要使用asp.net core 2.0 web api 搭建一个基础框架并立即应用于一个实际的项目中去. 这里需要使用identity server 4 做单点登陆. 下面就简单学习一下相关的预备知识. 基于Token的安全验证体系 这个比较简单, 简单来说就是为了证明我们有访问权限, 我们首先需 ...','学习Identity Server 4的预备知识','full/2580a4909b5059ea22ca7eba723370da1c3fe737.jpg',1,'0000-00-00 00:00:00',145,'http://www.cnblogs.com/cgzl/p/7746496.html','我要使用asp.net core 2.0 web api 搭建一个基础框架并立即应用于一个实际的项目中去.'),(331,'shoufengwei','前言 上一篇文章中介绍了如何响应鼠标和键盘事件，本文介绍如何加载三维对象并实现给三维对象添加一个漂亮的皮肤。 一、 原理分析 我对三维的理解为：所谓三维对象无非是多个二维对象拼接到一起，贴图就更简单了，就是将一张图片贴到对象上。so easy，那么我们就一步步来实现吧。 二、 创建立方体 2.1 立 ...','PhiloGL学习（4）——三维对象、加载皮肤','full/6940cf62b26e175ce5d697f9c98468071fb8377d.jpg',0,'0000-00-00 00:00:00',72,'http://www.cnblogs.com/shoufengwei/p/7747015.html','上一篇文章中介绍了如何响应鼠标和键盘事件，本文介绍如何加载三维对象并实现给三维对象添加一个漂亮的皮肤。'),(332,'何以堪','要介绍DataFrame和各数据源的IO操作，从各数据源读取数据构造DataFrame，将DataFrame中的数据写到各数据源。 ...','Spark SQL数据源','full/32a5454eede8ef17221df08d8edf26032d3804b7.jpg',0,'0000-00-00 00:00:00',104,'http://www.cnblogs.com/ywjy/p/7747482.html','[TOC]'),(333,'sqdmydxf','\r\n    阿里java开发手册已经发表，很多都值得认真研究思考，看到零度的思考题，没忍住研究了一下。 零度的思考：https://mp.weixin.qq.com/s/dDR21k30s6ZVfDvl8BVQmA 首先，看一下给出的反例的执行结果。 1. 如果是\"1\"，最后list中的元素为[\"2\"] 2.  ...\r\n    ','对foreach循环的思考','',0,'0000-00-00 00:00:00',197,'http://www.cnblogs.com/sqdmydxf/p/7746958.html','阿里java开发手册已经发表，很多都值得认真研究思考，看到零度的思考题，没忍住研究了一下。'),(334,'编程人，在天涯','\r\n    今天本来打算研究一下yii2.0的AR模型的实现原理，然而，计划赶不上变化，突然就想先研究一下yii2.0的数据库组件创建的过程。通过对yii源码的学习，了解了yii组件注册与创建的过程，并发现原来yii组件注册之后并不是马上就去创建的，而是待到实际需要使用某个组件的时候再去创建对应的组件实例的。本 ...\r\n    ','Yii2之组件的注册与创建','',0,'0000-00-00 00:00:00',92,'http://www.cnblogs.com/wujuntian/p/7745136.html',' '),(335,'weiqinl','前言 web应用程序，切换主题，给其换肤，是一个比较常见的需求。 如何能快速的切换主题色？(只有固定的一种皮肤) 如果又想把主题色切换为以前的呢？（有多种可切换的皮肤） 该以何种方式编写标签的css属性？ 快速切换主题这个需求，它考验了项目的CSS代码，是否具有可维护性、可扩展性。 css要如何编写 ...','基于ElementUI的网站换主题的一些思考与实现','full/fd6315a8333925deabece3ac40715d180bab1a8a.jpg',3,'0000-00-00 00:00:00',486,'http://www.cnblogs.com/weiqinl/p/7732892.html','web应用程序，切换主题，给其换肤，是一个比较常见的需求。'),(336,'pray_REQ','以下要讲的案例来自于《Spring 3.X 企业应用开发实战》这本书。 针对我一周的摸索，现在总结几个易错点，当然，这是在我自己犯过错误的前提下总结出来的，如果有说的不到位的地方，欢迎大家指出。所使用的代码均出自《Spring 3.X 企业应用开发实战》chapter2，代码什么的都不重要，差别不大 ...','使用Spring框架实现用户登录实例','full/5b6a933217839f9622046cd0ac54de49f27e3086.jpg',2,'0000-00-00 00:00:00',210,'http://www.cnblogs.com/bing-newyearday/p/7747706.html',' '),(337,'BenchTse','前言 本文搭建了一个由三节点（master、slave1、slave2）构成的Hadoop完全分布式集群（区别单节点伪分布式集群），并通过Hadoop分布式计算的一个示例测试集群的正确性。 本文集群三个节点基于三台虚拟机进行搭建，节点安装的操作系统为Centos7（yum源），Hadoop版本选取为 ...','Hadoop2.8.1完全分布式环境搭建','full/df178d8009a8c7dbf0c0062d449c2c3f833c4c52.jpg',0,'0000-00-00 00:00:00',178,'http://www.cnblogs.com/pcxie/p/7747317.html',' '),(338,'ywliao','版权声明：本文为博主原创文章，转载请注明出处   机器学习的研究领域是发明计算机算法，把数据转变为智能行为。机器学习和数据挖掘的区别可能是机器学习侧重于执行一个已知的任务，而数据发掘是在大数据中寻找有价值的东西。 机器学习一般步骤 收集数据，将数据转化为适合分析的电子数据 探索和 ...','R语言进行机器学习方法及实例（一）','full/8d5c9338e901a370601abbf41e2df03eee48c296.jpg',0,'0000-00-00 00:00:00',178,'http://www.cnblogs.com/ywliao/p/7182090.html','版权声明：本文为博主原创文章，转载请注明出处'),(339,'白菜白','对于AngularJS什么，小编在这就不多做介绍了。大家可以看小编的上一篇博客。 言归正传，小编在上一篇博客中介绍了AngularJS中的指令、表达式还有非常实用的三种服务。接下来，带大家看一看AngularJS中的$http、表格、dom及事件，当然还有其动画以及极其重要的路由。 作为一个前端程序 ...','媲美jQuery的JS框架----AngularJS（二）','full/bc6a923690dfcc554411b4c996501d54966778c8.jpg',5,'0000-00-00 00:00:00',407,'http://www.cnblogs.com/zxt-17862802783/p/7747256.html','对于AngularJS什么，小编在这就不多做介绍了。大家可以看小编的上一篇博客。'),(340,'老坏猫','一、 网关的功能：承上启下 最近有点忙，更新慢了。感谢园友们给予的支持，现在github上已经有。目标是最好的开源组态，看来又近一步^^ 之前有提到网关是物联网的关键环节，它的作用就是承上启下。 下位机有下位机的语言，上位机有上位机的思路。网关就是一个翻译，把下位机的语言转成通用语，再告诉上位机该怎 ...','开源纯C#工控网关+组态软件(四)上下位机通讯原理','full/3501eb8ac178332a4394a00c32a01d3d9b2df6aa.jpg',0,'0000-00-00 00:00:00',502,'http://www.cnblogs.com/evilcat/p/7743970.html',' '),(341,'龙恩0707','理解vue中的scope的使用 我们都知道vue slot插槽可以传递任何属性或html元素，但是在调用组件的页面中我们可以使用 template scope=\"props\"来获取插槽上的属性值，获取到的值是一个对象。注意：scope=\"它可以取任意字符串\";上面已经说了 scope获取到的是一个对 ...','理解vue中的scope的使用','full/f013aba6ab7f9616a15937cee2a26684925ce552.jpg',2,'0000-00-00 00:00:00',165,'http://www.cnblogs.com/tugenhua0707/p/7745735.html','理解vue中的scope的使用'),(342,'杉枫','推荐系统怎样稳定高效提供服务，持续不断满足业务需求，持续不断面对技术挑战，是每一个服务端开发同学应该持续思考，和持续不断优化线上服务。 以前我们开发的程序更多的是网站，并且以单体服务形式构建，好处是整个程序一次构建，维护方便，但当公司发展后，组织机构变大，程序由多个人维护，单体程序维护成本高，难于修 ...','个性化推荐系统（四）--- 推荐系统服务端','full/d3fd9a56da76bc6f3012517d0d754b5d11d691c2.jpg',0,'0000-00-00 00:00:00',266,'http://www.cnblogs.com/freedommovie/p/7745920.html',' 推荐系统怎样稳定高效提供服务，持续不断满足业务需求，持续不断面对技术挑战，是每一个服务端开发同学应该持续思考，和持续不断优化线上服务。'),(343,'仪式黑刃','砝码称重 有了对母函数的一般认识后，我们可以用它来解决一些简单的计数问题，比如说下面这道题：我们有1，2，3，4g四个砝码，一共可以称出多少种重量；而且，对于某一个重量，共有多少种称法？这个可以直接用母函数求解，1g的对应1+x，2g的对应1+x2，以此类推。所以整个母函数就是G(x)=(1+x)( ...','母函数应用','full/accec2dd6ae3bbebbdbc6ca3785e8eddeb0472d9.jpg',0,'0000-00-00 00:00:00',97,'http://www.cnblogs.com/hongshijie/p/7745934.html',' '),(344,'shoufengwei','前言 上一篇文章中介绍了如何让对象动起来，本文介绍如何让场景响应我们的鼠标和键盘以控制场景的缩放及对象的转动和移动等。 一、 原理分析 有了上一篇文章的基础，我们已经知道了如何让场景和对象动起来。本文我们通过键盘和鼠标来控制对象的动作，这就有点Game的意思了。对程序员来说，这其实是个很easy的事 ...','PhiloGL学习（3）——程序员的法宝—键盘、鼠标','full/6940cf62b26e175ce5d697f9c98468071fb8377d.jpg',0,'0000-00-00 00:00:00',93,'http://www.cnblogs.com/shoufengwei/p/7745901.html','上一篇文章中介绍了如何让对象动起来，本文介绍如何让场景响应我们的鼠标和键盘以控制场景的缩放及对象的转动和移动等。'),(345,'YSOcean','前一篇博客我们讲解了Linux文件和目录处理命令，还是老生常淡，对于新手而言，我们不需要完全记住命令的详细语法，记住该命令能完成什么功能，然后需要的时候去查就好了，用的多了我们就自然记住了。这篇博客我们接着讲Linux命令——链接命令和权限管理命令。 1、链接命令 一、生成链接文件命令：ln ①、命 ...','Linux系列教程（五）——Linux链接命令和权限管理命令','full/5155848fe0d4fce78605a7289a81ad87a0d4134c.jpg',1,'0000-00-00 00:00:00',124,'http://www.cnblogs.com/ysocean/p/7712425.html','　　前一篇博客我们讲解了'),(346,'听醒木一声收','上一期简单讲解了vue的基本语法，这一次我们做一个小项目，搭建一个简单的图书管理平台，能够让我们更深刻的理解这门语言的妙用。 ...','vue.js快速搭建图书管理平台','full/d983f9299f64d733aa76cb806d74f28fda1af0f4.jpg',12,'0000-00-00 00:00:00',1403,'http://www.cnblogs.com/lihaohai/p/7745978.html',' '),(347,'看见2016','\r\n    下表为是否适合打垒球的决策表，预测E= {天气=晴，温度=适中，湿度=正常，风速=弱} 的场合，是否合适中打垒球。 天气 温度 湿度 风速 活动 晴 炎热 高 弱 取消 晴 炎热 高 强 取消 阴 炎热 高 弱 进行 雨 适中 高 弱 进行 雨 寒冷 正常 弱 进行 雨 寒冷 正常 强 取消 阴 寒 ...\r\n    ','机器学习之决策树算法','',0,'0000-00-00 00:00:00',128,'http://www.cnblogs.com/kanjian2016/p/7746005.html','E= {'),(348,'lovesoo','Robot Framework是一款python语言编写，通用的功能自动化测试框架。它使用了比较易用的表格数据语法，基于关键字驱动测试，主要用来验收测试和验收测试驱动开发（ATDD）。 本文主要介绍Robot Framework在python2.7环境下的安装及一个http接口自动化测试demo。 ...','Robot Framework自动化测试框架初探','full/92725e6ec2d73a3bab20f40863812b94806eb1e5.jpg',0,'0000-00-00 00:00:00',140,'http://www.cnblogs.com/lovesoo/p/7748487.html','本文主要介绍'),(349,'等你归去来','虽说工作就是简单的事情重复做，但不是所有简单的事你都能有机会做的。 我们平日工作里，大部分时候都是在做修修补补的工作，而这也是非常重要的。做好修补工作，做好优化工作，足够让你升职加薪！ 但是如果有机会，去尝试些自己平日里少做的事，我觉得是一件值得庆幸的事。 前段时间，接了个新项目。只有一些idea在 ...','一份从0到1的java项目实践清单','full/f5a3542a652bb90869da43b90062bac7afd901c6.jpg',0,'0000-00-00 00:00:00',209,'http://www.cnblogs.com/yougewe/p/7749444.html','　　虽说工作就是简单的事情重复做，但不是所有简单的事你都能有机会做的。'),(350,'张善友','2017年10月31至11月3日，由微软举办的Tech Summit 2017技术暨生态大会将在北京盛大举办，要在北京连开四天。今年的技术大会看头十足，不仅有大咖级人物带来十二大主题课程，更有三天四场的主题之夜。微软技术大会最早是由微软技术教育大会TechED演变而来。从今年“智 · 远”的主题、百 ...','微软Tech Summit 2017，等你来打Call','full/80dbaa6a62f22d8120852f438ca89a8c11e5d2f1.jpg',0,'0000-00-00 00:00:00',305,'http://www.cnblogs.com/shanyou/p/7746066.html','2017年10月31至11月3日，由微软举办的Tech Summit 2017技术暨生态大会将在北京盛大举办，要在北京连开四天。今年的技术大会看头十足，不仅有大咖级人物带来十二大主题课程，更有三天四场的主题之夜。微软技术大会最早是由微软技术教育大会TechED演变而来。从今年“智 · 远”的主题、百余场主题课程以及四场主题之夜来看，今年的技术大会看头十足，不仅有大咖级人物带来十二大主题课程，更有三天四场的主题之夜。微软每一次技术更迭也被视为下一次技术革命的风向标，无论炫目的AR技术，还是前沿的认知技术和人工智能，微软都时常让人耳目一新，眼前一亮。'),(351,'min.jiang','\r\n    上下文 记的学英语的时候，总是不记的某个词是什么意思，然后就看不下去了，只能问周围的同学或者老师或者去查词典，他们的建议是通过上下文去推测这个词大概的意思,反正我那会上学时没理解，所以英文一直比较差。 现在英语水平也没提高多少，尽管有点领会。 后来慢慢理解了一些，因为有些词有很多种意思，放在某个场景 ...\r\n    ','简易RPC框架-上下文','',0,'0000-00-00 00:00:00',283,'http://www.cnblogs.com/ASPNET2008/p/7749242.html','记的学英语的时候，总是不记的某个词是什么意思，然后就看不下去了，只能问周围的同学或者老师或者去查词典，他们的建议是通过上下文去推测这个词大概的意思,反正我那会上学时没理解，所以英文一直比较差。'),(352,'慕容小匹夫','此次主题夜活动由微软和Unity独家联合举办，由MR领域的专家大咖领衔，带你领略别样的行业领域知识和最实际的经验；趣味体验环节，花样体会技术魅力和多样的前沿产品。让您紧跟技术产业风向，拥抱时代浪潮，分享、学习、体验、成长。 ...','微软Tech Summit 2017，微软携手Unity打造MR之夜','full/0ee871040730f6c5e54890d8c62c78c08bf1c396.jpg',11,'0000-00-00 00:00:00',734,'http://www.cnblogs.com/murongxiaopifu/p/7749515.html','2017年10月31日至11月3日，微软将在北京举办Tech Summit 2017技术暨生态大会。今年的大会不仅有大咖级人物带来的十二大主题、百余场课程，而且还会迎来最特别的一位嘉宾——微软公司首席执行官Satya Nadella。'),(353,'chuanbao','首页我们先来解释一下下JQuerymobile是什么，jQuery Mobile是JQuery 框架的一个组件（而非jquery的移动版本）。jQuery Mobile是一款基于HTML5的用户界面系统 是用于创建移动 Web 应用的前端开发框架，可以应用于智能手机与平板电脑，而且使用 HTML5  ...','JQuerymobile实例源代码','full/74babdfbd2636dff609c3f85bc0b29b01b09719c.jpg',1,'0000-00-00 00:00:00',139,'http://www.cnblogs.com/lgc-17862800193/p/7746078.html','首页我们先来解释一下下JQuerymobile是什么，jQuery Mobile是JQuery'),(354,'天下！行','\r\n    方便自己，方便他人，记一次连接oracle的经历，使用 【Oracle官方非托管Odac驱动，Oracle.DataAccess.Client】连接数据库的时候程序会报错，找了很久都不知道是什么原因，原来是本机没有安装客户端。在不安装客户端的情况下，将连接驱动改为【Oracle官方托管odac驱动， ...\r\n    ','Oracle官方非托管Odac驱动与Oracle官方托管odac驱动','',0,'0000-00-00 00:00:00',126,'http://www.cnblogs.com/txqx/p/7746118.html','方便自己，方便他人，记一次连接oracle的经历，使用 【Oracle官方非托管Odac驱动，Oracle.DataAccess.Client】连接数据库的时候程序会报错，找了很久都不知道是什么原因，原来是本机没有安装客户端。在不安装客户端的情况下，将连接驱动改为【Oracle官方托管odac驱动，Oracle.ManagedDataAccess.Client】，程序正常运行'),(355,'千鸟12','\r\n    进入单用户模式 rhel61、在系统数秒时，按下键，进入到系统引导菜单 中2、选择系统后 按“e”键 选择kernel后 按“e”键 后空格 1+回车 b：启动系统 进入到单用户模式 rhel71、在系统数秒时，按下键，进入到系统引导菜单中2、选择系统后 按“e”键 在linux16那一行末尾加上： ...\r\n    ','忘记root密码，进入单用户模式修改密码','',0,'0000-00-00 00:00:00',0,'http://www.cnblogs.com/qianniao12/p/7751548.html','进入单用户模式'),(356,'LineZero','ASP.NET Core 2.0 开源Git HTTP Server，实现类似 GitHub、GitLab。 GitHub：https://github.com/linezero/GitServer 设置 需要先安装Git,并确保git 命令可以执行，GitPath 可以是 git 的绝对路径。 目 ...','ASP.NET Core 开源GitServer 实现自己的GitHub','full/5e95753ec1befad031133dd2e5d1fc51875a1f39.jpg',4,'0000-00-00 00:00:00',435,'http://www.cnblogs.com/linezero/p/gitserver.html','ASP.NET Core 2.0 开源Git HTTP Server，实现类似 GitHub、GitLab。'),(357,'一个柠檬','前 言 上周更新了一篇音乐播放器的博客，因为时间原因，并不完整，有人评论我能不能实现同步显示歌词，今天就来跟大家分享一下，如何实现歌词的同步显示。 这次我们就不写过多的CSS样式了，单纯的实现歌词的同步显示，先看一下效果。 上周我们提到的audio标签，这次我们直接在audio标签中添加contro ...','更新~音乐播放器的同步显示歌词','full/d05935542e2ff39defbabed5d7604beac76da1d3.jpg',4,'0000-00-00 00:00:00',436,'http://www.cnblogs.com/1996zy/p/7746430.html',' '),(358,'crawl+','以 ArrayList 为例介绍了数据结构中的顺序线性表的知识，设计了 ArrayList 的源码分析和实现原理等。 ...','顺序线性表 ---- ArrayList 源码解析及实现原理分析','full/06ff0d0623f20ffbfb5f4a0c31eae731183c1f51.jpg',0,'0000-00-00 00:00:00',110,'http://www.cnblogs.com/crawl/p/7738888.html','原创播客，如需转载请注明出处。原文地址：'),(359,'郑陆伟','最近负责的一些项目开发，都用到了微信支付（微信公众号支付、微信H5支付、微信扫码支付、APP微信支付）。在开发的过程中，在调试支付的过程中，或多或少都遇到了一些问题，今天总结下，分享，留存。 ...','微信公众号支付|微信H5支付|微信扫码支付|小程序支付|APP微信支付解决方案总结','full/605e43a0f314762b70edf3dc87bd13655dcc2e1c.jpg',1,'0000-00-00 00:00:00',359,'http://www.cnblogs.com/zhengluwei/p/7746095.html','最近负责的一些项目开发，都用到了微信支付（微信公众号支付、微信H5支付、微信扫码支付、APP微信支付）。在开发的过程中，在调试支付的过程中，或多或少都遇到了一些问题，今天总结下，分享，留存。'),(360,'q303248153','在 \"上一篇\" 我们对CoreCLR中的JIT有了一个基础的了解, 这一篇我们将更详细分析JIT的实现. JIT的实现代码主要在 \"https://github.com/dotnet/coreclr/tree/master/src/jit\" 下, 要对一个的函数的JIT过程进行详细分析, 最好的办法 ...','CoreCLR源码探索(八) JIT的工作原理(详解篇)','full/d2b321299055788af3c5ad6bfecf5c346d8d0450.jpg',2,'0000-00-00 00:00:00',175,'http://www.cnblogs.com/zkweb/p/7746222.html','在'),(361,'我吃小月饼','前 言 LiuDaP 今天就给大家介绍一个特别基础的东西，javascript中函数的一点儿小知识（js代码的执行顺序），希望对大家有那么一点点帮助吧！！！ 严格意义上来说，javascript没有多线程的概念，所有的程序都是单线程依次执行的。 1、什么是单线程？ 通俗点说，就是代码在执行过程中，另 ...','js代码执行顺序问题','full/fd2dc4ad9ce3da42fb622724172c24b1311b7918.jpg',9,'0000-00-00 00:00:00',447,'http://www.cnblogs.com/interesting-me/p/7745952.html',' 　　'),(362,'Mushishi_xu','​9.1 等待函数的使用 9.1.1 为什么要使用等待函数 我们在做自动化的时候很多时候都不是很顺利，不是因为app的问题，我们的脚本也没问题，但是很多时候都会报错，比如一个页面本来就有id为1的这个元素，可是我无论怎么定位他都没办法操作，然后报错，这个是怎么个情况呢？因为当我们app打开一个页面的 ...','Appium python自动化测试系列之等待函数如何进行实战（九）','full/f534088fa651b943ff871757734b55a6568a8d03.jpg',0,'0000-00-00 00:00:00',6,'http://www.cnblogs.com/Mushishi_xu/p/7751523.html','我们在做自动化的时候很多时候都不是很顺利，不是因为app的问题，我们的脚本也没问题，但是很多时候都会报错，比如一个页面本来就有id为1的这个元素，可是我无论怎么定位他都没办法操作，然后报错，这个是怎么个情况呢？因为当我们app打开一个页面的时候我们的appium的运行速度过快那么可能害没有将页面的资源解析完成然后你就去操作了，这样能行吗？肯定不行的，这样不报错谁错呢？所以在很多的时候我们都需要加载等待时间的。那我们是不是盲目的去每个页面都加载等待时间呢？'),(363,'孤雁11','tomcat的基础知识 一、tomcat的定义 apache的官网是这么说的：使用Apache Tomcat ®软件了Java Servlet，JavaServer页，Java表达式语言和Java的WebSocket技术的一个开源实现。Java Servlet，JavaServer Pages，Ja ...','tamcat的使用','full/5e980b333533002a5dad3ad65ce8610b4dfc2b73.jpg',0,'0000-00-00 00:00:00',2,'http://www.cnblogs.com/story1/p/7751530.html','tomcat的基础知识'),(364,'换个影子','前 言 在如今的生活中，手机已经与我们的生活紧紧的联系在了一起。而手机APP更是其中，重要的一环。今天，影子就为大家介绍一种开发手机APP的超级神器 ionic。 ionic 是一个强大的 HTML5 应用程序开发框架(HTML5 Hybrid Mobile App Framework )。 可以帮 ...','开发手机APP的神器  ---   ionic','full/bae3600dc1936cc7212e97cad9542f2f4d7a6fb4.jpg',4,'0000-00-00 00:00:00',643,'http://www.cnblogs.com/2502778498spw/p/7748294.html',' '),(365,'追寻的鹿','声明：本篇博文是学习《机器学习实战》一书的方式路程，系原创，若转载请标明来源。 1 决策树的基础概念 决策树分为分类树和回归树两种，分类树对离散变量做决策树 ,回归树对连续变量做决策树。决策树算法主要围绕两大核心问题展开:第一, 决策树的生长问题 , 即利用训练样本集 , 完成决策树的建立过程 。第 ...','机器学习之决策树（ID3 、C4.5算法）','full/7698aa0ef306ac83a738cca22535e34cd01ac848.jpg',0,'0000-00-00 00:00:00',0,'http://www.cnblogs.com/pursued-deer/p/7751552.html','     决策树分为分类树和回归树两种，分类树对离散变量做决策树 ,回归树对连续变量做决策树。决策树算法主要围绕两大核心问题展开:第一, 决策树的生长问题 , 即利用训练样本集 , 完成决策树的建立过程 。第二, 决策树的剪枝问题,即利用检验样本集 , 对形成的决策树进行优化处理。这里主要介绍分类树的两个经典算法：ID3算法和C4.5算法，他们都是以信息熵作为分类依据，ID3 是用信息增益，而C4.5 是利用信息增益率。并且都是单棵决策树。'),(366,'zishengY','\r\n    摘要：在生产环境上对服务器进行网络参数（比如CPU、内存等）的监控是很必要的，比如当服务器网络参数如内存不够用、磁盘空间快要占满时及时通知运维人员进行处理，保证服务器系统的安全。而zabbix就是这么一个非常流行且方案成熟的网监控解决方案，这篇文章主要分享我这两天部署zabbix经验【我搞zabbi ...\r\n    ','我搞zabbix的那两天（1）','',4,'0000-00-00 00:00:00',152,'http://www.cnblogs.com/zishengY/p/7746953.html','CPU、内存等）的监控是很必要的，比如当服务器网络参数如内存不够用、磁盘空间快要占满时及时通知运维人员进行处理，保证服务器系统的安全。而zabbix就是这么一个非常流行且方案成熟的网监控解决方案，这篇文章主要分享我这两天部署zabbix经验【'),(367,'请叫我大苏','网上一些分析的文章有说，RecyclerView 在复用时会按顺序去 mChangedScrap, mAttachedScrap 等等缓存里找，没有找到再往下去找，从代码上来看是这样没错，但我觉得这样表述有问题。因为就我们这篇文章基于 RecyclerView 的滑动场景来说，新卡位的复用以及旧卡位... ...','基于场景解析RecyclerView的回收复用机制原理','full/c5411bbfa8ee891dbbb485d8fcc0644f3c1c0993.jpg',0,'0000-00-00 00:00:00',52,'http://www.cnblogs.com/dasusu/p/7746946.html','最近在研究 RecyclerView 的回收复用机制，顺便记录一下。我们知道，RecyclerView 在 layout 子 View 时，都通过回收复用机制来管理。网上关于回收复用机制的分析讲解的文章也有一大堆了，分析得也都很详细，什么四级缓存啊，先去 mChangedScrap 取再去哪里取啊之类的；但其实，我想说的是，RecyclerView 的回收复用机制确实很完善，覆盖到各种场景中，但并不是每种场景的回收复用时都会将机制的所有流程走一遍的。举个例子说，在 setLayoutManager、setAdapter、notifyDataSetChanged 或者滑动时等等这些场景都会触发回收复用机制的工作。但是如果只是 RecyclerView 滑动的场景触发的回收复用机制工作时，其实并不需要四级缓存都参与的。'),(368,'仪式黑刃','有了指针实现看似已经足够了，那为什么还要有另外的实现方式呢？原因是诸如BASIC和FORTRAN等许多语言都不支持指针，如果需要链表而又不能使用指针，那么就必须使用另外的实现方法。还有一个原因，是在ACM-ICPC，OI等竞赛中，比赛时间有限，用指针写起来太费事，而且数量不多的情况下，用数组实现的脸 ...','Single linked list by cursor','full/accec2dd6ae3bbebbdbc6ca3785e8eddeb0472d9.jpg',0,'0000-00-00 00:00:00',57,'http://www.cnblogs.com/hongshijie/p/7748098.html',' '),(369,'5只猫','一：需求 做一个类似于安卓的弹出消息框，如图。当用户点击下载或者选择时，能够从底部弹出一个提示框，用于提示用户。 二：Popup 类 不需要我们自己额外去写一个弹窗类，微软自己有一个Popup 弹窗类。当弹窗打开时，会自动放在当前应用页面的最顶层。 Popup类里有一个Child属性，用来存弹窗中的 ...','UWP Popup 弹出提示框','full/138a55c873be63016f3779fa55809d89a1217958.jpg',0,'0000-00-00 00:00:00',154,'http://www.cnblogs.com/MzwCat/p/7748033.html','做一个类似于安卓的弹出消息框，如图。当用户点击下载或者选择时，能够从底部弹出一个提示框，用于提示用户。'),(370,'寻找任大侠','全文目录 1 篇首语：挑战MIT计算机课程 2 看我怎么驾驭MIT计算机科学的课程（斯考特·杨） 2.1 为什么临时抱佛脚没用？ 2.2 你能加速理解吗？ 3 钻研：你学得更快 3.1 第一阶段：知识面覆盖 3.2 第二阶段：练习 3.3 第三阶段：自省 4 费曼技巧 4.1 对付你完全摸不着头脑的 ...','十天内掌握线性代数-斯考特·杨的快速自学方法','full/346dff48ada96d5b96299212b8bd4a05981b80f5.jpg',0,'0000-00-00 00:00:00',251,'http://www.cnblogs.com/xunzhaorendaxia/p/7747845.html','1 篇首语：挑战MIT计算机课程'),(371,'弗兰克的猫','今天要说的是Java中两个非常重要的概念——类和对象。 什么是类，什么又是对象呢？类是对特定集合的概括描述，比如，人，这个类，外在特征上，有名字，有年龄，能说话，能吃饭等等，这是我们作为人类的相同特征，那么对象呢？我们口口声声说要面向对象编程，可是找了这么久也没找到对象，这还怎么编程（滑稽）。此对象 ...','【JAVA零基础入门系列】Day11 Java中的类和对象','full/21664aa2a1e97159573c20ce7220696301651529.jpg',0,'0000-00-00 00:00:00',147,'http://www.cnblogs.com/mfrank/p/7747587.html','　　今天要说的是Java中两个非常重要的概念——类和对象。'),(372,'Kavlez','基本配置 不用任何插件的情况下，先按如下配置: set nu syntax on set hlsearch set tabstop=4 set shiftwidth=4 set expandtab set smartcase set ic colorscheme srcery-drk Vundle  ...','Vim - 常用配置','full/2af16b2dc83793134906c0c7c5087499daf97f31.jpg',0,'0000-00-00 00:00:00',142,'http://www.cnblogs.com/kavlez/p/vimrc-tips.html','不用任何插件的情况下，先按如下配置:'),(373,'Eric zhou','搭建了Nginx集群后，需要继续深入研究的就是日常Nginx监控。 Nginx如何监控？相信百度就可以找到：nginx-status 通过Nginx-status，实时获取到Nginx监控数据后，如何和现有监控系统集成？一个很好的解决方案： Nginx+Telegraf+Influxdb+Grafa ...','[原创]Nginx监控-Nginx+Telegraf+Influxb+Grafana','full/13f56e0988b8e92002a16c7e6941df41beacdfac.jpg',3,'0000-00-00 00:00:00',202,'http://www.cnblogs.com/tianqing/p/7745436.html','搭建了Nginx集群后，需要继续深入研究的就是日常Nginx监控。'),(374,'firs大风吹','一般而言，工厂模式分为3种，简单工厂模式，工厂方法模式，抽象工厂模式。这三种工厂模式逐层深入吧。 一，从springWeb.jar包使用抽象工厂模式的一个例子聊起 之前对spring各种痴迷，所以在需要发送http请求时，用了spring自带的http客户端，上代码： 上UML图，首先是工厂类： 产 ...','java设计模式-工厂模式（springweb为例子）','full/014f3de2d0472da2d6d69138a378a9263e80119a.jpg',0,'0000-00-00 00:00:00',115,'http://www.cnblogs.com/sundaymorning/p/7489348.html','一般而言，工厂模式分为3种，简单工厂模式，工厂方法模式，抽象工厂模式。这三种工厂模式逐层深入吧。'),(375,'孤独的居士','\r\n    | 版权：本文版权归作者和博客园共有，欢迎转载，但未经作者同意必须保留此段声明，且在文章页面明显位置给出原文连接。如有问题，可以邮件：wangxu198709@gmail.com 前言 相信很多人都有使用过sqlite3的经验，一年前因为项目上的需要，写了一个基于sqlite3的持久化队列库(per ...\r\n    ','用gdb调试python多线程代码-记一次死锁的发现','',0,'0000-00-00 00:00:00',111,'http://www.cnblogs.com/sting2me/p/7745551.html','版权：本文版权归作者和博客园共有，欢迎转载，但未经作者同意必须保留此段声明，且在文章页面明显位置给出原文连接。如有问题，可以邮件：wangxu198709@gmail.com'),(376,'闪客sun','一次项目架构和性能上的优化，该项目功能更描述十分简单，但可以说麻雀虽小五脏俱全，可以掌握Java很多优化性能的知识。 ...','初探性能优化——2个月到4小时的性能提升','full/b37b73ebf1578e7d2c99e347e4058f04d1f51407.jpg',19,'0000-00-00 00:00:00',1478,'http://www.cnblogs.com/flashsun/p/7744466.html','　　一直不知道性能优化都要做些什么，从哪方面思考，直到最近接手了一个公司的小项目，可谓麻雀虽小五脏俱全。让我这个编程小白学到了很多性能优化的知识，或者说一些思考方式。真的感受到任何一点效率的损失放大一定倍数时，将会是天文数字。最初我的程序计算下来需要跑'),(377,'黑楼绝','背景： 10月28日的一个早上，老黑一如往常地练习，我测试不破坏，当时我找到sqli-libs 游戏，可是我没有立即开始，于是，奇妙的事情就由php开始了。ubuntu16.04安装相关环境 apache，php，mysql (参考网站)，一切都很顺利，但是在启动创建sqli-libs需要的secu ...','【20171028早】ubuntu 16.04 LTS 安装php遇到的问题','full/9ea567207ee259a1500bc2bbcda335a290dac0f9.jpg',0,'0000-00-00 00:00:00',66,'http://www.cnblogs.com/heijuelou/p/7746904.html','  背景：'),(378,'三目鸟','\r\n    这里介绍一下Java web 入门级开发中常用的代码调式方法; ( 仅供入门级童靴 参考) ; 工具: chrome 浏览器 (版本越高越好); Java web 入门级开发 主要就是两个方面: Java 操作数据库 JDBC ; 和 Java 输出 页面 : JSP ; 所以本文的思路也就是按照这 ...\r\n    ','java web 入门级 开发 常用页面调试方法','',0,'0000-00-00 00:00:00',202,'http://www.cnblogs.com/sanmubird/p/7745725.html','这里介绍一下Java web 入门级开发中常用的代码调式方法;  (  仅供入门级童靴 参考) ;'),(379,'大转转FE','HTML5的Websocket（理论篇 I） ** 先请来TA的邻居：** http：无状态、基于tcp请求/响应模式的应用层协议 （A:哎呀，上次你请我吃饭了么? B:我想想, 上次请你吃了么） tcp：面向连接、保证高可靠性(数据无丢失、数据无失序、数据无错误、数据无重复到达) 传输层协议。（看 ...','HTML5的Websocket（理论篇 I）','full/5f338d145f366aa3806f0fb42948903a794d002d.jpg',0,'0000-00-00 00:00:00',305,'http://www.cnblogs.com/zhuanzhuanfe/p/7744577.html','** 先请来TA的邻居：**'),(380,'sphere','相比新的网络请求框架Volley真的很落后，一无是处吗，要知道Volley是由google官方推出的，虽然推出的时间很久了，但是其中依然有值得学习的地方。 从命名我们就能看出一些端倪，volley中文意为群射，齐射，官方解释说它适合通信频繁但是数据量不大的网络请求操作( a burst or emi ...','温故而知新 Volley源码解读与思考','full/f1e589433990532febd3117e17927912ef9251a5.jpg',0,'0000-00-00 00:00:00',84,'http://www.cnblogs.com/sphere/p/7745304.html','　　相比新的网络请求框架Volley真的很落后，一无是处吗，要知道Volley是由google官方推出的，虽然推出的时间很久了，但是其中依然有值得学习的地方。  从命名我们就能看出一些端倪，volley中文意为群射，齐射，官方解释说它适合通信频繁但是数据量不大的网络请求操作( a burst or emission of many things or a large amount at once )，至于为什么我们解读完源码就知道了。'),(381,'笨兔勿应','\r\n    最近在个性化推荐系统的优化过程中遇到一些问题，大致描述如下：目前在我们的推荐系统中，各个推荐策略召回的item相对较为固定，这样就会导致一些问题，用户在多个推荐场景（如果多个推荐场景下使用了相同的召回策略）、多次请求时得到的结果也较为固定，对流量的利用效率会有所降低；尤其对于行为较少的用户，用来作为 ...\r\n    ','大数据量样本随机采样-蓄水池算法','',0,'0000-00-00 00:00:00',172,'http://www.cnblogs.com/bentuwuying/p/7744652.html','最近在个性化推荐系统的优化过程中遇到一些问题，大致描述如下：目前在我们的推荐系统中，各个推荐策略召回的item相对较为固定，这样就会导致一些问题，用户在多个推荐场景（如果多个推荐场景下使用了相同的召回策略）、多次请求时得到的结果也较为固定，对流量的利用效率会有所降低；尤其对于行为较少的用户，用来作为trigger的行为数据本身就很少，这样就使得召回item同质化较为严重，使得第一个问题更加明显。'),(382,'风吹De麦浪','作用域 作用域：是指变量可访问的范围，他规定了如何查找变量，也就是确定当前执行代码对变量的访问权限。 作用域有两种工作模式： 静态作用域 ：又称为词法作用域，在编译阶段就可以决定变量的引用，由程序定义的位置决定，和代码执行顺序无关，用嵌套的方式解析。 动态作用域 ：在程序运行时候，和代码的执行顺序决 ...','javascript 之作用域-06','full/a029e9792635e00ce2ecf3dc7ac752ee10ac6cc8.jpg',0,'0000-00-00 00:00:00',131,'http://www.cnblogs.com/CandyManPing/p/7744514.html','作用域：是指变量可访问的范围，他规定了如何查找变量，也就是确定当前执行代码对变量的访问权限。'),(383,'start逍遥','Help-->Eclipse Marketpalce...-->搜索JBoss tools->install 勾选Hibernate tools，点击next，进行安装。 注意版本，找自己eclipse版本对应的安装，我的是INDIGO 安装后，重启Eclipse。搞定。 启用Hibernate p ...','使用Hibernate Tools从数据库自动逆向生成Hibernate实体类','full/6e839f78eb0b38640b07047ccc44aa1ea643156a.jpg',0,'0000-00-00 00:00:00',97,'http://www.cnblogs.com/start-fxw/p/7744432.html','　　　　Help-->Eclipse Marketpalce...-->搜索JBoss tools->install'),(384,'行走即歌','\r\n    回顾 通过前两节的学习，我们知道 IServiceCollection 以元数据（ServiceDescriptor）的形式存放着用户注册的服务，它的 IServiceCollection 的拓展方法 BuildServiceProvider 为我们提供一个默认的容器 ServiceProvider ...\r\n    ','解析 .Net Core 注入 (3) 创建对象','',0,'0000-00-00 00:00:00',203,'http://www.cnblogs.com/cheesebar/p/7719907.html','通过前两节的学习，我们知道 IServiceCollection 以元数据（ServiceDescriptor）的形式存放着用户注册的服务，它的 IServiceCollection 的拓展方法 BuildServiceProvider 为我们提供一个默认的容器 ServiceProvider，然而创建实例对象的任务并不是由他完成的，具体的是引擎 IServiceProviderEngine（更准确点是抽象类 ServiceProviderEngine） 类型来完成的，可以这么说，整个创建对象的核心功能，都由此抽象类控制完成。具体如下：‘'),(385,'守功','\r\n    最近在完成学校课程的java平时作业，要实现一个计时器，包含开始、暂停以及重置三个功能。由于老师规定要用这个timer类，也就去学习了一下，顺便记录一下。 首先呢去查了一下java手册上的东西，发现timer的构造函数是这么解释的（拿翻译机翻译了） 在指定时间间隔触发一个或多个 ActionEven ...\r\n    ','java swing中Timer类的学习','',0,'0000-00-00 00:00:00',100,'http://www.cnblogs.com/sgatbl/p/7747572.html','最近在完成学校课程的java平时作业，要实现一个计时器，包含开始、暂停以及重置三个功能。由于老师规定要用这个timer类，也就去学习了一下，顺便记录一下。'),(386,'liulun','开篇 开发一个产品（本文“产品”特指移动端软件产品，但是移动端产品的设计流程和方法与PC端的产品并无本质区别）， 可以是一项很简单的事情： 打开IDE，拖几个控件，写几行代码，做一个简单的测试，提交到app store上， 一个下午搞定一个产品； 也可以是一项很复杂的事情： 他可能会包含严格的前期设 ...','产品经理做什么？','full/55961bf239b7c9128e72df6db1b5ab8053bfb7e7.jpg',1,'0000-00-00 00:00:00',333,'http://www.cnblogs.com/liulun/p/7742436.html','开发一个产品（本文“产品”特指移动端软件产品，但是移动端产品的设计流程和方法与PC端的产品并无本质区别），');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
