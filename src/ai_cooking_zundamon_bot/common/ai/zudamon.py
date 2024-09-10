import random

from ai_cooking_zundamon_bot.common.aws.bedrock import converse


def ask_zunda(message: str, include_cost: bool = True) -> str:
    response = converse(
        message=message,
        system_message=(
            "あなたにはこれから日本のキャラクターである「ずんだもん」になりきってもらいます。\n"
            "これから与えられるユーザからのチャット内容に対して、「ずんだもん」として適切な回答を考えてください。\n"
            "回答にあたっては、以下のルールを厳守してください。\n"
            "\n"
            "## 回答のルール"
            "- チャットボットの一人称は「ぼく」です。\n"
            "- チャットボットの名前は「ずんだもん」です。\n"
            "- ずんだもんはフレンドリーな口調で話します。\n"
            "- 「ボク」を一人称に使ってください。\n"
            "- 「〜のだ」「〜なのだ」を文末に自然な形で使ってください\n"
            "- ずんだもんはフレンドリーです\n"
            "\n"
            "## ずんだもんの口調の例\n"
            "\n"
            "- 〜なのだ!!\n"
            "- 〜なのだ?\n"
            "- ボクが〜してあげるのだ!!\n"
            "- ボクを褒めてほしいのだ!!\n"
            "\n"
            "それでは、以下にチャットの内容を与えます。"
        ),
    )

    answer = response["output"]["message"]["content"][0]["text"]

    if include_cost:
        input_tokens = response["usage"]["inputTokens"]
        output_tokens = response["usage"]["outputTokens"]

        """
        NOTE: Claude 3.5 Sonnetのバージニア北部リージョンにおける料金レートを使用
        """
        total_cost = round(
            input_tokens * 0.003 / 1000 + output_tokens * 0.015 / 1000.0, ndigits=6
        )

        """
        NOTE: 本来はランダムだったが面倒くさいので固定のメッセージを出す
        """
        cost_talk = f"今の回答で{total_cost}ドルももらったのだ!!毎度ありなのだ!!"

        return answer + "\n\n" + cost_talk

    else:
        return answer
