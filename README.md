# invoiceOCR_for_fun

一个对中国增值税发票的信息提取软件
main.py通过划定识别区域调用CloudEnv API进行文字提取实现
alternative.py对整张图片进行识别再匹配信息

## 二次开发：
可以增加更多划定区域和提取信息的类别


## 短板：
main.py：
1.必须是扫描件的图片输入，图片大小需比较统一
2.软件运行时必须联网
alternative.py
1.因为当前版本没分割发票区域，不好区分购买方和销售方信息
## 优点：
1.简单易用，识别准确率高
alternative.py：
1.不需要比较统一的图片输入

## 用法：
1. 将发票图片或 PDF 文件放置在该项目的根目录中
2. 注册一个 CloudEnv 账户，并将 CloudEnv API 密钥放入文件 .env 中
3. 根据两种代码的优缺点选择运行 main.py或者alternative.py


