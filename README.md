# ai-cooking-zundamon-bot

お料理のレシピをずんだもんが教えてくれるAI Discord Bot(実態はLT用に[Claudeお嬢様](https://github.com/tosuri13/lady-claude)からレシピ機能だけを剥がしてきたもの)。

## 🛠️ Develop

Pythonのパッケージ管理には**Poetry**と**poethepoet**、ビルドとAWS環境へのデプロイには**AWS SAM**を使用しています。

- 依存関係のインストール

```shell
$ poetry install
```

- アプリケーションのビルドとデプロイ

```shell
$ poe build && poe deploy
```

> [!WARNING]
> こちらのリポジトリを参考にAWS環境へデプロイされる場合は、`samconfig.toml`や`template.yaml`はご自身の環境に合わせて書き換えてください。

> [!WARNING]
> アプリケーション内に登場するSSMパラメータ(Discordのトークンやベクトルを格納するS3バケットなど)は手動で作成する必要があります。
