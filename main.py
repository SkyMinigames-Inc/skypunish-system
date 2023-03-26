import discord
import asyncio
import random
import re
import time
import os

client = discord.Client()

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import secreto
    token = secreto.token()

msg_id = None
msg_user = None
msg_author = None

qntdd = int

def toint(s):
    try:
        return int(s)
    except ValueError:
        return float(s)
    
def times():
    import datetime
    now = datetime.datetime.now()
    qntdd = (now.strftime("%H"))
    qntdd = toint(qntdd)
    if qntdd == 0:
        return "{}:{}".format('22', now.strftime("%M"))
    if qntdd == 1:
        return "{}:{}".format('23', now.strftime("%M"))
    else:
        return "{}:{}".format(qntdd - 2, now.strftime("%M"))


chat_filter = ["PQP", "VSF", "VIADO", "VTNC", "TNC", "CU", "CÚ", "CARALHO", "BOSTA", "PUTA", "MERDA",
               "ARROMBADO", "KRL", "CRL", "FDP", "VSF", "FODE", "FODA-SE", "FODASE", "FODASSE", "FODACE", "FDS",
               "VADIA", "PORRA", "POHA", "FUDER", "FUDE", "PNC", "VAGABUNDO", "VAGABUNDA", "PUTO", "FODER",
               "DESGRAÇADO", "DESCRAÇA", "DESGRASSA", "DESGRASA", "FUDIDO", "VIADOS", "CACETE", "KCT", "VAGABUNDA",
               "PIROCA", "PIROKA", "PIROCÃO", "BUCETA", "BUCETUDA",

               "PQP*", "VSF*", "VIADO*", "VTNC*", "TNC*", "CU*", "CÚ*", "CARALHO*", "BOSTA*", "PUTA*", "MERDA*",
               "ARROMBADO*", "KRL*", "CRL*", "FDP*", "VSF*", "FODE*", "FODA-SE*", "FODASE*", "FODASSE*", "FODACE*",
               "FDS*",
               "VADIA*", "PORRA*", "POHA*", "FUDER*", "FUDE*", "PNC*", "VAGABUNDO*", "VAGABUNDA*", "PUTO*", "FODER*",
               "DESGRAÇADO*", "DESCRAÇA*", "DESGRASSA*", "DESGRASA*", "FUDIDO*", "VIADOS*", "CACETE*", "KCT*",
               "VAGABUNDA*",
               "PIROCA*", "PIROKA*", "PIROCÃO*", "BUCETA*", "BUCETUDA*"]
bypass_list = ["450336001081212938", "505558087537786890", "505561793134067732", "424633334849863680", "402077273961791499"]

@client.event
async def on_ready():
    print('╲╭━━━━━━━━╮╲ ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮')
    print('╲┃╭╮   ╭╮┃╲ ┃ BOT ONLINE - Hello World!')
    print(' ┗┫┏━━━━━━┓┣┛╲╰┳╮ NOME:', client.user.name)
    print('╲┃╰━━━━━━╯┃ ━━━╯┃ ID:', client.user.id)
    print('╲╰┳━━━━━━┳╯ \ \╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━-')
    print('[------------ONLINE------------]')
    await client.change_presence(game=discord.Game(name="Moderando | SkyMinigames".format(len(set(client.get_all_members())))))
    canal1 = client.get_channel('517459653525897251')
    canal2 = client.get_channel('517459682541961243')
    await client.edit_channel(canal1, name='off')
    await client.edit_channel(canal2, name='off')

