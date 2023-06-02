import json


def reformat_output_payload(payload):

    reformatted_data = json.dumps(payload, indent=4, ensure_ascii=False)
    reformatted_data = reformatted_data.encode().decode('utf-8').replace('\\\\n', ' ').replace('\\\\', '\\').encode().decode('unicode-escape').replace('"{', '{').replace('}"', '}').replace('\\"', '')
    return json.loads(reformatted_data)