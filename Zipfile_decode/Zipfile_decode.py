import zipfile
import time

def decode_zip(zFile,password):
    try:
        zFile.extractall(pwd=password.encode('ascii'))

        print("[*]Found Password:",password)
        return password
    except:
        pass


def main():
    zFile = zipfile.ZipFile('***Your zip file***')
    passFile = open('***Your dic txt***','r')
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = decode_zip(zFile,password)
        if guess:
            print('[*]Password=',password)
            return
        else:
            print("[*]Can't find password!")
            return


if __name__ == '__main__':
    print('[*]Wait~  ^O^')
    time.sleep(3)
    main()
