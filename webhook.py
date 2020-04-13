from discord import Webhook, RequestsWebhookAdapter, Embed, Color
import datetime
import Color

def avatar_url():
    return 'https://cdn.discordapp.com/avatars/597984411694399490/b63669f142e713de30f1f5f48b33502d.webp?size=128'

def send_cyber(webhook):
    embed = Embed(title='Successfully checked out!', description='Motion Logo Beanie', color=65365)
    embed.add_field(name='Store', value='Supreme US', inline=True)
    embed.add_field(name='Size', value='N/A', inline=True)
    embed.add_field(name='Profile', value='||Test US||', inline=True)
    embed.add_field(name='Order', value='||123456||', inline=True)
    embed.add_field(name='Proxy List', value='||Supreme||', inline=True)
    embed.add_field(name='Category', value='Hats', inline=True)
    embed.add_field(name='Color', value='black', inline=True)
    embed.add_field(name='Quantity', value='1', inline=True)
    embed.add_field(name='Captcha Bypass', value='Enabled', inline=True)
    embed.add_field(name='Mode', value='Safe', inline=True)
    embed.set_footer(text='CyberAIO • {timestamp}'.format(timestamp=datetime.datetime.now().strftime('%m/%d/%Y %I:%M:%S.%f')[:-3]),
                     icon_url='https://images-ext-2.discordapp.net/external/AFl8btw6-OdaFIC4DU6c8as5gTG8SIVdsOx_hLOXnEs/https/cdn.cybersole.io/media/discord-logo.png')
    embed.set_thumbnail(
        url='https://images-ext-2.discordapp.net/external/th0cNlyGulQ8O3T4TiSv9gXrNe7Rah4bvj0kdS43zCY/https/assets.supremenewyork.com/186430/rs/JS7Ta8AUyo4.jpg?width=80&height=80')
    webhook.send(embed=embed, avatar_url=avatar_url(), username='CyberAIO')


def send_kodai(webhook):
    embed = Embed(title=':rocket: Kodai Success :rocket:', color=Color(0x6afe94))
    embed.add_field(name='Store', value='Supreme US', inline=True)
    embed.add_field(name='Checkout Speed', value='6.629s', inline=True)
    embed.add_field(name='Product', value='Tupac Hologram TeeBlack', inline=False)
    embed.add_field(name='Size', value='Preferred ― White', inline=True)
    embed.add_field(name='Profile', value='||Test US|| :flag_us:', inline=True)
    embed.add_field(name='Order Number', value='||1234567||', inline=True)
    embed.set_footer(text='KodaiAIO ― Tupac • [{timestamp}]'.format(timestamp=datetime.datetime.now().strftime('%a %b %d %Y')), icon_url='https://images-ext-2.discordapp.net/external/krVmbzqvZ1lgEThP_2eA0D60X_9xKP8d4tI_sL_YBs0/https/i.imgur.com/Z1ALPb8.png')
    embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/BMos3gyfY3IuYH5jEvqAZTvf3hkcRWujTzUE9OaoO6g/https/assets.supremenewyork.com/186866/rs/Q_naMtqtDYQ.jpg?width=80&height=80')
    webhook.send(embed=embed)

def send_balko(webhook):
    embed = Embed(title='Success - kith.com', url='https://kith.com/')
    embed.add_field(name='Size', value='XL', inline=True)
    embed.add_field(name='Product', value='Kith x Advisory Board Crystals Holograph Hoodie - Storm Dye', inline=True)
    embed.add_field(name='Delay', value='5500', inline=True)
    embed.add_field(name='Profile', value='||Test US||', inline=False)
    embed.add_field(name='Tasks', value='10', inline=False)
    embed.set_footer(text='Balkobot', icon_url='https://images-ext-1.discordapp.net/external/Ozcq5ehNVn0MAAmxFxi9EyRGT6QHAukkoBIedAyWTMM/https/pbs.twimg.com/profile_images/1177062169231405056/9whojPiW_400x400.jpg')
    embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/V1HwRVHDoHfraBU8ehoPwt_pgAcDIuwHumZrRhhXlkU/%3Fv%3D1585942492/https/cdn.shopify.com/s/files/1/0094/2252/products/ABC2002-110_007_775486ca-4ec3-4754-9a83-8d9d35283c81.jpg?width=80&height=80')
    webhook.send(embed=embed)

def send_webhook(bot):
    #url = 'https://ptb.discordapp.com/api/webhooks/699263716859969586/o1YEjsT2aQtgG0NGgfHgaVxTkL9sVttTYLBKJ_hQt9ey5NSTRVnu0yrggHOK2YdpMN8q'
    url = 'https://discordapp.com/api/webhooks/699310644175831150/pbSn_8su8B9heSkl3_a7dYVJ0M7g3pu9I8RolgITtyig5p8ALrIE4NnZ51z5bQ5J_nSU'
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    if bot == 'cyber':
        send_cyber(webhook)
    elif bot == 'kodai':
        send_kodai(webhook)
    elif bot == 'balko':
        send_balko(webhook)

if __name__ == '__main__':
    while True:
        bot = input('Which Bot? (Please select from Cyber, Kodai, Balko)\n').lower()
        if bot in ['cyber', 'kodai', 'balko']:
            break
        else:
            print('Unsupported bot selected! Only supports Cyber, Kodai, Balko')
    send_webhook(bot)

