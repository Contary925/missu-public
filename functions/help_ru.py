
import functions.call_function


async def help_ru(client, message, content):
    new_content = "help_ru_" + content.strip().lower()
    called = await functions.call_function.call_function(
        client, message, new_content
    )

    if not called:
        text = """# Привет! Я **Missu**, личный Discord-бот Kissu, написанный на discord.py.
Используй префикс **uwu** (или **уву**), чтобы вызвать мою команду.

**Музыка:** `play`, `pause`, `resume`, `skip`, `stop`, `queue`, `push`, `playnum`, `shuffle`, `repeat`, `link`.
→ `уву помощь музыка`

**Плейлисты и избранное:** сохраняй, сортируй и воспроизводи музыку.
→ `уву помощь плейлисты` | `уву помощь фавлист`

**Тексты песен:** поиск текстов через Genius.
→ `уву помощь текст`

**ИИ:** общение с разными моделями и DeepSeek с веб-поиском.
→ `уву помощь ии`

**Реакции и ответы:** автоматические реакции и ответы на сообщения.
→ `уву помощь реакции` | `уву помощь ответы`

**Разное:** `ping`, `choose`.
→ `уву помощь разное`

**Только владелец:** `shutdown`, `gitpush`, `perms set`.
**Администраторы:** `reboot`.
→ `уву помощь админ`

**Алиасы:** `next` = `skip` · `playfav` = `play favlist` · `pl` = `playlist` · `pld` = `playlistdefault` · `текст` = `lyrics` · `ии` = `ai` · `deepseek` / `дипсик` = `ai_deep` · `ссылка` = `link` · `gamba` / `gamble` = `choose` · `reaction` = `react`.

Русскую справку также можно вызвать командами `уву помощь`, `уву хелп` или `уву справка`.
Сами команды Missu по-прежнему используют английские названия!"""
        await message.channel.send(text)


async def help_ru_music(message):
    text = """# Воспроизведение музыки с YouTube!
Для использования этих команд нужно находиться в голосовом канале. Если музыка уже играет, новые песни будут добавляться в очередь.

1. `uwu play [source]` — воспроизвести песни из поискового запроса YouTube, по ссылке на видео или плейлист.
   Пример: `uwu play Toram Online BGM - King Piton`.
   Добавь `-s`, чтобы перемешать результаты: `uwu play [source] -s`.

2. `uwu play [prompt] -select [count]` — выбрать песню из результатов поиска вместо автоматического выбора первого совпадения.
   По умолчанию показываются 5 результатов, можно запросить до 10.
   Пример: `uwu play Toram Online BGM -select 10`.

3. `uwu pause` / `uwu resume` — приостановить или возобновить воспроизведение.
4. `uwu skip` (или `uwu next`) — пропустить текущую песню.
5. `uwu stop` — остановить воспроизведение, отключиться от голосового канала и очистить очередь.
6. `uwu queue` — показать очередь. Используй `uwu queue remove [index]` или `uwu queue remove last`, чтобы удалить песню.
7. `uwu push [index]` — переместить песню из очереди на следующую позицию.
   `uwu push last` переместит последнюю песню, а `uwu push [source]` добавит новые песни в начало очереди.
8. `uwu playnum [index]` — немедленно воспроизвести песню из очереди, пропустив текущую. Также поддерживается `last`.
9. `uwu shuffle` — перемешать очередь.
10. `uwu repeat` — повторно воспроизвести текущую песню после её завершения.
11. `uwu link` (или `uwu ссылка`) — получить ссылку на текущую песню.
12. `uwu play np` — добавить текущую песню в очередь.

Missu поддерживает личные музыкальные коллекции:
- `uwu favlist` — управление избранными песнями.
- `uwu playlist` — создание, управление и обмен плейлистами.

Подробнее: `уву помощь фавлист` и `уву помощь плейлисты`."""
    await message.channel.send(text)


async def help_ru_favlist(message):
    text = """# Сохраняй любимые песни в избранное!
1. `uwu favlist` — посмотреть своё избранное.
2. `uwu favlist add [source]` — добавить песню по поисковому запросу YouTube или ссылке на видео. Ссылки на плейлисты не поддерживаются.
3. `uwu favlist add np` — добавить текущую песню.
4. `uwu favlist remove [index]` — удалить песню по её номеру.
   Пример: `uwu favlist remove 3`.
5. `uwu favlist clear` — очистить избранное.
6. `uwu play favlist` (или `uwu playfav`) — добавить все сохранённые песни в очередь.
   Добавь `-s`, чтобы перемешать их: `uwu play favlist -s`.

**Музыка других пользователей:**
7. `uwu favlist browse [@user]` — посмотреть избранное другого пользователя.
   Вместо упоминания можно использовать личный алиас.

**Настройки видимости:**
8. `uwu playlist visibility on` — разрешить другим пользователям просматривать твои плейлисты и избранное.
9. `uwu playlist visibility off` — запретить другим пользователям просматривать твои плейлисты и избранное.

По умолчанию видимость отключена. Просматривать чужие музыкальные коллекции можно только с разрешения их владельца.

Если музыка уже играет, сохранённые песни просто добавятся в очередь."""
    await message.channel.send(text)