@client.event
async def on_message(message):
    if not message.author == client.user:
        if not message.author.server_permissions.kick_members:
            spam = await client.wait_for_message(author=message.author, channel=message.channel)
            if spam.content == message.content:
                await client.delete_message(spam)
    
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            role = discord.utils.get(message.server.roles, name='STAFF')
            if not role in message.author.roles:
                if not message.author.id in bypass_list:
                    try:
                        await client.delete_message(message)
                        userID = message.author.id
                        deletar = await client.send_message(message.channel,
                                                        "<@%s> **Modere seu palavreado!**" % (
                                                            userID))
                        await asyncio.sleep(3)
                        await client.delete_message(deletar)
                    except discord.errors.NotFound:
                        return
                    except discord.errors.Forbidden:
                        return
    
    try:
        role = discord.utils.get(message.server.roles, name='STAFF')
        if not role in message.author.roles:
          if not message.author.id in bypass_list:
            for word in contents:

                if word.lower().startswith('discord.gg/'):
                    if not word.lower() == 'discord.gg/sky':
                        if not word.lower() == 'discord.gg/':
                            await client.delete_message(message)
                            await client.send_message(message.channel, '{} Convites de outros servidores não são permitidos aqui!'.format(message.author.mention))


                elif word.lower().startswith('https://discordapp.com/invite/'):
                    if not word.lower() == 'https://discordapp.com/invite/sky':
                        if not word.lower() == 'https://discordapp.com/invite/':
                            await client.delete_message(message)
                            await client.send_message(message.channel,
                                                      '{} Convites de outros servidores não são permitidos aqui!'.format(
                                                          message.author.mention))

                elif word.lower().startswith('https://discord.gg/'):
                    if not word.lower() == 'https://discord.gg/sky':
                        if not word.lower() == 'https://discord.gg/':
                            await client.delete_message(message)
                            await client.send_message(message.channel,
                                                      '{} Convites de outros servidores não são permitidos aqui!'.format(
                                                          message.author.mention))
    except:
        return


    prefix = '/'

    if message.content.lower().startswith(prefix+'unmute'):
        try:
            role = discord.utils.get(message.server.roles, name='STAFF')
            mutado = discord.utils.get(message.server.roles, name='MUTADO')
            user = message.mentions[0]
            unmute = discord.Embed(title=None, description=None, color=0xF2F2F2)
            unmute.set_author(name='[UNMUTE] {}'.format(user), icon_url=user.avatar_url)
            unmute.add_field(name='Usuário:', value=user.mention, inline=True)
            unmute.add_field(name='Autor:', value=message.author.mention, inline=True)
            channel = discord.utils.find(lambda c: c.name == 'punições-log', message.server.channels)
            if role in message.author.roles:
                if mutado in user.roles:
                    args = message.content.split(" ")
                    a = '%s' % (" ".join(args[2:]))
                    if not a == '':
                        unmute.add_field(name='Motivo:', value='%s' % (" ".join(args[2:])), inline=True)
                        await client.delete_message(message)
                        await client.remove_roles(user, mutado)
                        await client.send_message(message.channel, '{} Silenciamento removido.'.format(message.author.mention))
                        await client.send_message(channel, embed=unmute)
                    else:
                        unmute.add_field(name='Motivo:', value='Não informado.', inline=True)
                        await client.delete_message(message)
                        await client.remove_roles(user, mutado)
                        await client.send_message(message.channel, '{} Silenciamento removido.'.format(message.author.mention))
                        await client.send_message(channel, embed=unmute)
                else:
                    await client.delete_message(message)
                    await client.send_message(message.channel, '{} Esse usuário não está silenciado.'.format(message.author.mention))
            else:
                await client.send_message(message.channel, '{} Permissão insuficiente.'.format(message.author.mention))
        except AttributeError:
            await client.send_message(message.author, "Este comando não é executável por mensagem privada.")
        except IndexError:
            try:
                role = discord.utils.get(message.server.roles, name='STAFF')
                if role in message.author.roles:
                    await client.send_message(message.channel,
                                      '{} Mencione um usuário válido: **{}unmute @[user] [motivo]**'.format(
                                          message.author.mention, prefix))
                else:
                    await client.send_message(message.channel,
                                              '{} Permissão insuficiente.'.format(message.author.mention))
            except:
                return

    if message.content.lower().startswith(prefix+'punir'):
        try:
            role = discord.utils.get(message.server.roles, name='STAFF')
            user = message.mentions[0]
            unmute = discord.Embed(title=None, description=None, color=0xF2F2F2)
            unmute.set_author(name='[UNMUTE] {}'.format(user), icon_url=user.avatar_url)
            unmute.add_field(name='Usuário:', value=user, inline=True)
            unmute.add_field(name='Autor:', value='CONSOLE', inline=True)
            unmute.add_field(name='Motivo:', value='Tempo esgotado', inline=True)
            if role in message.author.roles:
              if not role in user.roles:
                args = message.content.split(" ")
                embed = discord.Embed(title='Aplicar punição | SkyMinigames',
                                      description='Selecione uma punição para o usuário: {}\n\n:one: **Spam/Flood**\n\n:two: **Informações Falsas**\n\n:three: **Comércio**\n\n:four: **Comportamento Tóxico**\n\n:five: **Ofensas** `I`\n\n:six: **Ofensas** `II`\n\n:seven: **Difamação**\n\n:eight: **Conteúdo Inapropriado**\n\n:nine: **Tentativa de Fraude**\n\n:keycap_ten: **Divulgação**\n\n\nPara aplicar a punição, digite o seu respectivo número:'.format(user.mention),
                                      color=0xAC58FA)
                embed.set_footer(text='Para cancelar, digite qualquer coisa.')
                try:
                    if toint(args[1]):
                        if args[1] == '1':
                            channel = discord.utils.find(lambda c: c.name == 'punições-log', message.server.channels)
                            try:
                                mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                                mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Tempmute', inline=True)
                                mute.add_field(name='Duração:', value='30 minutos', inline=True)
                                mute.add_field(name='Infração:', value='Spam/Flood', inline=True)
                                mute.add_field(name='Prova:', value='%s' % (" ".join(args[3:])), inline=True)
                                await client.send_message(channel, embed=mute)

                            except:
                                mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                                mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Tempmute', inline=True)
                                mute.add_field(name='Duração:', value='30 minutos', inline=True)
                                mute.add_field(name='Infração:', value='Spam/Flood', inline=True)
                                mute.add_field(name='Prova:', value='Não informado.', inline=True)
                                await client.send_message(channel, embed=mute)

                            mutado = discord.utils.get(message.server.roles, name='MUTADO')
                            await client.add_roles(user, mutado)
                            await client.delete_message(message)
                            await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))
                            await asyncio.sleep(1800)
                            try:
                                await client.remove_roles(user, mutado)
                                await client.send_message(channel, embed=unmute)
                            except:
                                return

                        elif args[1] == '2':
                            channel = discord.utils.find(lambda c: c.name == 'punições-log', message.server.channels)
                            try:
                                mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                                mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Tempmute', inline=True)
                                mute.add_field(name='Duração:', value='30 minutos', inline=True)
                                mute.add_field(name='Infração:', value='Informações Falsas', inline=True)
                                mute.add_field(name='Prova:', value='%s' % (" ".join(args[3:])), inline=True)
                                await client.send_message(channel, embed=mute)

                            except:
                                mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                                mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Tempmute', inline=True)
                                mute.add_field(name='Duração:', value='30 minutos', inline=True)
                                mute.add_field(name='Infração:', value='Informações Falsas', inline=True)
                                mute.add_field(name='Prova:', value='Não informado.', inline=True)
                                await client.send_message(channel, embed=mute)

                            mutado = discord.utils.get(message.server.roles, name='MUTADO')
                            await client.add_roles(user, mutado)
                            await client.delete_message(message)
                            await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))
                            await asyncio.sleep(1800)
                            try:
                                await client.remove_roles(user, mutado)
                                await client.send_message(channel, embed=unmute)
                            except:
                                return

                        elif args[1] == '3':
                            channel = discord.utils.find(lambda c: c.name == 'punições-log', message.server.channels)
                            try:
                                mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                                mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Tempmute', inline=True)
                                mute.add_field(name='Duração:', value='30 minutos', inline=True)
                                mute.add_field(name='Infração:', value='Comércio', inline=True)
                                mute.add_field(name='Prova:', value='%s' % (" ".join(args[3:])), inline=True)
                                await client.send_message(channel, embed=mute)

                            except:
                                mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                                mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Tempmute', inline=True)
                                mute.add_field(name='Duração:', value='30 minutos', inline=True)
                                mute.add_field(name='Infração:', value='Comércio', inline=True)
                                mute.add_field(name='Prova:', value='Não informado.', inline=True)
                                await client.send_message(channel, embed=mute)

                            mutado = discord.utils.get(message.server.roles, name='MUTADO')
                            await client.add_roles(user, mutado)
                            await client.delete_message(message)
                            await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))
                            await asyncio.sleep(1800)
                            try:
                                await client.remove_roles(user, mutado)
                                await client.send_message(channel, embed=unmute)
                            except:
                                return

                        elif args[1] == '4':
                            channel = discord.utils.find(lambda c: c.name == 'punições-log', message.server.channels)
                            try:
                                mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                                mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Tempmute', inline=True)
                                mute.add_field(name='Duração:', value='2 horas', inline=True)
                                mute.add_field(name='Infração:', value='Comportamento Tóxico', inline=True)
                                mute.add_field(name='Prova:', value='%s' % (" ".join(args[3:])), inline=True)
                                await client.send_message(channel, embed=mute)

                            except:
                                mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                                mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Tempmute', inline=True)
                                mute.add_field(name='Duração:', value='2 horas', inline=True)
                                mute.add_field(name='Infração:', value='Comportamento Tóxico', inline=True)
                                mute.add_field(name='Prova:', value='Não informado.', inline=True)
                                await client.send_message(channel, embed=mute)

                            mutado = discord.utils.get(message.server.roles, name='MUTADO')
                            await client.add_roles(user, mutado)
                            await client.delete_message(message)
                            await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))
                            await asyncio.sleep(7200)
                            try:
                                await client.remove_roles(user, mutado)
                                await client.send_message(channel, embed=unmute)
                            except:
                                return

                        elif args[1] == '5':
                            channel = discord.utils.find(lambda c: c.name == 'punições-log', message.server.channels)
                            try:
                                mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                                mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Tempmute', inline=True)
                                mute.add_field(name='Duração:', value='2 horas', inline=True)
                                mute.add_field(name='Infração:', value='Ofensas `I`', inline=True)
                                mute.add_field(name='Prova:', value='%s' % (" ".join(args[3:])), inline=True)
                                await client.send_message(channel, embed=mute)

                            except:
                                mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                                mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Tempmute', inline=True)
                                mute.add_field(name='Duração:', value='2 horas', inline=True)
                                mute.add_field(name='Infração:', value='Ofensas `I`', inline=True)
                                mute.add_field(name='Prova:', value='Não informado.', inline=True)
                                await client.send_message(channel, embed=mute)

                            mutado = discord.utils.get(message.server.roles, name='MUTADO')
                            await client.add_roles(user, mutado)
                            await client.delete_message(message)
                            await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))
                            await asyncio.sleep(7200)
                            try:
                                await client.remove_roles(user, mutado)
                                await client.send_message(channel, embed=unmute)
                            except:
                                return

                        elif args[1] == '6':
                            channel = discord.utils.find(lambda c: c.name == 'punições-log', message.server.channels)
                            try:
                                mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                                mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Banimento', inline=True)
                                mute.add_field(name='Duração:', value='Permanente', inline=True)
                                mute.add_field(name='Infração:', value='Ofensas `II`', inline=True)
                                mute.add_field(name='Prova:', value='%s' % (" ".join(args[3:])), inline=True)
                                await client.send_message(channel, embed=mute)
                            except:
                                mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                                mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Banimento', inline=True)
                                mute.add_field(name='Duração:', value='Permanente', inline=True)
                                mute.add_field(name='Infração:', value='Ofensas `II`', inline=True)
                                mute.add_field(name='Prova:', value='Não informado.', inline=True)
                                await client.send_message(channel, embed=mute)

                            await client.ban(user)
                            await client.delete_message(message)
                            await client.send_message(message.channel,
                                                      '{} Usuário punido.'.format(message.author.mention))

                        elif args[1] == '7':
                            channel = discord.utils.find(lambda c: c.name == 'punições-log', message.server.channels)
                            try:
                                mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                                mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Banimento', inline=True)
                                mute.add_field(name='Duração:', value='Permanente', inline=True)
                                mute.add_field(name='Infração:', value='Difamação', inline=True)
                                mute.add_field(name='Prova:', value='%s' % (" ".join(args[3:])), inline=True)
                                await client.send_message(channel, embed=mute)
                            except:
                                mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                                mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Banimento', inline=True)
                                mute.add_field(name='Duração:', value='Permanente', inline=True)
                                mute.add_field(name='Infração:', value='Difamação', inline=True)
                                mute.add_field(name='Prova:', value='Não informado.', inline=True)
                                await client.send_message(channel, embed=mute)

                            await client.ban(user)
                            await client.delete_message(message)
                            await client.send_message(message.channel,
                                                      '{} Usuário punido.'.format(message.author.mention))

                        elif args[1] == '8':
                            channel = discord.utils.find(lambda c: c.name == 'punições-log', message.server.channels)
                            try:
                                mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                                mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Banimento', inline=True)
                                mute.add_field(name='Duração:', value='Permanente', inline=True)
                                mute.add_field(name='Infração:', value='Conteúdo Inapropriado', inline=True)
                                mute.add_field(name='Prova:', value='%s' % (" ".join(args[3:])), inline=True)
                                await client.send_message(channel, embed=mute)
                            except:
                                mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                                mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Banimento', inline=True)
                                mute.add_field(name='Duração:', value='Permanente', inline=True)
                                mute.add_field(name='Infração:', value='Conteúdo Inapropriado', inline=True)
                                mute.add_field(name='Prova:', value='Não informado.', inline=True)
                                await client.send_message(channel, embed=mute)

                            await client.ban(user)
                            await client.delete_message(message)
                            await client.send_message(message.channel,
                                                      '{} Usuário punido.'.format(message.author.mention))

                        elif args[1] == '9':
                            channel = discord.utils.find(lambda c: c.name == 'punições-log', message.server.channels)
                            try:
                                mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                                mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Banimento', inline=True)
                                mute.add_field(name='Duração:', value='Permanente', inline=True)
                                mute.add_field(name='Infração:', value='Tentativa de Fraude', inline=True)
                                mute.add_field(name='Prova:', value='%s' % (" ".join(args[3:])), inline=True)
                                await client.send_message(channel, embed=mute)
                            except:
                                mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                                mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Banimento', inline=True)
                                mute.add_field(name='Duração:', value='Permanente', inline=True)
                                mute.add_field(name='Infração:', value='Tentativa de Fraude', inline=True)
                                mute.add_field(name='Prova:', value='Não informado.', inline=True)
                                await client.send_message(channel, embed=mute)

                            await client.ban(user)
                            await client.delete_message(message)
                            await client.send_message(message.channel,
                                                      '{} Usuário punido.'.format(message.author.mention))

                        elif args[1] == '10':
                            channel = discord.utils.find(lambda c: c.name == 'punições-log', message.server.channels)
                            try:
                                mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                                mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Banimento', inline=True)
                                mute.add_field(name='Duração:', value='Permanente', inline=True)
                                mute.add_field(name='Infração:', value='Divulgação', inline=True)
                                mute.add_field(name='Prova:', value='%s' % (" ".join(args[3:])), inline=True)
                                await client.send_message(channel, embed=mute)
                            except:
                                mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                                mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                                mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                                mute.add_field(name='Infrator:', value=user.mention, inline=True)
                                mute.add_field(name='Punição:', value='Banimento', inline=True)
                                mute.add_field(name='Duração:', value='Permanente', inline=True)
                                mute.add_field(name='Infração:', value='Divulgação', inline=True)
                                mute.add_field(name='Prova:', value='Não informado.', inline=True)
                                await client.send_message(channel, embed=mute)

                            await client.ban(user)
                            await client.delete_message(message)
                            await client.send_message(message.channel,
                                                      '{} Usuário punido.'.format(message.author.mention))

                        else:
                            await client.delete_message(message)
                            await client.send_message(message.channel,
                                                      '{} Não existe uma punição de número `{}`.'.format(message.author.mention, args[1]))
                except:
                    bbb = await client.send_message(message.channel, embed=embed)
                    aaa = await client.wait_for_message(author=message.author, channel=message.channel)
                    channel = discord.utils.find(lambda c: c.name == 'punições-log', message.server.channels)
                    if aaa.content == '1':
                        try:
                            mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                            mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Tempmute', inline=True)
                            mute.add_field(name='Duração:', value='30 minutos', inline=True)
                            mute.add_field(name='Infração:', value='Spam/Flood', inline=True)
                            mute.add_field(name='Prova:', value='%s' % (" ".join(args[2:])), inline=True)
                            await client.send_message(channel, embed=mute)

                        except:
                            mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                            mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Tempmute', inline=True)
                            mute.add_field(name='Duração:', value='30 minutos', inline=True)
                            mute.add_field(name='Infração:', value='Spam/Flood', inline=True)
                            mute.add_field(name='Prova:', value='Não informado.', inline=True)
                            await client.send_message(channel, embed=mute)

                        mutado = discord.utils.get(message.server.roles, name='MUTADO')
                        await client.add_roles(user, mutado)
                        await client.delete_message(message)
                        await client.delete_message(bbb)
                        await client.delete_message(aaa)
                        await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))
                        await asyncio.sleep(1800)
                        try:
                            await client.remove_roles(user, mutado)
                            await client.send_message(channel, embed=unmute)
                        except:
                            return

                    elif aaa.content == '2':
                        try:
                            mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                            mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Tempmute', inline=True)
                            mute.add_field(name='Duração:', value='30 minutos', inline=True)
                            mute.add_field(name='Infração:', value='Informações Falsas', inline=True)
                            mute.add_field(name='Prova:', value='%s' % (" ".join(args[2:])), inline=True)
                            await client.send_message(channel, embed=mute)
                        except:
                            mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                            mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Tempmute', inline=True)
                            mute.add_field(name='Duração:', value='30 minutos', inline=True)
                            mute.add_field(name='Infração:', value='Informações Falsas', inline=True)
                            mute.add_field(name='Prova:', value='Não informado.', inline=True)
                            await client.send_message(channel, embed=mute)

                        mutado = discord.utils.get(message.server.roles, name='MUTADO')
                        await client.add_roles(user, mutado)
                        await client.delete_message(message)
                        await client.delete_message(bbb)
                        await client.delete_message(aaa)
                        await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))
                        await asyncio.sleep(1800)
                        try:
                            await client.remove_roles(user, mutado)
                            await client.send_message(channel, embed=unmute)
                        except:
                            return

                    elif aaa.content == '3':
                        try:
                            mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                            mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Tempmute', inline=True)
                            mute.add_field(name='Duração:', value='30 minutos', inline=True)
                            mute.add_field(name='Infração:', value='Comércio', inline=True)
                            mute.add_field(name='Prova:', value='%s' % (" ".join(args[2:])), inline=True)
                            await client.send_message(channel, embed=mute)
                        except:
                            mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                            mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Tempmute', inline=True)
                            mute.add_field(name='Duração:', value='30 minutos', inline=True)
                            mute.add_field(name='Infração:', value='Comércio', inline=True)
                            mute.add_field(name='Prova:', value='Não informado.', inline=True)
                            await client.send_message(channel, embed=mute)

                        mutado = discord.utils.get(message.server.roles, name='MUTADO')
                        await client.add_roles(user, mutado)
                        await client.delete_message(message)
                        await client.delete_message(bbb)
                        await client.delete_message(aaa)
                        await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))
                        await asyncio.sleep(1800)
                        try:
                            await client.remove_roles(user, mutado)
                            await client.send_message(channel, embed=unmute)
                        except:
                            return

                    elif aaa.content == '4':
                        try:
                            mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                            mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Tempmute', inline=True)
                            mute.add_field(name='Duração:', value='2 horas', inline=True)
                            mute.add_field(name='Infração:', value='Comportamento Tóxico', inline=True)
                            mute.add_field(name='Prova:', value='%s' % (" ".join(args[2:])), inline=True)
                            await client.send_message(channel, embed=mute)
                        except:
                            mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                            mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Tempmute', inline=True)
                            mute.add_field(name='Duração:', value='2 horas', inline=True)
                            mute.add_field(name='Infração:', value='Comportamento Tóxico', inline=True)
                            mute.add_field(name='Prova:', value='Não informado.', inline=True)
                            await client.send_message(channel, embed=mute)

                        mutado = discord.utils.get(message.server.roles, name='MUTADO')
                        await client.add_roles(user, mutado)
                        await client.delete_message(message)
                        await client.delete_message(bbb)
                        await client.delete_message(aaa)
                        await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))
                        await asyncio.sleep(7200)
                        try:
                            await client.remove_roles(user, mutado)
                            await client.send_message(channel, embed=unmute)
                        except:
                            return

                    elif aaa.content == '5':
                        try:
                            mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                            mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Tempmute', inline=True)
                            mute.add_field(name='Duração:', value='2 horas', inline=True)
                            mute.add_field(name='Infração:', value='Ofensas `I`', inline=True)
                            mute.add_field(name='Prova:', value='%s' % (" ".join(args[2:])), inline=True)
                            await client.send_message(channel, embed=mute)
                        except:
                            mute = discord.Embed(title=None, description=None, color=0xFACC2E)
                            mute.set_author(name='[MUTE] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Tempmute', inline=True)
                            mute.add_field(name='Duração:', value='2 horas', inline=True)
                            mute.add_field(name='Infração:', value='Ofensas `I`', inline=True)
                            mute.add_field(name='Prova:', value='Não informado.', inline=True)
                            await client.send_message(channel, embed=mute)

                        mutado = discord.utils.get(message.server.roles, name='MUTADO')
                        await client.add_roles(user, mutado)
                        await client.delete_message(message)
                        await client.delete_message(bbb)
                        await client.delete_message(aaa)
                        await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))
                        await asyncio.sleep(7200)
                        try:
                            await client.remove_roles(user, mutado)
                            await client.send_message(channel, embed=unmute)
                        except:
                            return

                    elif aaa.content == '6':
                        try:
                            mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                            mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Banimento', inline=True)
                            mute.add_field(name='Duração:', value='Permanente', inline=True)
                            mute.add_field(name='Infração:', value='Ofensas `II`', inline=True)
                            mute.add_field(name='Prova:', value='%s' % (" ".join(args[2:])), inline=True)
                            await client.send_message(channel, embed=mute)
                        except:
                            mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                            mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Banimento', inline=True)
                            mute.add_field(name='Duração:', value='Permanente', inline=True)
                            mute.add_field(name='Infração:', value='Ofensas `II`', inline=True)
                            mute.add_field(name='Prova:', value='Não informado.', inline=True)
                            await client.send_message(channel, embed=mute)

                        await client.ban(user)
                        await client.delete_message(message)
                        await client.delete_message(bbb)
                        await client.delete_message(aaa)
                        await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))

                    elif aaa.content == '7':
                        try:
                            mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                            mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Banimento', inline=True)
                            mute.add_field(name='Duração:', value='Permanente', inline=True)
                            mute.add_field(name='Infração:', value='Difamação', inline=True)
                            mute.add_field(name='Prova:', value='%s' % (" ".join(args[2:])), inline=True)
                            await client.send_message(channel, embed=mute)
                        except:
                            mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                            mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Banimento', inline=True)
                            mute.add_field(name='Duração:', value='Permanente', inline=True)
                            mute.add_field(name='Infração:', value='Difamação', inline=True)
                            mute.add_field(name='Prova:', value='Não informado.', inline=True)
                            await client.send_message(channel, embed=mute)

                        await client.ban(user)
                        await client.delete_message(message)
                        await client.delete_message(bbb)
                        await client.delete_message(aaa)
                        await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))

                    elif aaa.content == '8':
                        try:
                            mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                            mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Banimento', inline=True)
                            mute.add_field(name='Duração:', value='Permanente', inline=True)
                            mute.add_field(name='Infração:', value='Conteúdo Inapropriado', inline=True)
                            mute.add_field(name='Prova:', value='%s' % (" ".join(args[2:])), inline=True)
                            await client.send_message(channel, embed=mute)
                        except:
                            mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                            mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Banimento', inline=True)
                            mute.add_field(name='Duração:', value='Permanente', inline=True)
                            mute.add_field(name='Infração:', value='Conteúdo Inapropriado', inline=True)
                            mute.add_field(name='Prova:', value='Não informado.', inline=True)
                            await client.send_message(channel, embed=mute)

                        await client.ban(user)
                        await client.delete_message(message)
                        await client.delete_message(bbb)
                        await client.delete_message(aaa)
                        await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))

                    elif aaa.content == '9':
                        try:
                            mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                            mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Banimento', inline=True)
                            mute.add_field(name='Duração:', value='Permanente', inline=True)
                            mute.add_field(name='Infração:', value='Tentativa de Fraude', inline=True)
                            mute.add_field(name='Prova:', value='%s' % (" ".join(args[2:])), inline=True)
                            await client.send_message(channel, embed=mute)
                        except:
                            mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                            mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Banimento', inline=True)
                            mute.add_field(name='Duração:', value='Permanente', inline=True)
                            mute.add_field(name='Infração:', value='Tentativa de Fraude', inline=True)
                            mute.add_field(name='Prova:', value='Não informado.', inline=True)
                            await client.send_message(channel, embed=mute)

                        await client.ban(user)
                        await client.delete_message(message)
                        await client.delete_message(bbb)
                        await client.delete_message(aaa)
                        await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))

                    elif aaa.content == '10':
                        try:
                            mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                            mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Banimento', inline=True)
                            mute.add_field(name='Duração:', value='Permanente', inline=True)
                            mute.add_field(name='Infração:', value='Divulgação', inline=True)
                            mute.add_field(name='Prova:', value='%s' % (" ".join(args[2:])), inline=True)
                            await client.send_message(channel, embed=mute)
                        except:
                            mute = discord.Embed(title=None, description=None, color=0xFE2E2E)
                            mute.set_author(name='[BAN] {}'.format(user), icon_url=user.avatar_url)
                            mute.add_field(name='Autor:', value=message.author.mention, inline=True)
                            mute.add_field(name='Infrator:', value=user.mention, inline=True)
                            mute.add_field(name='Punição:', value='Banimento', inline=True)
                            mute.add_field(name='Duração:', value='Permanente', inline=True)
                            mute.add_field(name='Infração:', value='Divulgação', inline=True)
                            mute.add_field(name='Prova:', value='Não informado.', inline=True)
                            await client.send_message(channel, embed=mute)

                        await client.ban(user)
                        await client.delete_message(message)
                        await client.delete_message(bbb)
                        await client.delete_message(aaa)
                        await client.send_message(message.channel, '{} Usuário punido.'.format(message.author.mention))

                    else:
                        await client.delete_message(message)
                        await client.delete_message(bbb)
                        await client.delete_message(aaa)
                        await client.send_message(message.channel, '{} Punição cancelada.'.format(message.author.mention))
              else:
                  await client.delete_message(message)
                  await client.send_message(message.channel, '{} Este usuário não pode ser punido.'.format(message.author.mention))
            else:
                await client.send_message(message.channel, '{} Permissão insuficiente.'.format(message.author.mention))
        except AttributeError:
            await client.send_message(message.author, "Este comando não é executável por mensagem privada.")
        except IndexError:
            try:
                role = discord.utils.get(message.server.roles, name='STAFF')
                if role in message.author.roles:
                    await client.send_message(message.channel,
                                      '{} Mencione um usuário válido: **{}punir @[user] [prova]**'.format(
                                          message.author.mention, prefix))
                else:
                    await client.send_message(message.channel,
                                              '{} Permissão insuficiente.'.format(message.author.mention))
            except:
                return


