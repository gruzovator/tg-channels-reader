## Telegram API demo application

_Pure Python 3 Telegram client library [telethon](https://github.com/LonamiWebs/Telethon/ ) demo_

## How to run

1. Obtain API ID and API HASH. See https://core.telegram.org/api/obtaining_api_id
2. Run register.py to register your app and generate session file (required for main script)
    ```
    ./register.py -P <your phone> -I <your api id> -H <your api hash> -S tg
    ```
3. Run demo app
    ```
    ./run-chan-reader.py -I <your api id> -H <your api hash> -S tg -C <channel name>
```