async def help_ru_playlists(message):
    text = """# Создавай собственные плейлисты!
**Свои плейлисты:**
- `uwu playlist create [name]` / `delete [name]` — создать или удалить плейлист.
- `uwu playlist add [name] [source]` — добавить песни из поиска YouTube, по ссылке на видео или плейлист. Используй `np`, чтобы добавить текущую песню. Короткая форма: `+`.
- `uwu playlist remove [name] [index]` — удалить песню по номеру. Короткая форма: `-`.
- `uwu playlist show [name]` — посмотреть плейлист.
- `uwu playlist showall` — показать свои плейлисты.
- `uwu playlist play [name]` / `push [name]` — добавить песни в очередь или её начало. Добавь `-s` для перемешивания.

**Чужие плейлисты:**
- `uwu playlist browse [@user]` — посмотреть плейлисты пользователя. Добавь `= [playlist name]`, чтобы открыть конкретный.
- `uwu playlist copy [@user] = [playlist name]` — скопировать плейлист. Добавь `AS [new name]`, чтобы переименовать копию.
- Вместо упоминаний можно использовать личные алиасы.

**Видимость:**
- `uwu playlist visibility on` / `off` — разрешить или запретить просмотр своих плейлистов и избранного.
- По умолчанию видимость отключена. Без разрешения просматривать и копировать твои коллекции нельзя.

**Плейлист по умолчанию:**
- `uwu playlistdefault set [name]` (или `uwu pld set [name]`) — выбрать плейлист по умолчанию.
- Используй `uwu playlistdefault [command]`, чтобы не указывать его название: например, `play`, `show`, `add`.

Копирование чужих плейлистов не изменяет оригинал."""
    await message.channel.send(text)


async def help_ru_lyrics(message):
    text = """# Поиск текстов песен через Genius!
1. `uwu lyrics [song name]` — найти песню на Genius.
   Пример: `uwu lyrics Never Too Late Three Days Grace`.
2. `uwu lyrics np` — найти текст текущей песни.

Также можно использовать русский алиас `uwu текст`.
Missu попытается автоматически получить текст песни. Если это не удастся, ссылка на страницу Genius всё равно может быть доступна."""
    await message.channel.send(text)


async def help_ru_ai(message):
    text = """# Общение с ИИ!
1. `uwu ai [prompt]` (или `uwu ии [prompt]`) — отправить запрос ИИ-модели.
   Missu может использовать несколько моделей через OpenRouter.
2. `uwu ai_deep [prompt]` (или `uwu deepseek [prompt]`) — обратиться к DeepSeek с включённым веб-поиском.
   Также можно использовать `uwu дипсик`.

Ответы ИИ могут занимать некоторое время. Проверяй важную информацию самостоятельно и осторожно переходи по ссылкам, которые предоставляет модель."""
    await message.channel.send(text)


async def help_ru_react(message):
    text = """# Настрой автоматические реакции Missu!
1. `uwu react add [text] = [emoji]` — добавить личную реакцию.
   Если сообщение содержит указанный текст, Missu поставит выбранную реакцию.
   Пример: `uwu react add hello = 👋`.
2. `uwu react remove [text]` — удалить одну из своих реакций.
3. `uwu react list` — посмотреть свои реакции.

**Глобальные реакции (только для администраторов):**
4. `uwu react add [text] = [emoji] all` — добавить реакцию для всех пользователей.
5. `uwu react remove [text] all` — удалить глобальную реакцию.
6. `uwu react listall` — посмотреть все глобальные реакции.

Вместо `uwu react` также можно использовать `uwu reaction`."""
    await message.channel.send(text)


async def help_ru_reply(message):
    text = """# Настрой автоматические ответы Missu!
1. `uwu reply add [text] = [response]` — добавить личный автоматический ответ.
   Если сообщение содержит указанный текст, Missu отправит заданный ответ.
   Пример: `uwu reply add good morning = Good morning!`.
2. `uwu reply remove [text]` — удалить один из своих ответов.
3. `uwu reply list` — посмотреть свои ответы.

**Глобальные ответы (только для администраторов):**
4. `uwu reply add [text] = [response] all` — добавить ответ для всех пользователей.
5. `uwu reply remove [text] all` — удалить глобальный ответ.
6. `uwu reply listall` — посмотреть все глобальные ответы."""
    await message.channel.send(text)


async def help_ru_misc(message):
    text = """# Разные команды!
1. `uwu ping` — проверить время отклика Missu.
2. `uwu choose [item 1], [item 2], ...` — выбрать случайный вариант.
   Пример: `uwu choose pizza, sushi, burger`.
   Можно задавать вероятности: `uwu choose pizza 70%, sushi 20%, burger`.
   Оставшаяся вероятность поровну распределяется между вариантами без указанного процента.

**Сохранённые списки:**
3. `uwu choose create [name] = [items]` — создать список для повторного использования.
   Пример: `uwu choose create dinner = pizza, sushi, burger`.
4. `uwu choose add [name] [items]` — добавить варианты в сохранённый список.
5. `uwu choose remove [name] [items]` — удалить варианты из сохранённого списка.
6. `uwu choose show` — посмотреть свои сохранённые списки.
7. `uwu choose [name]` — выбрать вариант из сохранённого списка.
   Можно временно добавить или удалить варианты: `uwu choose dinner + pasta - sushi`.

Алиасы: `uwu gamba` и `uwu gamble` работают так же, как `uwu choose`."""
    await message.channel.send(text)


async def help_ru_admin(message):
    text = """# Команды администрирования!
1. `uwu perms set [user] [access_level]` — изменить уровень доступа пользователя.
   Пример: `uwu perms set @User admin`.
   Доступные уровни: `default`, `admin` (или `administrator`). Только владелец бота.
2. `uwu reboot` — перезапустить Missu. Доступно администраторам.
3. `uwu gitpush` — отправить локальные изменения на GitHub. Только владелец бота.
4. `uwu shutdown` — выключить Missu. Только владелец бота.

Используй эти команды осторожно!"""
    await message.channel.send(text)
