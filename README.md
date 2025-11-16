# 🦠 **Disease Remote Nuker — by xfsc**

A fully remote-controlled **Nextcord (Python)** bot designed for server management, raid tools, bypass utilities, logging systems, and automated actions through direct messages.  
The bot operates **exclusively through DMs**, ensuring privacy and controlled access.

---

## 🚀 **Main Features**

- 🔒 **Main server authorization**  
  Only users inside the MAIN_GUILD can execute commands.

- 🛰️ **Remote DM control**  
  All commands work through DMs, offering stealth and safety.

- 🧨 **Full Nuke System**  
  Deletes channels, creates channels, changes name/icon, spams, removes roles, renames all members, and more.

- 💥 **Massive simultaneous spam**  
  Uses asyncio to spam all channels at once.

- 👑 **Self-admin command**  
  Gives you administrator permissions on the selected server.

- 🔎 **Advanced logging**  
  Tracks:
  - New servers the bot joins
  - Every command executed
  - Every server selected using `$join`

- ⛔ **Protected servers**  
  SAFE_GUILDS prevents nuking or selecting specific servers.

- ⏳ **Auto-leave system**  
  If added to a random server, the bot automatically leaves after 5 minutes.

---

## 🛠️ **Technologies Used**

- Python 3
- Nextcord
- asyncio
- aiohttp
- requests
- fade (console visual effects)

---

## 📌 **Initial Setup**

Edit these variables inside `bot.py`:

```python
TOKEN = "YOUR_BOT_TOKEN"
PREFIX = "$"

MAIN_GUILD_ID = 123456789
INVITE_CHANNEL_ID = 123456789
LOG_GUILD_ID = 123456789

SAFE_GUILDS = [ID1, ID2]
```

Make sure the bot has **Administrator** permissions in servers where commands will be used.

---

## 📂 **Available Commands**

### 🔰 Basic
```
$join <id>        Select a server
$status           Show current selected server
$help             Display command list
```

### 💣 Raid & Nuke
```
$nuke             Full server destruction
$spam             Massive multi-channel spam
$delc             Delete all channels
$crc <num>        Create channels
$banall           Ban all members
$kickall          Kick all members
$renameall <txt>  Rename all members
```

### 🛑 Roles & Permissions
```
$admin            Gives yourself admin
$eliminarroles    Delete all roles
$crearroles <n>   Create roles
```

### ⚙️ Extras
```
$steal <vanity>   Steal vanity URL (if possible)
$lockall          Lock all channels
$unlockall        Unlock all channels
$massdm <msg>     DM all members
$leave            Bot leaves server
$bypasscmd        Rename everything + spam
```

---

## 📝 Notes

- The bot **only works via DMs** thanks to the `@solo_dm()` decorator.
- Logging requires the bot to be inside your log guild.
- Auto-leave prevents unwanted permanent server joins.

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.  
Improper use may violate Discord's Terms of Service.  
The author (**xfsc**) is not responsible for how this bot is used.

---

## ⭐ Credits

Developed entirely by **xfsc**, with console aesthetics powered by `fade`.

