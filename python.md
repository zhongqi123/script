# 自动化运维
## 1 系统基础信息模块详解

### 1.1 系统性能信息模块psutil

    获取系统运行的进程和系统利用率，以及其他系统信息：
    安装步骤如下：
    1. 安装依赖包
    yum install gcc python-devel
    2. wget https://pypi.python.org/packages/source/p/psutil/psutil-2.1.3.tar.gz 
    3. tar -zxvf psutil-2.1.3.tar.gz
    4. cd psutil-2.1.3
    5. python setup.py install
    举例：
    import psutil
    men=psutil.virtual_memory()
    men.total,men.used
#### 1.1.1获取系统性能信息

    (1) 获取CPU信息
    Linux系统CPU利用率有以下几个部分：
       user time：执行用户进程的时间百分比
       systemctl time:执行内核进程和中断的时间百分比
       wait io:因为io等待而使CPU处于idle空闲状态的时间百分比
       idle：CPU处于idle状态的时间百分比
    *** psutil.cpu_times()获得以上数据以及硬件相关信息，若想获取单独某个，例如：获取user time,则psutil.cpu_times().user ***
    psutil.cpu_count()获得CPU逻辑个数，默认logical=true(logical=False 获取CPU物理个数)
    
    (2) 内存信息
    linux系统内存利用率信息涉及total、used、free、buffers等，分别使用pustil.virtual_memory()与pustil.swap_memory()获取这些信息，示例如下：
    pustil.virtual_memory() 获取内存完整信息
    pustil.virtual_memory().total 获取内存总数
    pustil.swap_memory() 获取SWAP分区信息
    
    (3) 磁盘信息
    pustil.disk_partitions() 获取磁盘完整信息
    pustil.disk_partitions('/') 获取具体分区的使用情况
    pustil.disk_io_counters() 获取磁盘总的io个数
    
    (4) 网络信息
    pustil.net_io_counters() 获取网络总的io信息，默认pernic=False,pernic=true输出每个网络接口的io信息

    (5) 其他系统信息
    pusutil.users() 返回当前登录系统的用户信息
    pusutil.boot_time() 获取开机时间，以时间戳格式返回
    datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S") 修改返回开机时间格式
#### 1.1.2系统进程管理方法

    获取当前系统的进程信息
    (1) 进程信息
    psutil模块获取进程信息方面也提供了很好的支持，包括使用psutil.pids()获取所有进程的pid，使用psutil.Process()方法获取单个进程的名称、路径、状态、系统资源利用率等信息，实例如下：
    psutil.Process(PID_number).name()  获取指定进程id的进程名
    psutil.Process(PID_number).exe() 获取指定进程id的bin路径
    psutil.Process(PID_number).cwd() 获取指定进程id的工作目录绝对路径
    psutil.Process(PID_number).status() 获取指定进程id的状态
    psutil.Process(PID_number).create_time() 获取指定进程id的创建时间，时间戳格式
    psutil.Process(PID_number).uids() 获取指定进程id的uid信息
    psutil.Process(PID_number).gids() 获取指定进程id的gid信息
    psutil.Process(PID_number).cpu_times() 获取指定进程id的CPU时间信息
    psutil.Process(PID_number).memory_percent() 获取指定进程id的内存利用率
    psutil.Process(PID_number).num_threads() 获取指定进程id的开启线程数

    (2) popen类的使用
    获取用户启动的应用程序进程信息，跟踪程序进程运行状态，实例如下：
    import psutil
    from subprocess import PIPE
    p=psutil.Popen{("/usr/bin/python","-c","print('hello')"),stdout=PIPE}
    p.name()
    p.username()
    p.commuicate()
    p.cpu_times()

### 1.2 实用的IP地址模块ipy

    ipy模块高效完成IP的规划工作
    安装步骤如下：
    1. wget https://pypi.python.org/packages/source/I/IPy/IPy-0.81.tar.gz --no-check-certificate
    2. tar zxvf IPy-0.81.tar.gz
    3. cd IPy-0.81
    4. python setup.py install

