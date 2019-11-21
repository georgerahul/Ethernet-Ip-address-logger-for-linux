import sched
import time
import network
from googlesheet import GoogleSheet
from host import Host
import os.path
from os import path


def updateScheduler(hostname, interfaces, updateTime, filelocation, sheet_name):
    
    # check file exist or not.
    if path.exists(filelocation) == False :
        raise Exception(' File not found !!!: '+filelocation)
        return

    while True:
        #print('Updating Time')
        fetchAndUpdate(hostname, interfaces, filelocation,sheet_name)
        time.sleep(60*updateTime)


def fetchAndUpdate(hostname, interfaces, filelocation, sheet_name):
    sheet_conn = GoogleSheet(filelocation, sheet_name)

    try:
        sheet_conn.connect()
    except:
        # This can also happen if network is not up yet. So go for retry.
        # Google Sheet: Authorization Failed.
        return 

    try:
        sheet_conn.get_sheet1()
    except:
        # Google Sheet: Not found.s
        raise Exception("Google Sheet '"+ sheet_name + "' not available.")
    
    # Todo: change code to update all info in one-go. 
    # get all interface detailsa and update. Not one by one.
    for iface in interfaces:
        addr = network.get_ip_address(iface)
        sheet_conn.make_entry_in_gsheet([hostname, iface, addr],[0,1],4)
