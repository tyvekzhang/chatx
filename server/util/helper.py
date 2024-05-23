"""Helper part mainly for handle response"""

import json

from config.config import configs


def handle_event_stream(response):
    """
    Processes and yields event stream data in JSON format.

    Args:
        response: The response object containing event stream data.

    Yields:
        A JSON string containing the extracted content and a boolean indicating whether the processing is done.
    """
    if configs.online:
        for chunk in response:
            content = chunk.output.text
            done = False if chunk.output.finish_reason == "null" else True
            yield (
                json.dumps({"answer": content, "done": f"{done}"}, ensure_ascii=False)
                + "\n"
            )
    else:
        response = response.content.decode("utf-8")
        response = str(response).split("\n")[:-1]
        for chunk in response:
            chunk = json.loads(chunk)
            content = chunk["message"]["content"]
            done = chunk["done"]
            yield (
                json.dumps({"answer": content, "done": f"{done}"}, ensure_ascii=False)
                + "\n"
            )


def handle_response(response):
    """
    Extracts and returns the text content from a response object.

    Args:
        response: The response object from which to extract the text content.

    Returns:
        The extracted text content from an online response or the entire response for offline configurations.
    """
    if configs.online:
        return response.output.text
    else:
        response = response.json()
        result = response["message"]["content"]
        return result