#### 1.2.1 IP地址、网段的基本处理

    通过version方法区分IPv4与IPv6：
    from IPy import IP
    IP('10.0.0.0/8').version()      4代表IPv4
    IP('::1').version()           6代表IPv6
    通过指定网段输出该网段的IP个数及所有IP地址清单，代码如下：
    from IPy import IP
    ip=IP('192.168.0.0/16')
    print ip.len()    输出网段192.168.0.0/16的IP个数
    for x in ip:      输出网段所有IP清单
        print (x)
    ip.reverseNames()   反向解析地址格式
    ip.iptype         地址类型判断（私网还是公网）

#### 1.2.2 多网络计算方法详解

    比较两个网段是否存在包含、重叠等关系，IPy支持类似于数值型数据的比较，以帮助IP对象进行比较，如：
    IP('10.0.0.0/24') < IP('12.0.0.0/24')
    '192.168.1.100' in IP('192.168.1.0/24')
    IP('192.168.1.0/24') in IP('192.168.0.0/16')
    判断两个网段是否存在重叠，采用IPy提供的overlaps方法，如：
    IP('192.168.0.0/23').overlaps('192.168.1.0/24')    返回1表示存在重叠，返回0表示不存在重叠
### 1.3 DNS处理模块dnspython

    dnspython是实现DNS工具包，可以用于查询、传输并动态更新zone信息，同时支持事务签名验证信息和拓展DNS，在系统管理方面，我们可以利用其查询功能，来实现DNS服务监控以及解析结果的校验，可以代替nslookup及dig工具，轻松做到与现有平台的整合，安装步骤如下：
    1. wget  http://www.dnspython.org/kits/1.12.0/dnspython-1.12.0.tar.gz 
    2.tar -zxvf dnspython-1.12.0.tar.gz
    3. cd dnspython-1.12.0
    4. python setup.py install
#### 1.3.1 模块域名解析方法详解

    dnspython提供了一个DNS域名解析类resolver，使用它的query方法来实现域名的查询功能，query方法的定义如下：
    query(self,qname,rdtype=1,rdclass=1,tcp=False,source=None,raise_on_no_answer=True,source_port=0)
    其中，qname参数为查询的域名，rdtype参数用来指定DR资源的类型，常用的有以下几种：
    A记录：将主机名转换为IP地址
    MX记录：邮件交换记录，定义邮件服务器的域名
    CNAME记录：指定别名记录，实现域名间的映射
    NS记录：标记区域的域名服务器及授权子域
    PTR记录：反向解析，将IP地址转换为主机名
    SOA记录：一个起始授权区的定义

#### 1.3.2 常见解析类型示例说明

    (1) A记录
    实现A记录查询方法源码
    #!/usr/bin/env python
    import dns.resolver
    domain=raw_input('please input an domain:')
    A = dns.resolver.query(domain,'A')   指定查询类型为A记录
    for i in A.response.answer:            通过response.answer方法获取查询回应信息
        for j in i.items:           遍历响应信息
            print(j)
    (2) MX记录
    实现MX记录查询方法源码
    #!/usr/bin/env python
    import dns.resolver
    domain=raw_input('please input an domain:')
    MX = dns.resolver.query(domain,'MX')
    for i in MX:
        print'MX preference = ', i.preference,'mail exchange = ', i.exchange
    (3) NS记录
    实现NS记录查询方法源码
    #!/usr/bin/env python
    import dns.resolver
    domain=raw_input('please input an domain:')
    NS = dns.resolver.query(domain,'NS')
    for i in NS.response.answer:            
        for j in i.items:   
            print(j)
    (4)CNAME记录
    实现CNAME记录查询方法源码
    #!/usr/bin/env python
    import dns.resolver
    domain=raw_input('please input an domain:')
    cname = dns.resolver.query(domain,'CNAME')
    for i in cname.response.answer:            
        for j in i.items:   
            print(j)
