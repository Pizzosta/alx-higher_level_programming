#!/bin/bash
# a Bash script that takes in a URL as an argument and displays the body of the response
curl -sL "$1" -H "X-School-User-Id: 98"
