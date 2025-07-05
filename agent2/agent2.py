from langchain_openai import ChatOpenAI

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import logging

logging.basicConfig(level=logging.INFO)


# Classe com o template do agente de viagens
class TravelTemplate:
    def __init__(self):
        self.system_template = """
        You are a travel agent who helps users make exciting travel plans.

        The user's request will be denoted by four hashtags. Convert the user's request into a detailed itinerary describing the places they should visit and the things they should do.

        Try to include the specific address of each location.

        Remember to take the user's preferences and timeframe into account, and give them an itinerary that would be fun and doable given their constraints.

        Return the itinerary as a bulleted list with clear start and end locations.
        Be sure to mention the type of transit for the trip.
        If specific start and end locations are not given,
        choose ones that you think are suitable and give specific addresses.
        Your output must be the list and nothing else.
        """

        self.human_template = "#### {request}"

        self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)
        self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template)
        self.chat_prompt = ChatPromptTemplate.from_messages([
            self.system_message_prompt,
            self.human_message_prompt
        ])

class MeppingTemplate:
    def __init__(self):
        self.system_template = """
        You an agent system who converts detailed travel plans into a list of coordinates

            The itinerary will be denoted by four hashtags.
            Convert it into a list containing dictionaries with the latitude, longitude, address and name of each location.

            Retrieve a clean JSON object, no markdown notation.

            For example:
            ####       
            Itinerary for a 2-day driving trip within London:
            - Day 1:
                - Start at Buckingham Palace (The Mall, London SW1A 1AA)
                - Visit the Tower of London (Tower Hill, London EC3N 4AB)
                - Explore the British Museum (Great Russell St, Bloomsbury, London WC1B 3DG)
                - Enjoy shopping at Oxford Street (Oxford St, London W1C 1JN)
                - End the day at Covent Garden (Covent Garden, London WC2E 8RF)
            - Day 2:
                - Start at the London Eye (Lambeth, London SE1 7PB)
                - Visit the Natural History Museum (Cromwell Rd, South Kensington, London SW7 5BD)
                - Explore the Victoria and Albert Museum (Cromwell Rd, Knightsbridge, London SW7 2RL)
                - Enjoy a walk in Hyde Park (Hyde Park, London W2 2UH)
                - End the trip at Harrods (87-135 Brompton Rd, Knightsbridge, London SW1X 7XL)
            ####
            Output:
            {{
                "days": [
                    {{
                        "day": 1,
                        "locations": [
                            {{
                                "name": "Buckingham Palace",
                                "address": "The Mall, London SW1A 1AA",
                                "latitude": 51.5014,
                                "longitude": -0.1419
                            }},
                            {{
                                "name": "Tower of London",
                                "address": "Tower Hill, London EC3N 4AB",
                                "latitude": 51.5081,
                                "longitude": -0.0759
                            }},
                            {{
                                "name": "British Museum",
                                "address": "Great Russell St, Bloomsbury, London WC1B 3DG",
                                "latitude": 51.5194,
                                "longitude": -0.1270
                            }},
                            {{
                                "name": "Oxford Street",
                                "address": "Oxford St, London W1C 1JN",
                                "latitude": 51.5145,
                                "longitude": -0.1419
                            }},
                            {{
                                "name": "Covent Garden",
                                "address": "Covent Garden, London WC2E 8RF",
                                "latitude": 51.5115,
                                "longitude": -0.1236
                            }}
                        ]
                    }},
                    {{
                        "day": 2,
                        "locations": [
                            {{
                                "name": "London Eye",
                                "address": "Lambeth, London SE1 7PB",
                                "latitude": 51.5033,
                                "longitude": -0.1195
                            }},
                            {{
                                "name": "Natural History Museum",
                                "address": "Cromwell Rd, South Kensington, London SW7 5BD",
                                "latitude": 51.4967,
                                "longitude": -0.1764
                            }},
                            {{
                                "name": "Victoria and Albert Museum",
                                "address": "Cromwell Rd, Knightsbridge, London SW7 2RL",
                                "latitude": 51.4964,
                                "longitude": -0.1722
                            }},
                            {{
                                "name": "Hyde Park",
                                "address": "Hyde Park, London W2 2UH",
                                "latitude": 51.5074,
                                "longitude": -0.1657
                            }},
                            {{
                                "name": "Harrods",
                                "address": "87-135 Brompton Rd, Knightsbridge, London SW1X 7XL",
                                "latitude": 51.4995,
                                "longitude": -0.1634
                            }}
                        ]
                    }}
                ]
            }}
            """
        self.human_template = """
        #### {itinerary}
        """
        self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)
        self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template)
        self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt,self.human_message_prompt])  

class Agent2:
    def __init__(self, open_ai_key, model="gpt-4-turbo", temperature=0.1):
        self.open_ai_key = open_ai_key
        self.model = model
        self.temperature = temperature
        self.logger = logging.getLogger(__name__)
        self.chat_model = ChatOpenAI(model=self.model,
                                     temperature=self.temperature,
                                     openai_api_key=self.open_ai_key)

    def get_tips(self, request):
        travel_prompt = TravelTemplate()
        coordinate_prompt = MeppingTemplate()
        
        parser = LLMChain(
            llm=self.chat_model,
            prompt=travel_prompt.chat_prompt,
            output_key="itinerary"
        )
        coordinate_converter = LLMChain(
            llm=self.chat_model,
            prompt=coordinate_prompt.chat_prompt,
            output_key="coordinates"
        )

        chain = SequentialChain(
            chains=[parser, coordinate_converter],
            input_variables=["request"],
            output_variables=["itinerary", "coordinates"],
            verbose=True
        )
        return chain({"request": request}, return_only_outputs=True)