#### 1.3.3 实践：DNS域名轮询业务监控

    大部分DNS解析都是一个域名对应多个IP，本实例通过分析当前域名的解析IP，再结合服务器端口探测来实现自动监控，在域名解析中添加、删除IP时，无须对监控脚本进行更改，实现如下：
    #!/usr/bin/env python
    #_*_coding:utf-8 _*_
    #__author__:Davidlua

    import dns.resolver
    import os
    import httplib

    iplist = []  #定义域名IP列表变量
    appdomain = "www.baidu.com"   #定义目标域名

    def get_iplist(domain=""):
        """域名解析函数，解析成功IP追加到iplist"""
        try:
            A = dns.resolver.query(domain,'A')  #解析A记录
        except Exception,e:
            print "dns resolver error:" +str(e)
            return
        for i in A.response.answer:   #使用responese.answer方法
            for j in i.items:
                iplist.append(j)   #追加到iplist
        return True

    def checkip(ip):
        oip = ('%s') % ip   #将解析的Ip转为字符串格式，以便跟:80端口合并
        checkurl = oip+":80"
        getcontent = ""
        httplib.socket.setdefaulttimeout(5)   #定义http链接超时时间
        conn=httplib.HTTPConnection(checkurl)  #创建http链接对象

        try:
            conn.request('GET',"/",headers={"Host":appdomain})  #发起url请求，添加host主机
            r = conn.getresponse()
            getcontent = r.read(15)  #只获取url页面的15个字符，用来做可用性校验
        finally:
            if getcontent == "<!DOCTYPE html>":  #监控url页面的类型要先查清楚，在做对比，这里<!DOCTYPE html>要大写,也可以对比http状态码
                print oip+" [ok]"
            else:
                print oip+" [error]"     #这里可以放置告警程序，比如发短信，邮件等

    if __name__ == "__main__":
        if get_iplist(appdomain) and len(iplist) > 0:   #域名解析正确，且不少于1个IP
            for ip in iplist:
            checkip(ip)
        else:
            print "dns resolver error."
## 2. 业务监控详解

    本章涉及文件与目录差异对比方法、http质量监控、邮件告警等内容。
### 2.1 文件内容差异对比方法
    
    通过介绍difflib模块实现差异对比
#### 2.1.1 示例1：两个字符串的差异对比

    本实例对比两个字符串的差异，然后以版本控制风格进行输出：
    import difflib
    text1='123'
    text2='1234'
    text1_lines=text1.splitlines()
    text2_lines=text2.splitlines()
    d =difflib.Differ()
    diff = d.compare(text1_lines,text2_lines)
    print '\n'.join(list(diff))
### 2.2 发送电子邮件模块smtplib

    本章通过模拟一个smtpkk客户端，通过与smtp服务器交互来实现邮件发送的功能
