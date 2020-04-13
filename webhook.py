from discord import Webhook, RequestsWebhookAdapter, Embed
import datetime

def avatar_url():
    return 'https://cdn.discordapp.com/avatars/597984411694399490/b63669f142e713de30f1f5f48b33502d.webp?size=128'

def send_webhook():
    #url = 'https://ptb.discordapp.com/api/webhooks/699263716859969586/o1YEjsT2aQtgG0NGgfHgaVxTkL9sVttTYLBKJ_hQt9ey5NSTRVnu0yrggHOK2YdpMN8q'
    url = 'https://discordapp.com/api/webhooks/699310644175831150/pbSn_8su8B9heSkl3_a7dYVJ0M7g3pu9I8RolgITtyig5p8ALrIE4NnZ51z5bQ5J_nSU'
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    embed = Embed(title='Successfully checked out!',description='Motion Logo Beanie')
    embed.add_field(name='Store', value='Supreme US', inline=True)
    embed.add_field(name='Size', value='N/A', inline=True)
    embed.add_field(name='Profile', value='||Test US||', inline=True)
    embed.add_field(name='Order', value='||123456||', inline=True)
    embed.add_field(name='Proxy List', value='||Supreme||', inline=True)
    embed.add_field(name='Category', value='Hats', inline=True)
    embed.add_field(name='Color', value='black', inline=True)
    embed.add_field(name='Quantity', value='1', inline=True)
    embed.add_field(name='Captcha Bypass', value='Enabled', inline=True)
    embed.add_field(name='Mode', value='safe', inline=True)
    embed.set_author(name='', icon_url='https://images-ext-2.discordapp.net/external/th0cNlyGulQ8O3T4TiSv9gXrNe7Rah4bvj0kdS43zCY/https/assets.supremenewyork.com/186430/rs/JS7Ta8AUyo4.jpg?width=80&height=80')
    embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/th0cNlyGulQ8O3T4TiSv9gXrNe7Rah4bvj0kdS43zCY/https/assets.supremenewyork.com/186430/rs/JS7Ta8AUyo4.jpg?width=80&height=80')
    embed.timestamp = datetime.datetime.now().strftime('%d/%m/%Y %I:%M:%S%p')

    webhook.send(embed=embed,avatar_url=avatar_url())
send_webhook()