#日常使用脚本
参考了诸多前辈的代码，在源文件里都做了说明，在此对所有无私分享代码的前辈们一并表示感谢！

所有脚本都基于linux下的kde环境，欢迎大家使用、交流。

[ocrtran-git]: https://github.com/innerseacn/scripts/blob/master/ocrtran-git.py
[byzanz-record-kde]: https://github.com/innerseacn/scripts/blob/master/byzanz-record-kde
[gif]: https://github.com/innerseacn/accessories/blob/master/GIFrecord_2018-08-24_155834.gif

##ocrtran-git.py
一个实时截词并翻译的python脚本，用于看扫描版pdf电子书。(;¬_¬) 

借助命令行工具借取屏幕单词或短语，使用百度api进行识别，并通过百度翻译转换成中文，最后使用kdialog在桌面上显示气泡通知。

PS: 本来应该使用notify-send发送气泡通知，这样通用性好一些。不过在我的电脑上怎么也不成功，所以就用kdialog解决了。

╮（￣▽￣）╭

![gif][]

##byzanz-record-kde
一个录制屏幕gif的bash脚本。