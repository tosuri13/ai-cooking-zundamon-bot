def get_zunda_error_comment(exception: Exception) -> str:
    comment = (
        "どこかでエラーが発生してるみたいなのだ!!よく分からないからボクの開発者に聞いてほしいのだ!!\n"
        "```\n"
        f"{type(exception).__name__}: {exception}\n"
        "```\n"
    )

    return comment