#### 2.2.1 smtplib模块常用类与方法

    SMTP定义类：smtplib.SMTP([host[,port[,local_hostname[,timeout]]]),作为SMTP的构造函数，功能是与smtp服务器创建连接，在连接创建成功后，就可以向服务器发送请求，SMTP类具有如下方法：
    1. SMTP.connect([host[,port]])：连接远程smtp主机，host为远程主机地址，port为远程主机smtp端口，默认25，也可以直接以host:port形式来表示，例如：
    SMTP.connect("smtp.163.com","25")
    2. SMTP.login(user,password):远程smtp主机校验方法，参数为用户名和密码，例如：
    SMTP.login("user","1234556")
    3. SMTP.sendmail(from_addr,to_addr,msg[,mail_options,rcpt_options]):实现邮件发送功能，参数依次为发件人、收件人、邮件内容
    4. SMTP.startls([keyfile[,certfile]]):启用TLS模式，所有smtp指令都将加密传输
    5. SMTP.quit():断开smtp服务器的连接
    实例：使用gmail向QQ邮箱发送测试邮件
    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
    import smtplib

    Server = "smtp.163.com" # 163邮箱的SMTP服务器地址
    Subject = "Test email from Python"  # 邮件主题
    To = "1058161124@qq.com" # 收件人
    From = "zhongqi217@163.com" # 发件人
    Text = "This is the email send by xpleaf, from xpleaf@163.com!" # 邮件内容
    Body = '\r\n'.join(("From: %s" % From,
                    "To: %s" % To,
                    "Subject: %s" % Subject,
                    "",
                    Text))


    s = smtplib.SMTP()  # 实例化一个SMTP类
    s.connect(Server, '25') # 连接SMTP服务器
    s.starttls()    # 开启TLS（安全传输）模式
    s.login('zhongqi217@163.com', '*****')   # 登陆到163邮件服务器
    s.sendmail(From, [To], Body)    # 发送邮件
    s.quit()    # 退出
    [所有邮件格式总结](https://www.cnblogs.com/zhangxinqi/p/9113859.html)
### 2.3 探测web服务质量方法

    本章介绍pycurl实现探测web服务质量的情况，比如响应的HTTP状态码、请求延时、HTTP头信息、下载速度等，利用这些信息可以定位服务响应慢的具体环节
#### 2.3.1 模块常用方法

    pycurl.Curl()类实现创建一个libcurl包的Curl句柄对象，无参数。下面介绍Curl对象几个常用的方法。
    close()：对应libcurl 包中的curl_easy_cleanup方法，实现关闭、回收Curl对象。
    perform():对应libcurl 包中的curl_easy_perform方法，实现Curl对象请求的提交
    setopt(option,value):对应libcurl 包中的curl_easy_setopt方法，为一个CURL会话设置选项
    getinfo(option):对应libcurl 包中的curl_easy_getinfo方法
#### 2.3.2 实践：实现探测web服务质量

    #!/usr/bin/python
    # -*- coding:UTF-8 -*-
    import os, sys
    import time
    import pycurl

    #探测的目标URL
    URL= "http://www.baidu.com"
    #创建一个Curl对象
    c = pycurl.Curl()

    #定义请求的URL常量
    c.setopt(pycurl.URL, URL)
    #定义请求连接的等待时间
    c.setopt(pycurl.CONNECTTIMEOUT, 5)
    #定义请求超时时间
    c.setopt(pycurl.TIMEOUT, 5)
    #屏蔽下载进度条
    c.setopt(pycurl.NOPROGRESS, 1)
    #完成交互后强制断开连接，不重用
    c.setopt(pycurl.FORBID_REUSE, 1)
    #指定HTTP重定向的最大数为1
    c.setopt(pycurl.MAXREDIRS, 1)
    #设置保存DNS信息的时间为30秒
    c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)
    #创建一个文件对象，以“wb”方式打开，用来存储返回的http头部及页面内容
    indexfile = open(os.path.dirname(os.path.realpath(__file__)) + "/content.txt", "wb")
    #将返回的HTTP HEADER定向到indexfile文件
    c.setopt(pycurl.WRITEHEADER, indexfile)
    #将返回的HTML内容定向到indexfile文件对象
    c.setopt(pycurl.WRITEDATA, indexfile)
    try:
        #提交请求
        c.perform()
    except Exception, e:
        print "connection error: " + str(e)
        indexfile.close()
        c.close()
        sys.exit()
    
    #获取DNS解析时间
    NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
    #获取建立连接时间
    CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
    #获取从建立连接到准备传输所消耗的时间
    PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
    #获取从建立连接到传输开始消耗的时间
    STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
    #获取传输的总时间
    TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
    #获取HTTP状态码
    HTTP_CODE = c.getinfo(c.HTTP_CODE)
    #获取下载数据包大小
    SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
    #获取HTTP头部大小
    HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
    #获取平均下载速度
    SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)
    #打印输出相关数据
    print "HTTP状态码： %d" % (HTTP_CODE)
    print "DNS解析时间: %.2f ms" % (NAMELOOKUP_TIME * 1000)
    print "建立连接时间： %.2f ms" % (CONNECT_TIME * 1000)
    print "准备传输时间： %.2f ms" % (PRETRANSFER_TIME * 1000)
    print "传输开始时间: %.2f ms" % (STARTTRANSFER_TIME * 1000)
    print "传输结束总时间： %.2f ms" %(TOTAL_TIME * 1000)
    print "下载数据包大小： %d bytes/s" %(SIZE_DOWNLOAD)
    print "HTTP头部大小： %d byte" %(HEADER_SIZE)
    print "平均下载速度： %d bytes/s" %(SPEED_DOWNLOAD)
    #关闭文件及Curl对象
    indexfile.close()
    c.close()
