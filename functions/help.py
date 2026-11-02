import functions.call_function

async def help(client, message, content) :
    new_content = "help_" + content
    called = await functions.call_function.call_function(client, message, new_content)
    if not called : #send default help message
        text = """# Hello! I am **Missu**, Kissu's bot for personal use made with discord.py. 
The prefix to use me is '**uwu**' (or '**уву**') - use it every time you want to call me!
Here are some of my commands:
Main block - **Music**: play, stop, pause, push, playnum, repeat, etc. - run "uwu help music" for info!
**Misc.**: ping
**Owner only**: shutdown, gitpush, perms set. 
Try: uwu help [category] for help with specific commands (such as: **uwu help alias**)."""
        await message.channel.send(text)

async def help_music(message):
    text = """# Play music from YouTube! Note: you must be in a voice channel to run these commands.
Note: If I'm already playing music, then the "play" command will just add song(s) to the queue.
1. **Uwu play [source]** - play song(s) from a specified source (YouTube search prompt, YouTube video link, or YouTube playlist link)
Example: uwu play Toram Online BGM - King Piton
Note: This might take a while for large playlists!
Specifying a '-s' key will shuffle the songs in playlist (if the source is a YouTube playlist link).
Example: uwu play <https://www.youtube.com/playlist?list=PL43syiOjn5rQ6Bj0EP4CV2fWvCM0WifLD> -s
2. **Uwu pause**, **uwu resume** - pausing/resuming playback. 
**uwu skip** - skipping the current song and playing the next one.
**uwu stop** - stop the playback and delete the queue.
3. **Uwu queue** - view the queue.
4. **Uwu push [index]** - specify a song in queue which you want to play next. 
For example, if the 5th song in queue is "Toram Online BGM - King Piton", then "**uwu push 5**" will make it play next (become number 2 in the queue).
**Uwu push last** will push the last song in the queue instead.
**Uwu push [source]** will add song(s) to queue and play them next.
5. **Uwu playnum [index]** - specify a song in queue you want to play right now. The current song will be skipped.
**Uwu playnum last** will play the last song in the queue immediately.
6. **Uwu shuffle** - shuffle the queue.

Run **uwu help favlist** for info about music favlists!"""
    await message.channel.send(text)

async def help_favlist(message):
    text = """# Save songs to your favourite music list and play them quickly and easily!
1. **Uwu favlist** - view your favlist.
2. **Uwu favlist add [source]** - add a song from a specified source to your favlist. Playlists are not supported.
3. **Uwu favlist remove [index]** - remove the song with the specified index from your favlist.
Example: **uwu favlist remove 3** - this will remove the 3rd song from your favlist
4. **Uwu play favlist** - create a queue from your favlist and play it! (Or add everything from your favlist to the queue if already playing)
Note: specify a '-s' key to play or add your favlist songs in a random order: **uwu play favlist -s**
Note: **this is faster than using YouTube playlists!**"""
    await message.channel.send(text)