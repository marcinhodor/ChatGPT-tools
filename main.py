import json

import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current temperature in degree Celcius for a given city.",
        "parameters": {
            "type": "object",
            "properties": {
                "longitude": {
                    "type": "string",
                    "description": "Longitude of the city.",
                },
                "latitude": {
                    "type": "string",
                    "description": "Latitude of the city.",
                },
            },
            "required": ["longitude", "latitude"],
            "additionalProperties": False,
        },
        "strict": True,
    }
]


def get_weather(longitude: str, latitude: str) -> str:
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&temperature_unit=celsius"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        if "current_weather" in data and "temperature" in data["current_weather"]:
            temperature = data["current_weather"]["temperature"]
            return f"The current temperature is {temperature}°C."
        else:
            return "Sorry, I couldn't retrieve the weather data for this longitude and latititude from Open-Meteo."
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Open-Meteo API: {e}"
    except KeyError:
        return "Unexpected data format from Open-Meteo API."


def main():
    client = OpenAI()

    input_messages = [
        {
            "role": "system",
            "content": """You are a helpful assistant.\n
            You can call the function get_weather to get the current temperature in degree Celcius for a given city.\n
            You are not able to provide any other information about the weater so do not offer to give any.""",
        },
        {
            "role": "user",
            "content": "What is the weather like in New York?",
        },
    ]

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=input_messages,
        tools=tools,
    )

    output = response.output[0]

    if output.type == "function_call":
        if output.name == "get_weather":
            print(f"Function {output.name} call detected.")
            args = json.loads(output.arguments)

            result = get_weather(args["longitude"], args["latitude"])

            input_messages.append(output)
            input_messages.append(
                {
                    "type": "function_call_output",
                    "call_id": output.call_id,
                    "output": str(result),
                }
            )
        else:
            print(f"Unknown function call: {output.name}")
            return
    else:
        return print(response.output_text)

    response_2 = client.responses.create(
        model="gpt-4.1-mini",
        input=input_messages,
        tools=tools,
    )
    print(response_2.output_text)


if __name__ == "__main__":
    main()
