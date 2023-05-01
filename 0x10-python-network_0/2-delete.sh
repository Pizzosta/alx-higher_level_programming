#!/bin/bash
# a Bash script that sends a deletes request to a URL and displays the body of the response
curl -sL "$1" -X DELETE
