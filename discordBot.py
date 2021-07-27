#pip install discord.py

import discord
from discord import channel
from discord.ext import commands

import random

#Prefixo que será usado antes dos comandos, nesse bot é o "_"

client = commands.Bot(command_prefix = "_", case_insesitive = False)

#comando para avisar quando o bot estiver online

@client.event
async def on_ready():
    print('~Online~')

#comando para responder um comando no chat do discord - Comando: _teste

@client.command()
async def teste(ctx):
    await ctx.send('Funciona')

#comando somar 2 numeros  - Comando: _soma 1 1 (os numeros a serem somados, separados por espaço)

@client.command() 
async def soma(ctx, *nums):
    operation = " + ".join(nums)
    await ctx.send(f'{operation} = {eval(operation)}')

#sortear numeros  - Comando: _sorteio 80 (Sorteia números de 1 à 80)

@client.command()
async def sorteio(ctx, numero):
    valor = random.randint(1,int(numero))
    await ctx.send(f'O número sorteado é {valor}')

#trocar apelido - necessário criar um cargo com as permissões e atribuir ao bot - Comando: _trocarapelido @user novoApelido

@client.command(pass_content = True)
async def trocarapelido(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'O apelido de {member.mention} agora é {nick}')

client.run('colar token disponivel no site do discord - https://discord.com/developers/applications')
