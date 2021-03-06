##Tyler Sperle - 02/22/2022

import requests ## This imports the requests module
requests.packages.urllib3.disable_warnings() ## This disables the unsecure request warning
import json ## This imports the json module

##Functions
def sendCLI(cmdCLI, IP): ## This is a function that sends a CLI command to a network device url, and returns a response

    switchuser='cisco' ## This supplies the devices username
    switchpassword='cisco' ## This supplies the devices password

    url='https://' + IP + '/ins' ## This is the device URL where "IP" is the devices management IP address

    myheaders={'content-type':'application/json-rpc'}
    payload=[ ## This is where the API will send the command to the device
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": cmdCLI, ## This is the command we are sending to the device, where "cmdCLI" is the exact command we passed to the function
          "version": 1
        },
        "id": 1
      }
    ]

    ## verify=False below is to accept untrusted certificate
    response = requests.post(url,data=json.dumps(payload), verify = False, headers=myheaders,auth=(switchuser,switchpassword)).json() ## This is our
                                                                                                                ##original response converted to json
    return response

##Main        
deviceInfo = sendCLI("show version", "10.10.20.177") ## This runs the sendCLI function with the cmd "show version" and mgmt IP "10.10.20.177"

print("\n\n\n" + "Hostname =", deviceInfo["result"]["body"]["host_name"] + "\t", "Memory =",
      deviceInfo["result"]["body"]["memory"], deviceInfo["result"]["body"]["mem_type"] + "\n\n\n") ## This prints the desired info from the deviceInfo dictionary



