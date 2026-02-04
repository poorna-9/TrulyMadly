This project implements an AI Operations Assistant that accepts a natural-language task, plans the required steps, executes real API calls, and verifies the final output.
The system demonstrates:
Agent-based reasoning
Structured LLM outputs (no monolithic prompts)
Real third-party API integrations
Local execution via CLI
This project was built as part of a 24-hour GenAI Intern Assignment.
openweathermap and newsapi are used to extract data based on user query




To evaluate this open terminal and run:
 1: python -m pip install -r requirements.txt
 2:python main.py
 3:then provide userquery inside terminal 






 
Please i did not provided any API_KEYS please check the my mail before evalution i would send you API_KEYS
The examples i tested:
 1:Enter your task: Tell me the current weather in Bangalore
{
  "steps": [
    {
      "id": 1,
      "tool": "get_weather",
      "params": {
        "city": "Bangalore"
      }
    }
  ]
}
{
  "1": {
    "city": "Bengaluru",
    "temperature_celsius": 23.85,
    "humidity": 42,
    "weather": "clear sky"
  }
}
{
  "status": "success",
  "steps": [
    {
      "step_id": 1,
      "action": "get_weather",
      "status": "completed",
      "output": {
        "city": "Bengaluru",
        "temperature_celsius": 23.85,
        "humidity": 42,
        "weather": "clear sky"
      }
  2:
    Enter your task: Show me the latest technology news
{
  "steps": [
    {
      "id": 1,
      "tool": "get_news",
      "params": {
        "topic": "technology",
        "limit": 5
      }
    }
  ]
}
{
  "1": [
    {
      "title": "Coming to Xbox Game Pass: High on Life 2, Madden NFL 26, Avatar: Frontiers of Pandora, and More - Xbox Wire",
      "source": "Xbox.com",
      "description": "Coming soon to Xbox Game Pass: High on Life 2, Madden NFL 26, Avatar: Frontiers of Pandora, and more!",
      "url": "https://news.xbox.com/en-us/2026/02/03/xbox-game-pass-february-2026-wave-1/"
    },
    {
      "title": "Stardew Valley Turns 10: The Big ConcernedApe Interview - IGN",
      "source": "IGN",
      "description": "We sat down with Stardew Valley creator Eric Barone for a lengthy interview not about the game's beginnings, but about its journey over the last 10 years, and its future.",
      "url": "https://www.ign.com/articles/stardew-valley-turns-10-the-big-concernedape-interview"
    },
    {
      "title": "Metroid Prime 4: Beyond Sales Have Got Off To A Slow Start - Nintendo Life",
      "source": "Nintendo Life",
      "description": "One in a million",
      "url": "https://www.nintendolife.com/news/2026/02/metroid-prime-4-beyond-sales-have-got-off-to-a-slow-start"
    },
    {
      "title": "As player numbers fall, Highguard makes the actually-quite-good 5v5 mode permanent - Eurogamer",
      "source": "Eurogamer.net",
      "description": "Highguard is gaining more positive reviews following the addition of a 5v5 mode that's becoming permanent, but does it have a fighting chance?",
      "url": "https://www.eurogamer.net/highguard-gets-permanent-5v5-mode"
    },
    {
      "title": "I recommend these USB-C connectors to anyone with a laptop - here's what they do - ZDNET",
      "source": "ZDNet",
      "description": "Busted USB-C ports are a problem. These affordable breakaway accessories protect them at an affordable price.",
      "url": "https://www.zdnet.com/article/magnetic-usb-c-adapter-240w-duhesin-review/"
    }
  ]
}
{
  "status": "success",
  "steps": [
    {
      "step_id": 1,
      "action": "get_news",
      "status": "completed",
      "output": [
        {
          "title": "Coming to Xbox Game Pass: High on Life 2, Madden NFL 26, Avatar: Frontiers of Pandora, and More - Xbox Wire",
          "source": "Xbox.com",
          "description": "Coming soon to Xbox Game Pass: High on Life 2, Madden NFL 26, Avatar: Frontiers of Pandora, and more!",
          "url": "https://news.xbox.com/en-us/2026/02/03/xbox-game-pass-february-2026-wave-1/"
        },
        {
          "title": "Stardew Valley Turns 10: The Big ConcernedApe Interview - IGN",
          "source": "IGN",
          "description": "We sat down with Stardew Valley creator Eric Barone for a lengthy interview not about the game's beginnings, but about its journey over the last 10 years, and its future.",
          "url": "https://www.ign.com/articles/stardew-valley-turns-10-the-big-concernedape-interview"
        },
        {
          "title": "Metroid Prime 4: Beyond Sales Have Got Off To A Slow Start - Nintendo Life",
          "source": "Nintendo Life",
          "description": "One in a million",
          "url": "https://www.nintendolife.com/news/2026/02/metroid-prime-4-beyond-sales-have-got-off-to-a-slow-start"
        },
        {
          "title": "As player numbers fall, Highguard makes the actually-quite-good 5v5 mode permanent - Eurogamer",
          "source": "Eurogamer.net",
          "description": "Highguard is gaining more positive reviews following the addition of a 5v5 mode that's becoming permanent, but does it have a fighting chance?",
          "url": "https://www.eurogamer.net/highguard-gets-permanent-5v5-mode"
        },
        {
          "title": "I recommend these USB-C connectors to anyone with a laptop - here's what they do - ZDNET",
          "source": "ZDNet",
          "description": "Busted USB-C ports are a problem. These affordable breakaway accessories protect them at an affordable price.",
          "url": "https://www.zdnet.com/article/magnetic-usb-c-adapter-240w-duhesin-review/"
        }
      ]
    }
  ]
}


    }
  ]
}
