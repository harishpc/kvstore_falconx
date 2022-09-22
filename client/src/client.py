import os
import argparse



def msg(name=None):
    return '''[get [key]] [set [key] [value]] [del [key]]
        '''


def main():
    my_parser = argparse.ArgumentParser(description='A Simple KV (key-value) store web service with a subscription feature. As a user, I should be able to perform set(key, val) and get(key)  operations over HTTP and also subscribe to changes happening to any of the keys.',usage=msg())
    my_parser.add_argument('get', action='store', nargs=2,type=str,help="Given a key it fetches the value")
    my_parser.add_argument('getall', action='store', nargs=2,type=str,help="Given a key it fetches the complete item in the KV-Store")
    my_parser.add_argument('set', action='store', nargs=3,type=str,help="Given a key value it will set the key value")
    my_parser.add_argument('del', action='store', nargs=2,type=str,help="Given a key it remove the key")
    my_parser.add_argument('put', action='store', nargs=2,type=str,help="Given a key it update and exisitng or will insert a new key|value")
    my_parser.add_argument('subs', action='store', nargs=2,type=str,help="Given a key set subscription on any key")
    my_parser.add_argument('suball', action='store', nargs=2,type=str,help="Given a key will show all the key which have subscription")
    my_parser.add_argument('-v', '--version', action='version',version='%(prog)s 1.0', help="Show program's version number.")
    args = my_parser.parse_args()
    parser.print_help()




if __name__ == "__main__":
    main()
