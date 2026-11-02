import functions.call_function

async def help(client, message, content):
    new_content = "help_" + content.strip().lower()
    called = await functions.call_function.call_function(
        client, message, new_content
    )
    if not called:  # send default help message
        text = """# Hello! I am **Missu**, Kissu's bot for personal use made with discord.py.
The prefix to use me is '**uwu**' (or '**уву**') - use it every time you want to call me!

Here are some of my commands:

**Music**: play, pause, resume, skip, stop, queue, push, playnum, shuffle, repeat, link.
Run **uwu help music** for more info!

**Playlists and favlist**: save songs and organize them into playlists.
Run **uwu help playlists** or **uwu help favlist** for more info!

**Lyrics**: search for song lyrics using Genius.
Run **uwu help lyrics** for more info!

**AI**: ask AI models questions, or use DeepSeek with web search.
Run **uwu help ai** for more info!

**Reactions and replies**: make me react to messages or automatically reply to certain phrases.
Run **uwu help react** or **uwu help reply** for more info!

**Misc.**: ping, choose.
Run **uwu help misc** for more info!

**Owner only**: shutdown, gitpush, perms set.
**Admin only**: reboot.

You can also use command aliases:
- **next** = skip
- **playfav** = play favlist
- **pl** = playlist
- **pld** = playlistdefault
- **текст** = lyrics
- **ии** = ai
- **deepseek / дипсик** = ai_deep
- **ссылка** = link
- **gamba / gamble** = choose
- **reaction** = react

Try **uwu help [category]** to learn more about a specific feature!"""
        await message.channel.send(text)

async def help_music(message):
    text = """# Play music from YouTube!
Note: you must be in a voice channel to run these commands.
If I'm already playing music, new songs will be added to the queue.

1. **Uwu play [source]** - play song(s) from a YouTube search prompt, video link, or playlist link.
Example: **uwu play Toram Online BGM - King Piton**
Note: this might take a while for large playlists!

You can add **-s** to shuffle the songs before adding them to the queue.
Example: **uwu play <https://www.youtube.com/playlist?list=PL43syiOjn5rQ6Bj0EP4CV2fWvCM0WifLD> -s**

You can also use **-select** to choose a song from search results instead of playing the first match.
Example: **uwu play Toram Online BGM -select**
By default, 5 results are shown. You can specify another number:
**uwu play Toram Online BGM -select 10**

2. **Uwu pause**, **uwu resume** - pause/resume playback.
3. **Uwu skip** (or **uwu next**) - skip the current song.
4. **Uwu stop** - stop playback, disconnect from the voice channel and clear the queue.
5. **Uwu queue** - view the current queue.
Use **uwu queue remove [index]** to remove a song from the queue.
Example: **uwu queue remove 3**
Use **uwu queue remove last** to remove the last song.

6. **Uwu push [index]** - move a song in the queue to the next position.
Example: **uwu push 5** - move song number 5 to position 2.
**Uwu push last** will push the last song instead.
You can also use **uwu push [source]** to add song(s) to the queue and play them next.

7. **Uwu playnum [index]** - play a song from the queue immediately, skipping the current one.
**Uwu playnum last** will play the last song immediately.

8. **Uwu shuffle** - shuffle the queue.
9. **Uwu repeat** - play the current song once again after it finishes.
10. **Uwu link** (or **uwu ссылка**) - get a link to the currently playing song.
11. **Uwu play np** - add the currently playing song to the queue.

Run **uwu help favlist** or **uwu help playlists** for info about saved music!"""
    await message.channel.send(text)

async def help_favlist(message):
    text = """# Save songs to your favourite music list and play them quickly and easily!

1. **Uwu favlist** - view your favlist.
2. **Uwu favlist add [source]** - add a song to your favlist using a YouTube search prompt or link.
Playlists are not supported.
3. **Uwu favlist add np** - add the currently playing song to your favlist.
4. **Uwu favlist remove [index]** - remove a song by its index.
Example: **uwu favlist remove 3**
5. **Uwu favlist clear** - remove all songs from your favlist.
6. **Uwu play favlist** (or **uwu playfav**) - add all songs from your favlist to the queue and play them.
If music is already playing, songs will be added to the queue.

Specify **-s** to shuffle the songs:
**uwu play favlist -s**

Note: this is faster than using YouTube playlists!"""
    await message.channel.send(text)

