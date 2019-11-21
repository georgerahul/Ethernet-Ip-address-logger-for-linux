#!/usr/bin/python

import getopt
import sys
import core

fileName = 'systemTracker.py'
tab = " " * 5
usageSyntax = fileName + \
    ' -n <HostName/Alias> -i <Interface> -f <google credential json location> -s <google sheet name> [-t <Update time in minutes, default 10>]'


def main(argv):
    interfaces = []
    hostName = ''
    json_file_location = ''
    sheet_name = ''
    updateTime = 10
    try:
        opts, args = getopt.getopt(
            argv, "hi:f:s:n:t:", ["help", "interface=", "file=", "sheet=", "name=", "time="])
    except getopt.GetoptError:
        print(tab+' Argument mismatch: '+usageSyntax)
        sys.exit()

    # print(opts)

    # In case no arguments are present.
    if(len(opts) == 0):
        print('No arguments found !!! \n'+tab + usageSyntax)
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(tab + fileName)
            print(tab+"----"*10)
            print(tab+fileName + ' is used to report the interface Ip-Address to google sheet.\n' +
                  tab+'If you are using multiple linux pc through ssh and Ip Address changes each time, this can help you.\n')
            print(tab+usageSyntax)
            print(tab+"Example : " + fileName +
                  ' -n MyTestUbuntu -i wlan0 -f client.json -s testSheet')
            print(tab+"Example : " + fileName +
                  ' -n RpiNavi -i meth0 -i wlan0 -i eth0 -f client.json -s financeSheet -t 5')
            print(tab+"----"*10)
            sys.exit()
        elif opt in ("-i", "--interface"):
            checkArgumentMismatchError(arg)
            interfaces.append(arg)
        elif opt in ("-f", "--file"):
            checkArgumentMismatchError(arg)
            json_file_location = arg
        elif opt in ("-n", "--name"):
            checkArgumentMismatchError(arg)
            hostName = arg
        elif opt in ("-t", "--time"):
            checkArgumentMismatchError(arg)
            updateTime = int(arg)
        elif opt in ("-s", "--sheet"):
            checkArgumentMismatchError(arg)
            sheet_name = arg

    if(json_file_location == '' or sheet_name =='' or hostName == '' or len(interfaces) == 0):
        print(tab + " All 4 arguments are required.")
        print(tab + tab + usageSyntax)
        sys.exit(0)

    try:
        core.updateScheduler(hostName, interfaces, updateTime,
                         json_file_location, sheet_name)
    except Exception as e:
        print (e)



def checkArgumentMismatchError(arg):
    if arg[0] == '-':
        print(tab+' Argument mismatch error: \n '+tab+tab + usageSyntax)
        print(tab+" Example : " + fileName +
                  ' -n RpiNavi -i meth0 -i wlan0 -i eth0 -f yet_To_fill.')
        sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