@client.event
async def on_message_edit(before, after):
    embed = discord.Embed(title="Mensagem Editada", description="Uma mensagem foi editada neste servidor:", color=0x01A9DB)
    embed.add_field(name="Autor:", value=after.author.mention, inline=True)
    embed.add_field(name="Canal:", value=after.channel.mention, inline=True)
    embed.add_field(name="Mensagem Original:", value='```{}```'.format(before.content), inline=False)
    embed.add_field(name="Mensagem Editada:", value='```{}```'.format(after.content), inline=False)
    embed.set_footer(text="Server Log | SkyMinigames | às {}".format(times()), icon_url=before.server.icon_url)
    channel = discord.utils.find(lambda c: c.name == 'server-log', after.server.channels)

    if not after.content == '':
        if not before.content == after.content:
            await client.send_message(channel, embed=embed)

    contents = after.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            role = discord.utils.get(after.server.roles, name='STAFF')
            if not role in after.author.roles:
                if not message.author.id == '505558087537786890':
                    try:
                        await client.delete_message(after)
                        userID = after.author.id
                        deletar = await client.send_message(after.channel,
                                                        "<@%s> **Modere seu palavreado!**" % (
                                                            userID))
                        await asyncio.sleep(3)
                        await client.delete_message(deletar)
                    except discord.errors.NotFound:
                        return
                    except discord.errors.Forbidden:
                        return

    contents = after.content.split(" ")
    try:
        role = discord.utils.get(after.server.roles, name='STAFF')
        if not role in after.author.roles:
            if not after.author.id == '505558087537786890':
                for word in contents:

                    if word.lower().startswith('discord.gg/'):
                        if not word.lower() == 'discord.gg/sky':
                            if not word.lower() == 'discord.gg/':
                                await client.delete_message(after)
                                await client.send_message(after.channel, '{} Convites de outros servidores não são permitidos aqui!'.format(after.author.mention))


                    if word.lower().startswith('https://discordapp.com/invite/'):
                        if not word.lower() == 'https://discordapp.com/invite/sky':
                            if not word.lower() == 'https://discordapp.com/invite/':
                                await client.delete_message(after)
                                await client.send_message(after.channel,
                                                      '{} Convites de outros servidores não são permitidos aqui!'.format(
                                                          after.author.mention))

                    if word.lower().startswith('https://discord.gg/'):
                        if not word.lower() == 'https://discord.gg/sky':
                            if not word.lower() == 'https://discord.gg/':
                                await client.delete_message(after)
                                await client.send_message(after.channel,
                                                      '{} Convites de outros servidores não são permitidos aqui!'.format(
                                                          after.author.mention))
    except:
        return

