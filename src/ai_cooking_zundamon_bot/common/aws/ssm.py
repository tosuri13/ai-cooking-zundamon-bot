from typing import List

import boto3


def get_parameter(key: str, region_name: str = "ap-northeast-1") -> str:
    ssm_client = boto3.client("ssm", region_name)

    response = ssm_client.get_parameter(Name=key)

    return response["Parameter"]["Value"]
