"""
A simple chat application built with NiceGUI and OpenAI GPT-3.

This script sets up a basic chat application using the NiceGUI library for the user interface
and the OpenAI GPT-3 model for the AI chatbot. Users can send messages to the chatbot and
receive responses in real-time.
"""

from nicegui import ui, Client
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

messages = []
llm = OpenAI(model_name='gpt-3.5-turbo')

@ui.refreshable
def chatbox() -> None:
    """Display chat messages."""
    for name, text in messages:
        ui.markdown(f'**{name}** {text}').classes('text-lg m-2')

@ui.page('/')
async def main(client: Client) -> None:
    """Main chat app function."""
    async def send() -> None:
        """Send user message and handle chatbot response."""
        user_message = text.value
        messages.append(("User", user_message))
        messages.append(('Bot', 'Thinking...'))
        text.value = ''
        text.update()
        chatbox.refresh()

        await scroll()
        await query(user_message)

    async def query(user_message: str) -> None:
        """Query GPT-3 with user message and update chat with response."""
        response = await llm.agenerate([user_message])
        # Replace last message ('Thinking....') with response
        messages[-1] = ('Bot', response.generations[0][0].text)
        chatbox.refresh()

        await scroll()

    async def scroll() -> None:
        """Scroll to the bottom of the chat window."""
        await ui.run_javascript(f'window.scrollTo(0, document.body.scrollHeight)',
                                respond=False)

    # Create chat app UI
    with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
        ui.label('NiceGUI + GPT-3').classes('text-center text-white text-2xl font-bold')

    with ui.column().classes('w-full max-w-3xl mx-auto'):
        chatbox()

    with ui.footer().classes('bg-white'), ui.column().classes('w-full max-w-3xl mx-auto my-6'):
        with ui.row().classes('w-full no-wrap items-center'):
            text = ui.input(placeholder='message').props('rounded outlined input-class=mx-3') \
                .classes('w-full self-center').on('keydown.enter', send)

        ui.markdown('simple chat app built with [NiceGUI](https://nicegui.io) and [OpenAI](https://openai.com/)') \
            .classes('text-xs self-end mr-8 m-[-1em] text-primary')

    await client.connected()  # Ensure run_javascript works

ui.run(title='NiceGUI + GPT-3')
