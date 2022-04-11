import string
import itertools
import time
import zipfile

path = ""
file_path = path + ''

size = 5
start = time.time()


def BruteForce(chars):
    count = 0
    for ch in itertools.product(chars, repeat=size):
        password = bytes(''.join(ch), "UTF-8")
        with zipfile.ZipFile(file_path, 'r') as zf:
            print("tried :{}".format(count) + "回目")
            try:
                zf.extractall(path=path, pwd=password)
                print('success : password  : {}'.format(password))
                break
            except Exception as e:
                count += 1
    print("合計 :{}".format(time.time() - start) + "(s)")


if __name__ == "__main__":
    BruteForce(string.ascii_letters + string.digits)
