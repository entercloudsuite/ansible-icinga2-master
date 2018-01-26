#!/usr/bin/env python

import argparse
import telepot
from pprint import pprint

def parse_args():
    parser = argparse.ArgumentParser(description='Nagios notification via Telegram')
    parser.add_argument('-t', '--token', nargs='?', required=True)
    parser.add_argument('-o', '--object_type', nargs='?', required=True)
    parser.add_argument('--contact', nargs='?', required=True)
    parser.add_argument('--notificationtype', nargs='?')
    parser.add_argument('--hoststate', nargs='?')
    parser.add_argument('--hostname', nargs='?')
    parser.add_argument('--hostaddress', nargs='?')
    parser.add_argument('--servicename', nargs='?')
    parser.add_argument('--servicestate', nargs='?')
    parser.add_argument('--servicedesc', nargs='?')
    parser.add_argument('--datetime', nargs='?')
    parser.add_argument('--output', nargs='?')
    parser.add_argument('--customer', nargs='?')
    parser.add_argument('--notification_author', nargs='?')
    parser.add_argument('--notification_comment', nargs='?')
    args = parser.parse_args()
    return args

def send_notification(token, user_id, message):
    bot = telepot.Bot(token)
    bot.sendMessage(user_id, message, parse_mode="html")


def host_notification(args):
    state = ''
    if args.hoststate == 'UP':
        state = u'\U00002705 ' + "UP\n"
    elif args.hoststate == 'DOWN':
        state = u'\U0001F525 ' + "DOWN\n"
    elif args.hoststate == 'UNREACHABLE':
        state = u'\U00002753 ' + "UNREACHABLE\n"

    return "<b>HOST " + u'\U0001F4BB' + " - %s</b>\n <pre>%s%s: %s</pre>\n %s %s" % (
        args.customer,
        state,
        args.hostname,
        args.output,
        args.notification_author,
        args.notification_comment,
    )


def service_notification(args):
    state = ''
    if args.servicestate == 'OK':
        state = u'\U00002705 ' + "OK\n"
    elif args.servicestate == 'WARNING':
        state = u'\U000026A0 ' + "WARNING\n"
    elif args.servicestate == 'CRITICAL':
        state = u'\U0001F525 ' + "CRITICAL\n"
    elif args.servicestate == 'UNKNOWN':
        state = u'\U00002753 ' + "UNKNOWN\n"

    return "<b> SERVICE " + u'\U0001F310' +  " - [ %s %s]</b>\n <pre>%s - %s: %s</pre>\n %s %s" % (
        args.customer,
        state,
        args.hostname,
        args.servicedesc,
        args.output,
        args.notification_author,
        args.notification_comment,
    )


def main():
    args = parse_args()
    user_id = int(args.contact)
    if args.object_type == 'host':
        message = host_notification(args)
    elif args.object_type == 'service':
        message = service_notification(args)
    send_notification(args.token, user_id, message)

if __name__ == '__main__':
    main()