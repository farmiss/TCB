from discord import Webhook, RequestsWebhookAdapter, Embed, Color
import datetime

def send_cyber(product, size, profile, category, color, thumbnail):
    embed = Embed(title='Successfully checked out!', description=product, color=65365)
    embed.add_field(name='Store', value='Supreme US', inline=True)
    embed.add_field(name='Size', value=size, inline=True)
    embed.add_field(name='Profile', value='||{p}||'.format(p=profile), inline=True)
    embed.add_field(name='Order', value='||123456||', inline=True)
    embed.add_field(name='Proxy List', value='||Default||', inline=True)
    embed.add_field(name='Category', value=category, inline=True)
    embed.add_field(name='Color', value=color, inline=True)
    embed.add_field(name='Quantity', value='1', inline=True)
    embed.add_field(name='Captcha Bypass', value='Enabled', inline=True)
    embed.add_field(name='Mode', value='Safe', inline=True)
    embed.set_footer(text='CyberAIO • {timestamp}'.format(timestamp=datetime.datetime.now().strftime('%m/%d/%Y %I:%M:%S.%f')[:-3]),
                     icon_url='https://images-ext-2.discordapp.net/external/AFl8btw6-OdaFIC4DU6c8as5gTG8SIVdsOx_hLOXnEs/https/cdn.cybersole.io/media/discord-logo.png')
    embed.set_thumbnail(url=thumbnail)
    return embed


def send_kodai(product, size, color, profile, thumbnail):
    embed = Embed(title=':rocket: Kodai Success :rocket:', color=Color(0x6afe94))
    embed.add_field(name='Store', value='Supreme US', inline=True)
    embed.add_field(name='Checkout Speed', value='6.629s', inline=True)
    embed.add_field(name='Product', value=product, inline=False)
    embed.add_field(name='Size', value='{s} -- {c}'.format(s=size,c=color), inline=True)
    embed.add_field(name='Profile', value='||{p}|| :flag_us:'.format(p=profile), inline=True)
    embed.add_field(name='Order Number', value='||1234567||', inline=True)
    embed.set_footer(text='KodaiAIO ― {p} • [{timestamp}]'.format(p=product.split()[0],timestamp=datetime.datetime.now().strftime('%a %b %d %Y')), icon_url='https://images-ext-2.discordapp.net/external/krVmbzqvZ1lgEThP_2eA0D60X_9xKP8d4tI_sL_YBs0/https/i.imgur.com/Z1ALPb8.png')
    embed.set_thumbnail(url=thumbnail)
    return embed

def send_balko(product, size, profile, thumbnail):
    embed = Embed(title='Success - Supreme US')
    embed.add_field(name='Size', value=size, inline=True)
    embed.add_field(name='Product', value=product, inline=True)
    embed.add_field(name='Delay', value='5500', inline=True)
    embed.add_field(name='Profile', value='||{p}||'.format(p=profile), inline=False)
    embed.add_field(name='Tasks', value='10', inline=False)
    embed.set_footer(text='Balkobot', icon_url='https://images-ext-1.discordapp.net/external/Ozcq5ehNVn0MAAmxFxi9EyRGT6QHAukkoBIedAyWTMM/https/pbs.twimg.com/profile_images/1177062169231405056/9whojPiW_400x400.jpg')
    embed.set_thumbnail(url=thumbnail)
    return embed

def send_webhook(bot, product, size, category, color, profile, thumbnail, webhook, webhook_author='Spidey Bot', webhook_avatar='https://discordapp.com/assets/6debd47ed13483642cf09e832ed0bc1b.png'):
    #url = 'https://ptb.discordapp.com/api/webhooks/699263716859969586/o1YEjsT2aQtgG0NGgfHgaVxTkL9sVttTYLBKJ_hQt9ey5NSTRVnu0yrggHOK2YdpMN8q'
    webhook = Webhook.from_url(webhook, adapter=RequestsWebhookAdapter())
    if bot == 'cyber':
        embed = send_cyber(product, size, profile, category, color, thumbnail)
    elif bot == 'kodai':
        embed = send_kodai(product, size, color, profile, thumbnail)
    elif bot == 'balko':
        embed =send_balko(product, size, profile, thumbnail)
    webhook.send(embed=embed, avatar_url=webhook_avatar, username=webhook_author)

if __name__ == '__main__':
    print('This is a test webhook for Supreme US')
    webhook = input('Webhook: ')
    webhook_author = input('Webhook author(optional): ')
    webhook_avatar = input('Webhook avatar(optional): ')
    product = input('Product title: ')
    size = input('Product size: ')
    category = input('Category: ')
    color = input('Color: ')
    profile = input('Profile: ')
    thumbnail = input('Product image: ')
    while True:
        bot = input('Which Bot? (Please select from Cyber, Kodai, Balko)\n')
        if bot.lower() in ['cyber', 'kodai', 'balko']:
            send_webhook(bot.lower(), product, size, category, color, profile, thumbnail, webhook, webhook_author, webhook_avatar)
            print('{bot} webhook successfully sent'.format(bot=bot))
            if input('Try another bot? Y/N \n').lower() == 'n':
                break
        else:
            print('Unsupported bot selected! Only supports Cyber, Kodai, Balko')


