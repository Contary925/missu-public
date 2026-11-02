
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

Подробнее о сохранённой музыке: `уву помощь фавлист` или `уву помощь плейлисты`."""
    await message.channel.send(text)


async def help_ru_favlist(message):
    text = """# Сохраняй любимые песни в избранное!
1. `uwu favlist` — посмотреть своё избранное.
2. `uwu favlist add [source]` — добавить песню по поисковому запросу YouTube или ссылке на видео. Ссылки на плейлисты не поддерживаются.
3. `uwu favlist add np` — добавить текущую песню.
4. `uwu favlist remove [index]` — удалить песню по её номеру.
   Пример: `uwu favlist remove 3`.
5. `uwu favlist clear` — удалить все песни из избранного.
6. `uwu play favlist` (или `uwu playfav`) — добавить все сохранённые песни в очередь.
   Добавь `-s`, чтобы перемешать их: `uwu play favlist -s`.

Если музыка уже играет, сохранённые песни просто добавятся в очередь. Кстати, это быстрее, чем использовать плейлисты YouTube!"""
    await message.channel.send(text)


async def help_ru_playlists(message):
    text = """# Создавай собственные плейлисты!
1. `uwu playlist create [name]` — создать новый плейлист.
   Пример: `uwu playlist create Three Days Grace`.
2. `uwu playlist delete [name]` — удалить плейлист.
3. `uwu playlist add [name] [source]` — добавить песни из поиска YouTube, по ссылке на видео или плейлист.
   Используй `np`, чтобы добавить текущую песню. Пример: `uwu playlist add Three Days Grace np`.
   Короткая форма: `uwu playlist + [name] [source]`.
4. `uwu playlist remove [name] [index]` — удалить песню. Короткая форма: `uwu playlist - [name] [index]`.
5. `uwu playlist show [name]` — посмотреть содержимое плейлиста.
6. `uwu playlist showall` — показать все свои плейлисты.
7. `uwu playlist play [name]` — добавить песни из плейлиста в очередь.
8. `uwu playlist push [name]` — добавить песни из плейлиста в начало очереди.
   Добавь `-s`, чтобы перемешать песни: `uwu playlist play Three Days Grace -s`.

**Плейлист по умолчанию:** используй `uwu playlistdefault set [name]`, чтобы выбрать его.
После этого название плейлиста можно не указывать:
`uwu playlistdefault play`, `uwu playlistdefault show`, `uwu playlistdefault add [source]` и т. д.
Короткий алиас: `uwu pld set [name]`.

Плейлисты индивидуальны для каждого пользователя."""
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
