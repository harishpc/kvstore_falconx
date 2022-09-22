import os
import argparse
import requests
import configparser


config = configparser.ConfigParser()

headers={
            "Content-Type": "application/json"
        }


def set(params):
    url="http://localhost:8080/subscribe/"+params.subs[1]
    payload={}
    result=requests.post(url,json=payload,headers=headers)
    data=result.json()
    print(data)


def main():
    usagemsg="usage: sub [-h] requires both key and value | ex sub {key}"
    my_parser = argparse.ArgumentParser(description='A Simple KV (key-value) store web service with a subscription feature. As a user, I should be able to perform set(key, val) and get(key)  operations over HTTP and also subscribe to changes happening to any of the keys.',usage=usagemsg)
    my_parser.add_argument('subs', action='store', nargs=2,type=str,help="it will subscribe a particular key for any updation will return the values")
    args = my_parser.parse_args()
    if args.subs:
        set(args)




if __name__ == "__main__":
    main()
