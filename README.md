## El Tarf Tourist Chatbot 🌍🤖

A semi-intelligent multilingual chatbot designed to assist tourists in El Tarf, Algeria. 
The chatbot provides information about restaurants, beaches, monuments, hotels, and other points of interest, in three languages: Arabic, French, and English.

--- 

## Features

- Multilingual support: Arabic, French, English.
- Provides places to visit with latitude and longitude coordinates.
- Offers protection and safety instructions for each category.
- Integrates easily into mobile applications.
- Trained on a dataset of tourist places across Algeria, with city-specific filtering (El Tarf in this project).

--- 

## Installation

1- Clone the repository: 
      - git clone https://github.com/<your-username>/el-tarf-chatbot.git
      - cd el-tarf-chatbot

2- Install dependencies:
      pip install -r requirements.txt

3- Make sure your dataset CSV (algeria_tourist_places_all_cities.csv) is in the project folder.

--- 

## Usage 
1- Run locally: python app.py
2- The server will run on http://0.0.0.0:10000
3- API Endpoints: 
   - Home:
     GET / – returns a welcome message.
   - Chat:
     POST /chat – send a JSON payload:
        {
            "message": "restaurants in El Tarf"
        }
     Response example:
     {
         "response": "- Chez Miloud at (36.1891382, 1.5347464)\n- Restaurant Sodani at (36.1886224, 1.5339919)\n\nProtection Instructions:
         Respect hotel property and dispose of waste..."
     }

4- Can be integrated into mobile apps using the /chat API.

--- 

## Future Improvements

- Expand dataset with more cities and points of interest.
- Improve natural language understanding for more conversational queries.
- Add contextual follow-up questions.
- Deploy as a production-ready web or mobile service.

--- 

## License

MIT License – feel free to reuse and adapt.


     

