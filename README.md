sublime-ascii
=============

## 简介
用来在sublime中生成如下形式的文字.
<pre>
######## ##     ##    ###    ##     ## ########  ##       ######## 
##        ##   ##    ## ##   ###   ### ##     ## ##       ##       
##         ## ##    ##   ##  #### #### ##     ## ##       ##       
######      ###    ##     ## ## ### ## ########  ##       ######   
##         ## ##   ######### ##     ## ##        ##       ##       
##        ##   ##  ##     ## ##     ## ##        ##       ##       
######## ##     ## ##     ## ##     ## ##        ######## ######## 
</pre>

也就是项目 [https://github.com/muyr/pyqt_ascii](https://github.com/muyr/pyqt_ascii) 的sublime插件版

## 安装
将Ascii文件夹放置于sublime的Packages文件夹下，比如
`C:\Users\muyanru\AppData\Roaming\Sublime Text 2\Packages`

（可通过sublime执行菜单 Preferences -> Browse Packages...跳转到目录）


然后修改User文件夹下 `Default (Windows).sublime-keymap` 文件。
添加如下内容

<pre>
{ "keys": ["ctrl+shift+3"], "command": "asciishap"},
{ "keys": ["ctrl+shift+/"], "command": "asciislash"}
</pre>
保存退出

注意要是保存报错，请在上一行的末尾加上个半角逗号","，如下所示：
<pre>
[
...
{ "keys": ["ctrl+shift+x"], "command": "maya" },
{ "keys": ["ctrl+shift+3"], "command": "asciishap"},
{ "keys": ["ctrl+shift+/"], "command": "asciislash"}
]
</pre>

## 使用
选中的内容为目标，若没有任何内容被选中，则光标所在的单词为目标
### 快捷键方式
 * 按下快捷键 `ctrl+shift+3`（非数字键盘上的3，是跟#共用的那个3键）
即可目标变为以“#”作为填充字符的形式
 * 按下快捷键 `ctrl+shift+/`，即可将目标变为以“/”作为填充字符的形式

### 命令行方式
请执行菜单 View -> Show Console
或者快捷键 ctrl + ` 调出python命令行，

输入
<pre>
view.run_command('asciisharp')
</pre>
回车运行即可，相当于快捷键 `ctrl+shift+3`

输入
<pre>
view.run_command('asciislash')
</pre>
回车运行即可，相当于快捷键 `ctrl+shift+/`

### 高级方式
输入
<pre>
view.run_command('ascii', {'f':'@', 'e':'.'})
</pre>

参数说明：

 * f：（可选，默认为“#”）用来填充的字符，只能是1个字符，如果超出一个或者字符不符合要求，则采取默认字符
 * e：（可选，默认为“ ”空格）用来作为空白位置的字符，只能是1个字符，如果超出一个或者字符不符合要求，则采取默认字符




