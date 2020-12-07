import asyncio
from datetime import datetime

from userbot.utils import admin_cmd, sudo_cmd

userthumb = "./resources/541200.png"


@borg.on(admin_cmd(pattern="lsend ?(.*)"))
@borg.on(sudo_cmd(pattern="lsend ?(.*)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    end = datetime.now()
    (end - start).seconds
    men = f"Plugin Name - {input_str}.py \nUploaded By Lightning"
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        thumb=userthumb,
        caption=men,
        force_document=True,
        allow_cache=False,
        reply_to=message_id,
    )
    await asyncio.sleep(5)
    await event.delete()
