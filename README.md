# AI Weather Assistant

## Description

This Python application demonstrates how to use the OpenAI API with function calling to retrieve and report the current weather for a given city. It leverages the Open-Meteo API for weather data.

The primary purpose is to show an example of integrating an external tool (weather API) with an OpenAI language model, allowing the model to request specific information (latitude and longitude for a city) and then use that information to call a function that fetches real-time data.

## Features

- Integrates with the OpenAI API (specifically `gpt-4.1-mini`).
- Uses function calling to determine when to fetch weather data.
- Retrieves current temperature data from the Open-Meteo API.
- Handles API responses and potential errors.
- Loads API keys and other sensitive information from a `.env` file.

## Prerequisites

- Python 3.13 or higher (as specified in [`.python-version`](c:\Users\mhodo\Desktop\Python\Ruff.python-version) and [`pyproject.toml`](c:\Users\mhodo\Desktop\Python\Ruff\pyproject.toml)).
- An OpenAI API key.
- Access to the Open-Meteo API (no key required for basic use).

## Setup

1.  **Clone the repository (if applicable) or ensure you have the project files.**

2.  **Install dependencies and create/update the virtual environment:**
    Run the following command to create a `.venv` virtual environment (if it doesn't exist) and install all dependencies as specified in your `pyproject.toml`. This ensures your environment matches the configuration exactly.

    ```bash
    uv sync
    ```

    (If you update dependencies in `pyproject.toml`, simply re-run `uv sync` to update your environment.)

3.  **Create a `.env` file:**
    Create a file named `.env` in the root directory of the project and add your OpenAI API key:
    ```env
    // filepath: .env
    OPENAI_API_KEY="your_openai_api_key_here"
    ```
    The [`.gitignore`](c:\Users\mhodo\Desktop\Python\Ruff.gitignore) file is already configured to ignore `.env`.

## Usage

To run the application, execute the [`main.py`](c:\Users\mhodo\Desktop\Python\Ruff\main.py) script:

```bash
python main.py
```

The script will:

1.  Initialize the OpenAI client.
2.  Send an initial user message ("What is the weather like in New York?") to the OpenAI model.
3.  The model should detect that it needs to call the `get_weather` function and will return a function call request.
4.  The application will print that a function call was detected.
5.  The [`get_weather`](c:\Users\mhodo\Desktop\Python\Ruff\main.py) function will be called with the longitude and latitude provided by the model.
6.  The weather information will be fetched from Open-Meteo.
7.  The result of the function call is sent back to the OpenAI model.
8.  The model will then generate a final response based on the weather data, which will be printed to the console.

Example output might look like:

```
Function get_weather call detected.
The current temperature is 10.5°C.
```

(The exact temperature will vary).
