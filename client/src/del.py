import os
import requests
import argparse

headers={"Content-Type": "application/json"}

def remove(params):
    url="http://localhost:8080/key/"+params.rem[1]
    result=requests.delete(url)
    print(result.json())

def main():
    usagemsg="usage: del [-h] requires key | ex del {key}"
    my_parser = argparse.ArgumentParser(description='A Simple KV (key-value) store web service with a subscription feature. As a user, I should be able to perform set(key, val) and get(key)  operations over HTTP and also subscribe to changes happening to any of the keys.',usage=usagemsg)
    my_parser.add_argument('rem', action='store', nargs=2,type=str)
    args = my_parser.parse_args()
    if args.rem:
        remove(args)







if __name__ == "__main__":
    main()
