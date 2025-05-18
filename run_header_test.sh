#!/bin/bash
read -p "Enter your CDN domain (e.g., source.rachel.onl.ac): " domain
read -p "Enter header delay in seconds (e.g., 30): " delay
python3 test_header_delay.py $domain --delay $delay