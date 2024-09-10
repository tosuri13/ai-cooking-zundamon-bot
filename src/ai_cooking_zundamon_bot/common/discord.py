import json

import requests

from ai_cooking_zundamon_bot.common.aws.ssm import get_parameter


def respond_interaction(content: str, interaction_token: str) -> None:
    application_id = get_parameter(key="/ACZB/DISCORD_APPLICATION_ID")

    response = requests.post(
        url=f"https://discord.com/api/v10/webhooks/{application_id}/{interaction_token}",
        data=json.dumps(
            {
                "content": content,
            }
        ),
        headers={
            "Authorization": f"Bot {get_parameter(key='/ACZB/DISCORD_BOT_TOKEN')}",
            "Content-Type": "application/json",
        },
    )

    if response.status_code != 200:
        raise ValueError(
            f"Communication to Discord API failed. [reason: {response.text}]"
        )

    return None


def get_option_dict(options: dict | None):
    if options is None:
        return {}
    else:
        return {option["name"]: option["value"] for option in options}
