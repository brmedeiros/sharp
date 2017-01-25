#!/usr/bin/python3

import discord
import asyncio
import datetime as dt

import sharp_login_info as info
import auxiliar_functions as auxf

def main():

    client = discord.Client()

    @client.async_event # equivalent to @client.event \n @asyncio.courotine
    def on_ready():
        '''this function represents the event 'being ready'...'''
        print('s.h.a.r.p. v.0.1\n------\nLogged in as {0}, id: {1}'.format(client.user, client.user.id))
        auxf.sp_print('Server(s) joined:')
        for server in client.servers:
            auxf.sp_print('{0}'.format(server))
        print('\n------')

    @client.async_event
    def on_message(message):
        '''this function represents a 'message event' in any of the channels...'''
        if message.author == client.user:
            print('{:%d/%m/%y %H:%M} @{} {}: {}'
                  .format(dt.datetime.now(), message.channel, message.author.name, message.content))
        
        if message.content.startswith('#'):
            print('{:%d/%m/%y %H:%M} @{} user: {}'
                  .format(dt.datetime.now(), message.channel, message.content))

            yield from client.send_message(message.channel, 'Hello! I\'m s.h.a.r.p.')

    client.run(info.token)

if __name__ == '__main__':
    main()
