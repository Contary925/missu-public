
import functions.call_function


async def help(client, message, content):
    new_content = "help_" + content.strip().lower()
    called = await functions.call_function.call_function(
        client, message, new_content
    )

    if not called:
        text = """# Hello! I'm **Missu**, Kissu's bot for personal use made with discord.py.
Use **uwu** (or **уву**) as my command prefix.

**Music:** `play`, `pause`, `resume`, `skip`, `stop`, `queue`, `push`, `playnum`, `shuffle`, `repeat`, `link`.
→ `uwu help music`

**Playlists & favlist:** save, organize and play your music.
→ `uwu help playlists` | `uwu help favlist`

**Lyrics:** search for song lyrics using Genius.
→ `uwu help lyrics`

**AI:** chat with AI models or use DeepSeek with web search.
→ `uwu help ai`

**Reactions & replies:** automatic reactions and responses to messages.
→ `uwu help react` | `uwu help reply`

**Misc:** `ping`, `choose`.
→ `uwu help misc`

**Owner:** `shutdown`, `gitpush`, `perms set`.
**Admin:** `reboot`.

**Aliases:** `next` = `skip` · `playfav` = `play favlist` · `pl` = `playlist` · `pld` = `playlistdefault` · `текст` = `lyrics` · `ии` = `ai` · `deepseek` / `дипсик` = `ai_deep` · `ссылка` = `link` · `gamba` / `gamble` = `choose` · `reaction` = `react`.

Use **uwu help [category]** for more information!"""
        await message.channel.send(text)


async def help_music(message):
    text = """# Play music from YouTube!
You must be in a voice channel to use these commands. If music is already playing, new songs will be added to the queue.

1. `uwu play [source]` — play songs from a YouTube search, video link or playlist link.
   Example: `uwu play Toram Online BGM - King Piton`
   Add `-s` to shuffle the results: `uwu play [source] -s`.

2. `uwu play [prompt] -select [count]` — choose a song from search results instead of playing the first match.
   By default, 5 results are shown; you can request up to 10.
   Example: `uwu play Toram Online BGM -select 10`.

3. `uwu pause` / `uwu resume` — pause or resume playback.
4. `uwu skip` (or `uwu next`) — skip the current song.
5. `uwu stop` — stop playback, disconnect and clear the queue.
6. `uwu queue` — view the queue. Use `uwu queue remove [index]` or `uwu queue remove last` to remove a song.

7. `uwu push [index]` — move a queued song to the next position.
   Use `uwu push last` to move the last song, or `uwu push [source]` to add new songs to the front of the queue.

8. `uwu playnum [index]` — play a queued song immediately, skipping the current one. Also supports `last`.
9. `uwu shuffle` — shuffle the queue.
10. `uwu repeat` — play the current song once again after it finishes.
11. `uwu link` (or `uwu ссылка`) — get a link to the currently playing song.
12. `uwu play np` — add the currently playing song to the queue.

For saved music, see `uwu help favlist` or `uwu help playlists`."""
    await message.channel.send(text)


async def help_favlist(message):
    text = """# Save songs to your favourite music list!
1. `uwu favlist` — view your favlist.
2. `uwu favlist add [source]` — add a song using a YouTube search prompt or video link. Playlist links are not supported.
3. `uwu favlist add np` — add the currently playing song.
4. `uwu favlist remove [index]` — remove a song by its index.
   Example: `uwu favlist remove 3`.
5. `uwu favlist clear` — remove all songs from your favlist.
6. `uwu play favlist` (or `uwu playfav`) — add all saved songs to the queue.
   Add `-s` to shuffle them: `uwu play favlist -s`.

If music is already playing, saved songs will be added to the queue. Note: this is faster than using YouTube playlists!"""
    await message.channel.send(text)


