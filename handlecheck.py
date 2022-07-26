#!/usr/bin/python3

##
## handlecheck.py
##
# If you found this script useful, please consider a small ADA donation to:
# $phrankerco
# -or-
# addr1q9k2aqqyyru0y3p6d2h7ggdw7f99v5tsf5teuk8dcqrge4vjp62n3v953kqykl8zgh5ctamrwvu2380z4ndh6zch4l3s2jvf2v


import koios_python
import json
import requests
import binascii

# Policy ID for all Handles
POLICYID = "f0ff48bbb7bbe9d59a40f1ce90e9e9d0ff5002ec48f232b49ca0fb9a"

# Get user input of range to check
print("adahandle - digit check\nIf a handle is still available to mint, the integer will be displayed. If the integer is not display, it has already been minted.\nTo check a single digit, enter it in both start and end.\n")
startrange = input("Enter start of range: ")
endrange = input("Enter end of range: ")

# Make sure user entered proper range
if int(endrange) < int(startrange):
        print("Error: start must be less than end!")
        quit()


# Loop thru range, convert to hex, check using Koios
for x in range(int(startrange), int(endrange)+1):
        asset = str(x)
        b = bytes(asset, "utf-8")
        y = binascii.hexlify(b)
        hexasset = str(y, "ascii")
        res = koios_python.get_asset_address_list(POLICYID, hexasset)
        # if handle has been minted, it will return address holding handle, so if result set is empty then it has not beem minted
        if not res:
                print(asset)