async def help_playlists(message):
    text = """# Save songs to your own playlists and play them easily!

1. **Uwu playlist create [name]** - create a new playlist.
Example: **uwu playlist create Three Days Grace**

2. **Uwu playlist delete [name]** - delete a playlist.

3. **Uwu playlist add [name] [source]** (or **uwu pl add ...**) - add a song or songs to a playlist.
The source can be a YouTube search prompt, video link, or playlist link.
Use **np** to add the currently playing song.
Example: **uwu playlist add Three Days Grace np**

You can also use **uwu playlist + [name] [source]**.

4. **Uwu playlist remove [name] [index]** - remove a song from a playlist.
You can also use **uwu playlist - [name] [index]**.
Example: **uwu playlist remove Three Days Grace 2**

5. **Uwu playlist show [name]** - view the songs in a playlist.
6. **Uwu playlist showall** - view all your playlists.

7. **Uwu playlist play [name]** - add all songs from a playlist to the queue and play them.
8. **Uwu playlist push [name]** - add all songs from a playlist to the queue and play them next.

Add **-s** to shuffle the playlist:
**uwu playlist play Three Days Grace -s**

9. **Uwu playlistdefault set [name]** - set your default playlist.
After that, you can use playlist commands without specifying its name.

Examples:
**uwu playlistdefault play**
**uwu playlistdefault show**
**uwu playlistdefault add Never Too Late**

Use **uwu pld set [name]** as a shorter alias for setting the default playlist.

Note: playlists are personal to each user."""
    await message.channel.send(text)

async def help_lyrics(message):
    text = """# Find song lyrics using Genius!

1. **Uwu lyrics [song name]** - search for a song on Genius.
Example: **uwu lyrics Never Too Late Three Days Grace**

2. **Uwu lyrics np** - search for lyrics of the currently playing song.

You can also use the Russian alias **uwu текст**.

Note: Missu searches Genius and attempts to retrieve the lyrics automatically.
If the lyrics cannot be retrieved, a link to the Genius page may still be available."""
    await message.channel.send(text)

async def help_ai(message):
    text = """# Chat with AI models!

1. **Uwu ai [prompt]** (or **uwu ии [prompt]**) - send a prompt to an AI model.
Missu can use several models through OpenRouter.

2. **Uwu ai_deep [prompt]** (or **uwu deepseek [prompt]**) - ask DeepSeek with web search enabled.
You can also use **uwu дипсик**.

Note: AI responses may take some time. Always verify important information and be careful with links provided by AI."""
    await message.channel.send(text)

async def help_react(message):
    text = """# Make Missu react to messages automatically!

1. **Uwu react add [text] = [emoji]** - add a personal reaction.
Whenever a message contains the specified text, Missu will react with the selected emoji.
Example: **uwu react add hello = 👋**

2. **Uwu react remove [text]** - remove one of your reactions.
3. **Uwu react list** - view your personal reactions.

Administrators can also manage global reactions:

4. **Uwu react add [text] = [emoji] all** - add a reaction that applies to everyone.
5. **Uwu react remove [text] all** - remove a global reaction.
6. **Uwu react listall** - view all global reactions.

Note: global reaction management is available to administrators only.
You can also use **uwu reaction** instead of **uwu react**."""
    await message.channel.send(text)

async def help_reply(message):
    text = """# Make Missu reply to messages automatically!

1. **Uwu reply add [text] = [response]** - add a personal automatic reply.
Whenever a message contains the specified text, Missu will send the response.
Example: **uwu reply add good morning = Good morning!**

2. **Uwu reply remove [text]** - remove one of your automatic replies.
3. **Uwu reply list** - view your personal replies.

Administrators can also manage global replies:

4. **Uwu reply add [text] = [response] all** - add a reply that applies to everyone.
5. **Uwu reply remove [text] all** - remove a global reply.
6. **Uwu reply listall** - view all global replies.

Note: global reply management is available to administrators only."""
    await message.channel.send(text)

async def help_misc(message):
    text = """# Miscellaneous commands!

1. **Uwu ping** - check Missu's response time.
2. **Uwu choose [item 1], [item 2], ...** - choose a random item from the provided list.
Example: **uwu choose pizza, sushi, burger**

You can also assign probabilities:
**uwu choose pizza 70%, sushi 20%, burger**
The remaining probability is distributed equally among items without a specified percentage.

You can save reusable lists:

3. **Uwu choose create [list name] = [items]** - create a list.
Example: **uwu choose create dinner = pizza, sushi, burger**

4. **Uwu choose add [list name] [items]** - add items to a saved list.
5. **Uwu choose remove [list name] [items]** - remove items from a saved list.
6. **Uwu choose show** - show your saved lists.

To choose from a saved list, use its name:
**uwu choose dinner**

You can temporarily add or remove items when choosing:
**uwu choose dinner + pasta - sushi**"""
    await message.channel.send(text)

async def help_admin(message):
    text = """# Administration commands!

1. **Uwu perms set [user] [access_level]** - change a user's access level.
Example: **uwu perms set @User admin**
Available levels: **default**, **admin** (or **administrator**).
This command is owner-only.

2. **Uwu reboot** - restart Missu.
Available to administrators only.

3. **Uwu gitpush** - upload local changes to GitHub.
This command is owner-only.

4. **Uwu shutdown** - shut down Missu.
This command is owner-only.

Note: use these commands with care!"""
    await message.channel.send(text)