@client.event
async def on_message_delete(message):
    embed = discord.Embed(title="Mensagem Apagada", description="Uma mensagem foi apagada neste servidor:", color=0xFA5858)
    embed.add_field(name="Autor:", value=message.author.mention, inline=True)
    embed.add_field(name="Canal:", value=message.channel.mention, inline=True)
    embed.add_field(name="Mensagem:", value='```{}```'.format(message.content), inline=False)
    embed.set_footer(text="Server Log | SkyMinigames | às {}".format(times()), icon_url=message.server.icon_url)
    channel = discord.utils.find(lambda c: c.name == 'server-log', message.server.channels)
    await client.send_message(channel, embed=embed)

@client.event
async def on_member_remove(member):
    role = discord.utils.get(member.server.roles, name='MUTADO')
    if role in member.roles:
        canal1 = client.get_channel('517459653525897251')
        canal2 = client.get_channel('517459682541961243')
        if canal1.name == 'off':
            await client.edit_channel(canal1, name=member.id)
        else:
            await client.edit_channel(canal2, name=member.id)

    embed = discord.Embed(title="Usuário Saiu", description="Um usuário saiu deste servidor: (ID: {})".format(member.id), color=0xFA5858)
    embed.add_field(name="Membro:", value=member.mention, inline=True)
    embed.add_field(name="Nome:", value=member.name, inline=True)
    embed.add_field(name="Cargo:", value=member.top_role.mention, inline=True)
    embed.set_footer(text="Server Log | SkyMinigames | às {}".format(times()), icon_url=member.server.icon_url)
    channel = discord.utils.find(lambda c: c.name == 'server-log', member.server.channels)
    await client.send_message(channel, embed=embed)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='MUTADO')
    canal1 = client.get_channel('517459653525897251')
    canal2 = client.get_channel('517459682541961243')
    if canal1.name == member.id:
        await client.add_roles(member, role)
        await client.edit_channel(canal1, name='off')
    else:
        if canal2.name == member.id:
            await client.add_roles(member, role)
            await client.edit_channel(canal2, name='off')

    embed = discord.Embed(title="Usuário Entrou", description="Um usuário entrou neste servidor: (ID: {})".format(member.id), color=0xFF781)
    embed.add_field(name="Membro:", value=member.mention, inline=True)
    embed.add_field(name="Nome:", value=member.name, inline=True)
    embed.add_field(name="Cargo:", value=member.top_role.mention, inline=True)
    embed.set_footer(text="Server Log | SkyMinigames | às {}".format(times()), icon_url=member.server.icon_url)
    channel = discord.utils.find(lambda c: c.name == 'server-log', member.server.channels)
    await client.send_message(channel, embed=embed)

@client.event
async def on_member_ban(member):
    embed = discord.Embed(title="Banimento Aplicado",
                          description="Um usuário foi banido deste servidor:", color=0xFA5858)
    embed.add_field(name="Membro:", value=member.mention, inline=True)
    embed.add_field(name="ID:", value=member.id, inline=True)
    embed.set_footer(text="Server Log | SkyMinigames | às {}".format(times()), icon_url=member.server.icon_url)
    channel = discord.utils.find(lambda c: c.name == 'server-log', member.server.channels)
    await client.send_message(channel, embed=embed)

@client.event
async def on_member_unban(server, member):
    embed = discord.Embed(title="Banimento Removido",
                          description="Um usuário teve seu banimento removido deste servidor:", color=0xFF781)
    embed.add_field(name="Membro:", value=member.mention, inline=True)
    embed.add_field(name="ID:", value=member.id, inline=True)
    embed.set_footer(text="Server Log | SkyMinigames | às {}".format(times()), icon_url=member.server.icon_url)
    channel = discord.utils.find(lambda c: c.name == 'server-log', server.channels)
    await client.send_message(channel, embed=embed)

client.run(token)
