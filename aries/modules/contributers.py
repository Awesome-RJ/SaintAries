import github
from pyrogram import filters
from aries import pbot as app


@app.on_message(filters.command("repo") & ~filters.edited)
async def give_repo(c, m):
    g = github.Github()
    repo = g.get_repo("idzero23/SaintAries")
    list_of_users = "".join(
        f"*{count}.* [{i.login}](https://github.com/{i.login})\n"
        for count, i in enumerate(repo.get_contributors(), start=1)
    )

    text = f"""[Github](https://github.com/idzero23/SaintAries) | [support group](https://t.me/idzeroidsupport)
```----------------
| Contributors |
----------------```
{list_of_users}"""
    await m.reply(text, disable_web_page_preview=False)


__mod_name__ = "REPO"