async def help_playlists(message):
    text = """# Save songs to your own playlists!
1. `uwu playlist create [name]` — create a new playlist.
   Example: `uwu playlist create Three Days Grace`.
2. `uwu playlist delete [name]` — delete a playlist.
3. `uwu playlist add [name] [source]` — add songs from a YouTube search, video link or playlist link.
   Use `np` to add the currently playing song. Example: `uwu playlist add Three Days Grace np`.
   Short form: `uwu playlist + [name] [source]`.
4. `uwu playlist remove [name] [index]` — remove a song. Short form: `uwu playlist - [name] [index]`.
5. `uwu playlist show [name]` — view a playlist.
6. `uwu playlist showall` — view all your playlists.
7. `uwu playlist play [name]` — add playlist songs to the queue.
8. `uwu playlist push [name]` — add playlist songs to the front of the queue.
   Add `-s` to shuffle: `uwu playlist play Three Days Grace -s`.

**Default playlist:** use `uwu playlistdefault set [name]` to set one.
After that, you can omit the playlist name in commands:
`uwu playlistdefault play`, `uwu playlistdefault show`, `uwu playlistdefault add [source]`, etc.
Short alias: `uwu pld set [name]`.

Playlists are personal to each user."""
    await message.channel.send(text)


async def help_lyrics(message):
    text = """# Find song lyrics using Genius!
1. `uwu lyrics [song name]` — search for a song on Genius.
   Example: `uwu lyrics Never Too Late Three Days Grace`.
2. `uwu lyrics np` — search for lyrics of the currently playing song.

You can also use the Russian alias `uwu текст`.
Missu attempts to retrieve the lyrics automatically. If that fails, a link to the Genius page may still be available."""
    await message.channel.send(text)


async def help_ai(message):
    text = """# Chat with AI models!
1. `uwu ai [prompt]` (or `uwu ии [prompt]`) — send a prompt to an AI model.
   Missu can use several models through OpenRouter.
2. `uwu ai_deep [prompt]` (or `uwu deepseek [prompt]`) — ask DeepSeek with web search enabled.
   You can also use `uwu дипсик`.

AI responses may take some time. Always verify important information and be careful with links provided by AI."""
    await message.channel.send(text)


async def help_react(message):
    text = """# Make Missu react to messages automatically!
1. `uwu react add [text] = [emoji]` — add a personal reaction.
   Whenever a message contains the specified text, Missu reacts with the selected emoji.
   Example: `uwu react add hello = 👋`.
2. `uwu react remove [text]` — remove one of your reactions.
3. `uwu react list` — view your personal reactions.

**Global reactions (administrators only):**
4. `uwu react add [text] = [emoji] all` — add a reaction for everyone.
5. `uwu react remove [text] all` — remove a global reaction.
6. `uwu react listall` — view all global reactions.

You can also use `uwu reaction` instead of `uwu react`."""
    await message.channel.send(text)


async def help_reply(message):
    text = """# Make Missu reply to messages automatically!
1. `uwu reply add [text] = [response]` — add a personal automatic reply.
   Whenever a message contains the specified text, Missu sends your response.
   Example: `uwu reply add good morning = Good morning!`.
2. `uwu reply remove [text]` — remove one of your replies.
3. `uwu reply list` — view your personal replies.

**Global replies (administrators only):**
4. `uwu reply add [text] = [response] all` — add a reply for everyone.
5. `uwu reply remove [text] all` — remove a global reply.
6. `uwu reply listall` — view all global replies."""
    await message.channel.send(text)


async def help_misc(message):
    text = """# Miscellaneous commands!
1. `uwu ping` — check Missu's response time.
2. `uwu choose [item 1], [item 2], ...` — choose a random item.
   Example: `uwu choose pizza, sushi, burger`.
   You can assign probabilities: `uwu choose pizza 70%, sushi 20%, burger`.
   The remaining probability is distributed equally among items without a specified percentage.

**Saved lists:**
3. `uwu choose create [name] = [items]` — create a reusable list.
   Example: `uwu choose create dinner = pizza, sushi, burger`.
4. `uwu choose add [name] [items]` — add items to a saved list.
5. `uwu choose remove [name] [items]` — remove items from a saved list.
6. `uwu choose show` — view your saved lists.
7. `uwu choose [name]` — choose from a saved list.
   You can temporarily add or remove items: `uwu choose dinner + pasta - sushi`.

Aliases: `uwu gamba` and `uwu gamble` both work as `uwu choose`."""
    await message.channel.send(text)


async def help_admin(message):
    text = """# Administration commands!
1. `uwu perms set [user] [access_level]` — change a user's access level.
   Example: `uwu perms set @User admin`.
   Available levels: `default`, `admin` (or `administrator`). Owner only.
2. `uwu reboot` — restart Missu. Available to administrators.
3. `uwu gitpush` — upload local changes to GitHub. Owner only.
4. `uwu shutdown` — shut down Missu. Owner only.

Use these commands with care!"""
    await message.channel.send(text)
