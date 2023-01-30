import asyncio

from httpx import AsyncClient, UnsupportedProtocol
from requests_html import HTMLSession


async def get_url_images(url: str):
    session = HTMLSession()
    r = session.get(url)
    images = r.html.find('img')

    async with AsyncClient() as client:
        for image in images:
            url = image.attrs['src']  # TODO: Might fail when URL contain relative path

            try:
                image_data = await client.get(url)
                print('Image Size', url, len(image_data.content), 'bytes')
            except UnsupportedProtocol:
                print('Error: Handle this URL', url)


asyncio.run(get_url_images('https://python.org/'))
asyncio.run(get_url_images('https://onfido.com/'))
