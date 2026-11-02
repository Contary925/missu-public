# Missu

**Missu** is a personal Discord bot built with [discord.py](https://discordpy.readthedocs.io/). It combines music playback, playlists, automatic reactions and replies, AI chat, and a few miscellaneous utilities.

The bot is designed primarily for personal use.

## Features

- **Music playback** — search and play songs from YouTube, manage the queue, shuffle tracks, and repeat songs.
- **Playlists and favourites** — save tracks, organize them into personal playlists, and quickly add them to the queue.
- **Lyrics** — search for song lyrics using the Genius API.
- **AI chat** — interact with several AI models through OpenRouter, including DeepSeek with web search.
- **Automatic reactions and replies** — configure personal or global triggers for messages.
- **Utilities** — random choice with custom probabilities, saved choice lists, and more.
- **GitHub synchronization** — automatically pull updates on startup and push local changes when requested.

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/)
- [Git](https://git-scm.com/)
- [FFmpeg](https://ffmpeg.org/) (required for music playback)
- A Discord bot application and token

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Contary925/missu-public.git
   cd missu-public
   ```

2. Install the project dependencies:

   ```bash
   uv sync
   ```

3. Install FFmpeg and make sure it is available in your system PATH.

4. Create a `.env` file in the project root:

   ```env
   DISCORD_TOKEN=your_discord_bot_token
   OPENROUTER_API_KEY=your_openrouter_api_key
   GENIUS_ACCESS_TOKEN=your_genius_access_token
   ```

   `DISCORD_TOKEN` is required. The other API keys are optional and enable their respective features.

5. Create `shared/ID.py` locally:

   ```python
   OWNER_ID = 123456789012345678
   ```

   Replace the example value with your Discord user ID. This file is intentionally excluded from the public repository.

6. Enable the **Message Content Intent** in the Discord Developer Portal under your bot's settings.

## Running

Start the bot with:

```bash
uv run main.py
```

Missu will automatically attempt to pull the latest changes from the `main` branch on startup. Ignore this if you aren't using a git remote.

## Configuration

| Variable | Required | Description |
|---|---|---|
| `DISCORD_TOKEN` | Yes | Discord bot token |
| `OPENROUTER_API_KEY` | No | Enables AI commands |
| `GENIUS_ACCESS_TOKEN` | No | Enables lyrics search |

The bot owner is configured separately in `shared/ID.py` using `OWNER_ID`.

## Commands

All commands use the `uwu` prefix. The alternative prefix `уву` is also supported.

| Category | Commands |
|---|---|
| Music | `play`, `pause`, `resume`, `skip`, `stop`, `queue`, `push`, `playnum`, `shuffle`, `repeat`, `link` |
| Playlists | `playlist`, `playlistdefault` |
| Favourites | `favlist`, `playfav` |
| Lyrics | `lyrics` |
| AI | `ai`, `ai_deep` |
| Reactions | `react` |
| Automatic replies | `reply` |
| Miscellaneous | `ping`, `choose` |
| Administration | `reboot`, `shutdown`, `gitpush`, `perms` |

For detailed command usage, run:

```text
uwu help
uwu help [category]
```

## GitHub Synchronization

Missu includes a small Git-based synchronization workflow:

- `auto_git_pull.py` attempts to pull the latest changes from `origin/main` when the bot starts.
- `gitpush` uploads local changes to GitHub.
- `shutdown` attempts to synchronize local changes before shutting down.

The synchronization commands require a properly configured Git repository and working Git credentials.
Ignore these if you aren't using a git remote.

**Note:** the automatic push uses `git add .`, so make sure that sensitive files and local-only configuration are properly excluded through `.gitignore`.

## Notes

- This is a personal project, so some configuration files and credentials are intentionally not included in the repository.
- Music playback depends on external services and may be affected by changes to YouTube or yt-dlp.
- AI responses should be checked before relying on them, especially for important information.