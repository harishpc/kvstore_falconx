import os
import argparse
import requests
import configparser


config = configparser.ConfigParser()

url="http://localhost:8080/key/insert"
headers={
            "Content-Type": "application/json"
        }


def set(params):
    try:
        payload = {"key":params.put[1],"value":params.put[2]}
        result=requests.put(url,json=payload,headers=headers)
        data=result.json()
        print(data)
    except Exception as e:
        print("OOPS Error occured")


def main():
    usagemsg="usage: set [-h] requires both key and value | ex set {key} {value}"
    my_parser = argparse.ArgumentParser(description='A Simple KV (key-value) store web service with a subscription feature. As a user, I should be able to perform set(key, val) and get(key)  operations over HTTP and also subscribe to changes happening to any of the keys.',usage=usagemsg)
    my_parser.add_argument('put', action='store', nargs=3,type=str)
    args = my_parser.parse_args()
    if args.put:
        set(args)




if __name__ == "__main__":
    main()
