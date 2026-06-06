import requests
import json
import sys
import re

print("Downloading APK...")
# We need an arm64 v8a APK for com.facebook.orca version 564.0.0.42.89.
# The user log says "[+] Downloading 'Messenger' from 'uptodown'"
# It's hard to scrape uptodown via python quickly. Let's see if we can find the manifest another way or just download via apkeep?
