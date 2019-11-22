# Ethernet-Ip-address-logger-of-linux
The application will update the information of the interface Ip-Address of a machine, whether it is a raspberry, linux pc etc, to a google sheet.

If you are using multiple linux pc through ssh and Ip Address changes each time, this can help you.

The application is based on [google sheet api ](https://github.com/burnash/gspread).
Follow the link how to create a JSON file for your requriement.

## Installataion

```sh
sudo pip3 install --upgrade oauth2client
sudo pip3 install gspread
sudo pip3 install netifaces
```
Requirements: Python 3+.

## Basic Usage

```sh
python3 systemTracker.py -n <HostName/Alias> -i <Interface> -f <google credential json file location> -s <google sheet name> [-t <Update time in minutes, default 10>]
```

## Example

```sh
python3 systemTracker.py -n MyTestUbuntu -i wlan0 -f client.json -s testSheet
python3 systemTracker.py -n Raspberry1 -i meth0 -i wlan0 -i eth0 -f ../client.json -s IpSheet -t 5
```

## Sample image for google sheet
![Alt text](/sheetImage.png?raw=true "App selection")
