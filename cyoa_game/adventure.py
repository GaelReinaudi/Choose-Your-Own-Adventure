import asyncio

# import llm
import textwrap
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI


class Adventure:
    def __init__(self, api_key):
        # self.model = llm.get_model("gpt-3.5-turbo-16k")
        # self.model.key = api_key
        self.model = ChatOpenAI(model="gpt-3.5-turbo-16k", openai_api_key=api_key)

    def inital_prompt(self) -> str:
        messages = [
            SystemMessage(
                content="You are a talented author of Choose-Your-Own-Adventure books"
            ),
            HumanMessage(
                content="""
Write the first introductory part of a book of the type "chose your own adventure" \
where the reader, which is the main character, is a girl coder. the introductory part \
is typically 3 pages long.
Remarque: do not mention the page numbers, just write it in one \
block of a dozen paragraphs.
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
        key = input("Make your choice:")

    async def step(self):
        pass


async def test():
    import cyoa_game.config as config

    adventure = Adventure(config.OpenAIKeyManager.get_api_key())
    await adventure.start()
    await adventure.step()


if __name__ == '__main__':
    asyncio.run(test())
