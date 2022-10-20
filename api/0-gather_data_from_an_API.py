#!/usr/bin/python3

from urllib import response
import requests
import sys

if __name__=="__main__":
    response = requests.get(sys.argv[1])
    if(response.status_code > 400):{
        print("Error code: {}".format(response.status_code))
    }
    else:
        print("Employee {response.content.EMPLOYEE_NAME} is done with tasks({response.content.NUMBER_OF_DONE_TASKS}/{response.content.TOTAL_NUMBER_OF_TASKS}):")