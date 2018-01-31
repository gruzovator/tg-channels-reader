#!/usr/bin/env python
# coding: utf8
""" Script to register (and to make new telegram session file)"""
import argparse

from telethon import TelegramClient

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('-P', '--phone', help='phone number to sign in')
parser.add_argument('-I', '--api-id', type=int, help='tg api id')
parser.add_argument('-H', '--api-hash', help='tg api hash')
parser.add_argument('-F', '--session-file', help='session filename (.session extension will be added)')
args = parser.parse_args()

while not args.phone:
    args.phone = input('Your phone number: ')
while not args.api_id:
    args.api_id = input('API ID: ')
while not args.api_hash:
    args.api_hash = input('API HASH: ')
while not args.session_file:
    args.session_file = input('Session file path to generate: ')

client = TelegramClient(args.session_file, args.api_id, args.api_hash)
ok = client.connect()
if not ok:
    raise SystemExit('Telegram connection error')
client.send_code_request(args.phone)
client.sign_in(args.phone, input('Enter the code sent to your mobile phone: '))
print('done')
