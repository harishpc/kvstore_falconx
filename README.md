# KV (key-value) Service

# Problem Statement
The problem statement was to build a simple KV (key-value) store web service with a subscription feature. As a user, I should be able to perform set(key, val) and get(key)  operations over HTTP and also subscribe to changes happening to any of the key.

# Approach

The approach to solve the above problem was to use python flask framework to create a CRUD api which can store data in key value form in memory and similarly design a client in python which can fetch the values from the given api.

### language Used

* python
* shell

# Usage

* set {key} {value} : It will set key-value in {"key": {key} , "value": {value}}. set command only sets unique keys. If you try set an already present key it will return you a message : `{'message': 'set command can set unique key and values hari already exists'}`

* get {key} : It will fetches the value of the given key.

* del {key} : It will delete the {key} | {value} pair. Any {key} that has been subscribed and delete will also be removed from the subscription list if not updated.

* getall : It will return all the {key} {value} pair at any point of time in KV-Store memory.

* suball : It will return a list of all the key which has been subscribed. These key will response to any changes done via put.

* put {key} {value} : It's an update command. If there is no key in the memory in the KV-store it will add the {key}-{value} pair. If there is any {key} present it will update that. If any key is under subscription-list and get update via put command it will return a message : `{'message': 'subscription key hari has been updated', 'key': 'hari', 'oldvalue': 'pc', 'newvalue': 'haripc'}`

* subs {key} : It will set the key in subscription list any changes done to that {key} via put will response to changes.


# Prerequisite
[Docker](https://docs.docker.com/get-docker/) must be installed and running  
 To get an easy and quick installation of Docker use the following command
```
curl -L get.docker.com | sh
```
[Python](https://www.python.org/downloads/) must for running python application

[Pip](https://pip.pypa.io/en/stable/installing/) for downloading required packages

#### Directory Structure of Assignment

After Cloning the  directory this will look something like this :-

![directory Structure](https://github.com/harishpc/kvstore_falconx/blob/master/images/direct-structure.png)


- utility : It contains all the code for in memory saving key-value data
- client : It contains `bin` and `src` where the client bash script is in `bin` and the client code is in `src`
- The Root Directory contains the `Dockerfile` packed for running `kv-server`
- build.sh : It as interactive command-line to setup `kv-server` abd `kv-client`


# :rocket: Launch


### To get App up and running follow the server follow the following steps

#### 1. Clone the following Repo

```
git clone https://github.com/harishpc/kvstore_falconx.git

cd KV-Store
```

#### 2. The simplest way to get `kv-server` up and running is by running command

```
bash build.sh

```

which will give you an interactive menu to choose either to configure `kv-server` or `kv-client`

```
The following script will setup both the CLIENT and SERVER for you
 --------------------------------------------------------------------------------------------------------
 1 . To Setup Server
 2 . To Setup Client
Enter your choice :
```

#### 3. Choose `1` to `Setup Server` and it will start a docker container with application running on it.

Output will be like something :-

```
Sending build context to Docker daemon  922.1kB
Step 1/5 : FROM python:3.8
 ---> c0e1d3033786
Step 2/5 : COPY utility/requirements.txt .
 ---> Using cache
 ---> f1afaa82c662
Step 3/5 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> 3173130eb029
Step 4/5 : COPY  utility/code/ .
 ---> Using cache
 ---> 134e08747ce5
Step 5/5 : CMD [ "python", "app.py" ]
 ---> Using cache
 ---> 5f0eeeb22cf0
Successfully built 5f0eeeb22cf0
Successfully tagged kv-server:latest
e3d8eacc5ab61984e6931eac407708628bb32dc4fe5c38d6c10d3389b858dab3
```

#### 4. Run the same step again `build.sh` file to setup client this time

:warning: This second step need python to be configure in your machine. As it will find the default python and create virtualenv according to it.

```
The following script will setup both the CLIENT and SERVER for you
 --------------------------------------------------------------------------------------------------------
 1 . To Setup Server
 2 . To Setup Client
Enter your choice : 2
```

This will setup client for you.


#### 5. check help `-h` or `--help`

![help key](https://github.com/harishpc/kvstore_falconx/blob/master/images/help.png)



#### 6. Performing Operations

####  Setting a Key

* To Set a key you can set it the following way

![set key](https://github.com/harishpc/kvstore_falconx/blob/master/images/set.png)



####  Getting a Key

* To get a key you can set it the following way

![get key](https://github.com/harishpc/kvstore_falconx/blob/master/images/get.png)


####  Deleting a Key

* To delete a key you can set it the following way

![delete key](https://github.com/harishpc/kvstore_falconx/blob/master/images/del.png)


####  Get all the Key

* To get all a key at a given time

![get-all key](https://github.com/harishpc/kvstore_falconx/blob/master/images/getall.png)


#### Subscribe get for any changes

![sub key](https://github.com/harishpc/kvstore_falconx/blob/master/images/subs.png)

##### To check subscription on key at any given time you can `suball` to get all the key in subscription is set.



## :exclamation: ERROR

#### 7. IF there is an issue with setting up client. Try setting it up manual. Below are the steps to setup client manually. The above code has been tested in an fresh EC2 machine at region : ap-south-1 with ami-id : ( ami-00ddb0e5626798373 ) ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-20201026

```
pip install -r client/requirements.txt
cd client/bin/
bash kv-client.sh
```
