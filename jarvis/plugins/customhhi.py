from jarvis.utils import admin_cmd


@jarvis.on(admin_cmd(pattern=r".hhi<space><emoji><space><emoji>)"))
async def hhi(event):
    giveVar = event.text
    cat = giveVar[5:6]
    if not cat:
        cat = "🌺"
    ct = giveVar[7:8]
    if not ct:
        ct = "✨"
    await event.edit(
        f"{cat}{ct}{ct}{cat}{ct}{cat}{cat}{cat}\n{cat}{ct}{ct}{cat}{ct}{ct}{cat}{ct}\n{cat}{cat}{cat}{cat}{ct}{ct}{cat}{ct}\n{cat}{ct}{ct}{cat}{ct}{ct}{cat}{ct}\n{cat}{ct}{ct}{cat}{ct}{cat}{cat}{cat}\n☁☁☁☁☁☁☁☁"
    )