#!/bin/bash
# a Bash script displays the size of a URL in bytes
curl -sSL "$1" | wc -c

