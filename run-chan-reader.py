#!/usr/bin/env python
# coding: utf8
import argparse
from telethon import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, LeaveChannelRequest
from telethon.tl.types import UpdateNewChannelMessage

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('-S', '--session-file', required=True, help='session file path (see telethon lib docs)')
parser.add_argument('-I', '--api-id', required=True, help='telegram API id')
parser.add_argument('-H', '--api-hash', required=True, help='telegram API hash')
parser.add_argument('-C', '--channel-name', help='channel to join ')
args = parser.parse_args()
if args.session_file.endswith('.session'):
    args.session = args.session_file[:-8]


tg = TelegramClient(args.session_file, args.api_id, args.api_hash, update_workers=0)
ok = tg.connect()
if not ok:
    raise SystemExit('Telegram connection error')
if not tg.is_user_authorized():
    raise SystemExit('You are not authorized')

if args.channel_name:
    print('* subscribing to channel %s' % args.channel_name)
    try:
        entity = tg.get_input_entity(args.channel_name)
        tg(JoinChannelRequest(entity))
    except Exception as ex:
        print('* Subscription error: %s' % ex)

while True:
    try:
        print('waitng chats messages...')
        update = tg.updates.poll()
        if not update:
            continue
        if type(update) == UpdateNewChannelMessage:
            msg = update.message
            print('\n* Incoming Chat Message *')
            print('Text:', msg.message)
    except KeyboardInterrupt:
        break
tg.disconnect()




