import telegram
from telethon import TelegramClient
from telethon import events
import time
default = 0

API_id = "12349102"
API_HASH = "083cbe233de54ccbaabf515b7de5290f"
client = TelegramClient(f"Psycho", int(API_id), API_HASH)

@client.on(events.NewMessage(chats = "https://t.me/Acidonmeliketheraincalls"))
async def event_handler(event):
    global default
    new_post = event.id
    default == new_post
    print(new_post)
    tg_link = f"https://t.me/Acidonmeliketheraincalls/{new_post}"
    await client.send_message(entity= "@ViewBoosterBot", message= tg_link)
    time.sleep(10)
    await client.send_message(entity="@gentlespree", message=f"{tg_link}")
    print("sent")
    default = 0

client.start()
client.run_until_disconnected()