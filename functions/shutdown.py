from auto_git_push import sync_to_github
from functions.check_owner import check_owner
from classes.user import User
async def shutdown(client, message, admin_allow = False):
    if await check_owner(message) == 1 or (admin_allow and User(message.author.id).perms == "administrator"):
        await sync_to_github(message, admin_allow)
        await message.channel.send("Shutting down...")
        await client.close()
    else:
        await message.channel.send("Command restricted to be executed by the bot owner only.")
        
    