## 3. 定制业务质量报表详解

    本章介绍使用execl模块、rrdtool数据报表、scapy包处理等对数据进行处理
### 3.1 数据表之execl操作模块

    本节主要讲述利用python操作execl的模块XlsxWriter,安装步骤如下：
    wget https://files.pythonhosted.org/packages/04/c9/d5a8b02561a32bfcbec767a7d094c1ce54874eba9bc6bbaa58dd9ad523e7/XlsxWriter-1.0.4.tar.gz
    tar zxf XlsxWriter-1.0.4.tar.gz 
    cd XlsxWriter-1.0.4
    python setup.py install

    下面通过一个简单的功能演示示例，实现插入文字、数字、图片、单元格式等，代码如下：
    import xlsxwriter
    #创建一个Excel文件
    workbook = xlsxwriter.Workbook('demo1.xlsx')
    #创建一个工作表对象
    worksheet = workbook.add_worksheet()
    #设定第一列（A）宽度为20像素
    worksheet.set_column('A:A', 20)
    #定义一个加粗的格式对象
    #bold = workbook.add_format({'bold': True})
    bold = workbook.add_format()
    bold.set_bold()
    # WA1单元格写入'Hello'
    worksheet.write('A1', 'Hello')
    # A2单元格写入'World'并引用加粗格式对 象bold
    worksheet.write('A2', 'World', bold)
    # B2单元格写入中文并引用加粗格式对象
    worksheet.write('B2', u'中文测试', bold)
    # 用行列表示法写入数字'32'与'35.5'
    worksheet.write(2, 0, 32)
    # 行列表示法的单元格下标以0作为起始值，'3，0'等价 于'A3'
    worksheet.write(3, 0, 35.5)
    # 求A3：A4的和，并将结果写入'4，0'， 即'A5'
    worksheet.write(4, 0, '=SUM(A3:A4)')
    # 在B5单元格插入图片
    worksheet.insert_image('B5', 'img/python-logo.png')
    #关闭Excel文件
    workbook.close()
 #### 3.1.1 模块常用方法说明

    1. workbook类
    Workbook(filename[,options]),该类在磁盘上创建整个电子表格文件
    add_worksheet([sheetname])方法：添加一个新的工作表，参数sheetname为可选的工作表名称，默认为sheet1
    add_format([properties])方法：创建一个新的格式对象来格式化单元格，参数为指定一个格式属性的字典，例如设置一个加粗的格式对象，workbook.add_format({'bold':true})
    add_chart(options)方法：作用在工作表中创建一个图表对象，内部是通过insert_chart()方法来实现，参数options为图表指定一个字典属性，例如设置一个线条类型的图表对象，代码为chart=workbook.add_chart({'type:'line})
    close()方法：作用关闭工作表文件，如workbook.close()
    2. worksheet类
    worksheet类代表了一个工作表，调用add_worksheet()方法来创建，常用方法如下：
    write(row,col,*.args)方法：写普通数据到工作表的单元格，row为行，col为列，坐标索引值起始值为0，write方法已经作为其他更加具体数据类型方法的别名，包括：
        write_string()写入字符串类型数据，如：
            write_string(0,0,'hello')
        write_number()写入数字类型数据
        write_blank()写入空类型数据
        write_formula()写入公式类型数据
        write_datetime()写入日期类型数据
        write_booleam()写入逻辑类型数据
        write_url()写入超连接类型数据
    set_row(row,height,cell_format,options)方法：设置单元格的属性，row指定行位置，height设置行高
    set_column(first_col,last_col,width,cell_format.options)方法：设置一列或多列单元格属性
    insert_image(row,col.image[,options])方法：作用是插入图片到指定单元格，options为可选参数，作用是指定图片的位置。
    3. chart类
    chart类实现在xlsxwrite模块中图表组件的基类，支持的图表类型包括面积、条形图、柱形图、折线图、饼图等，一个图表对象是通过workbook的add_chart方法创建，通过{type,'图表类型'}字典参数指定图表的类型，语句如下：
    chart=workbook.add_chart({type,'column'}) #创建一个column(柱形)图表
    更多图表类型说明：
    area   