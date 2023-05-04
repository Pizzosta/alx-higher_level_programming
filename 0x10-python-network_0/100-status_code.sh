#!/bin/bash
# a Bash script that sends a request to a URL and displays only the status code of the response
curl -s "$1" -o /dev/null -w "%{http_code}"
