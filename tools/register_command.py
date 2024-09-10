import json

import requests

from src.ai_cooking_zundamon_bot.common.aws.ssm import get_parameter
from src.ai_cooking_zundamon_bot.common.event.discord import (
    ApplicationCommandOptionType,
)

APPLICATION_ID = get_parameter(key="/ACZB/DISCORD_APPLICATION_ID")
AUTH_HEADERS = {
    "Authorization": f"Bot {get_parameter(key='/ACZB/DISCORD_BOT_TOKEN')}",
    "Content-Type": "application/json",
}
COMMANDS_ENDPOINT_URL = (
    f"https://discord.com/api/v10/applications/{APPLICATION_ID}/commands"
)


if __name__ == "__main__":
    response = requests.get(
        url=COMMANDS_ENDPOINT_URL,
        headers=AUTH_HEADERS,
    )

    for command in response.json():
        command_id = command["id"]

        requests.delete(
            url=f"{COMMANDS_ENDPOINT_URL}/{command_id}",
            headers=AUTH_HEADERS,
        )

    commands = [
        {
            "name": "recipe",
            "description": "ボクがお料理のレシピを教えてあげるのだ!!",
            "options": [
                {
                    "name": "order",
                    "description": "レシピに関する命令を書くのだ!!",
                    "required": True,
                    "type": ApplicationCommandOptionType.STRING.value,
                },
            ],
        },
    ]

    for command in commands:
        response = requests.post(
            url=COMMANDS_ENDPOINT_URL,
            headers=AUTH_HEADERS,
            data=json.dumps(command),
        )
        if response.status_code == 201:
            print(f"\"{command['name']}\"コマンドの追加に成功したのだ!!")
        else:
            print(f"\"{command['name']}\"コマンドの追加に失敗したのだ...")
