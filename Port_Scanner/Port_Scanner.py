import optparse
import socket
import threading

screenLock = threading.Semaphore(value=1)
def connScan(tarHost,tarPort):
    try:
        conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        conn.connect((tarHost,tarPort))
        conn.send('123\r\n'.encode('ascii'))
        result = conn.recv(100)
        screenLock.acquire()
        print('[*]%d/tcp open' % tarPort)
        print('[*]' + str(result))
    except:
        screenLock.acquire()
        print('[*]%d/tcp cloed' % tarPort)
    finally:
        screenLock.release()
        conn.close()



def portScan(tarHost,tarPorts):
    try:
        tarIP = socket.gethostbyname(tarHost)
    except:
        print("[*]Cannot resolve '%s':Unkown host" % tarHost)
        return
    try:
        tarName = socket.gethostbyaddr(tarIP)
        print('\n[*]Scan Results for:' + tarName[0])
    except:
        print('\n[*]Scan Result for:' + tarIP)
    socket.setdefaulttimeout(1)
    for tarPort in tarPorts:
        print('Scanning port:' + str(tarPort))
        t = threading.Thread(target = connScan,args=(tarHost,int(tarPort)))
        t.start()

def main():
    parse = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parse.add_option('-H',dest='tarHost',type='string',help='specify target host')
    parse.add_option('-P', dest='tarPost', type='int', help='specify target post')
    (options,args) = parse.parse_args()
    tarHost = options.tarHost
    tarPost = options.tarPost
    args.append(tarPost)
    if((tarHost == None)|(tarPost == None)):
        print('[*]You must specify a target host and post! -H xxx.xxx.xxx.xxx -P xxxx')
        exit(0)
    portScan(tarHost,args)


if __name__ == '__main__':
    main()