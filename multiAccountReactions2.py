import asyncio
import random
from telethon import TelegramClient, types
from telethon.tl.functions.messages import SendReactionRequest
import logging
import yaml

logging.basicConfig(level=logging.INFO)

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

API_ID = config['api_id']
API_HASH = config['api_hash']
ACCOUNTS = config['accounts']
CHANNELS = config['channels']

REACT_EMOJIS = ['🥰', '👍', '🔥', '👏', '🤯', '❤️', '👌', '🤩', '🎉']


async def react_to_messages(client, channel, entity):
    messages = await client.get_messages(channel, limit=50)
    for message in messages:
        randreact = random.choice(REACT_EMOJIS)
        try:
            await client(SendReactionRequest(
                peer=types.InputPeerChannel(entity.channel_id, entity.access_hash),
                msg_id=message.id,
                reaction=randreact
            ))
            logging.info(f'{client.session.filename} reacted with {randreact}')
        except Exception as e:
            logging.error(f'{client.session.filename} failed to react: {str(e)}')


async def worker(account):
    try:
        client = TelegramClient(account['session'], account['api_id'], account['api_hash'])
        await client.start(account['phone'])

        for channel in CHANNELS:
            try:
                entity = await client.get_input_entity(channel)
                await react_to_messages(client, channel, entity)
            except Exception as e:
                logging.error(f"Error processing channel {channel}: {str(e)}")
    except Exception as e:
        logging.error(f"{account['phone']} encountered an error: {str(e)}")


async def main():
    tasks = [worker(account) for account in ACCOUNTS]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
