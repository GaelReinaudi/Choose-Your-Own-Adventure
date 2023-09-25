import asyncio

# import llm
import textwrap
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI


class Adventure:
    temperature = 0.7
    end_of_first_part = "And now, turn the page."

    def __init__(self, api_key):
        # self.model = llm.get_model("gpt-3.5-turbo-16k")
        # self.model.key = api_key
        self.model = ChatOpenAI(
            model="gpt-3.5-turbo-16k",
            openai_api_key=api_key,
            temperature=self.temperature,
        )

    def inital_prompt(self) -> str:
        messages = [
            SystemMessage(
                content="You are a talented author of Choose-Your-Own-Adventure books"
            ),
            HumanMessage(
                content=f"""
Write the first introductory part of a book of the type "chose your own adventure" \
where the reader, which is the main character, is a 17 year old girl coder. 
The introductory part is typically 3 pages long.
Write several paragraphs separated by blank lines.

Remarque: 
- Do not mention the page numbers! 
- Do Not give any choices to the reader yet.
- End the text with {self.end_of_first_part}

"""
            ),
        ]
        return messages

    def format_text(self, input_text, width=50):
        return textwrap.fill(input_text, width=width)

    async def start(self):
        response = self.model(self.inital_prompt())
        formatted_text = self.format_text(response.content)
        print(formatted_text)
        return formatted_text

    async def step(self):
        pass


async def test():
    import cyoa_game.config as config

    adventure = Adventure(config.OpenAIKeyManager.get_api_key())
    await adventure.start()
    await adventure.step()


if __name__ == '__main__':
    asyncio.run(test())
