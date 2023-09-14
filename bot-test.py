import asyncio
from pyppeteer import launch

async def main():
    # Launch Chromium
    browser = await launch()

    # Create a new page
    page = await browser.newPage()

    # Navigate to a website (e.g., Google)
    await page.goto('https://www.google.com')

    # Wait for a moment (optional)
    await page.waitFor(5000)  # 5 seconds

    # Take a screenshot (optional)
    await page.screenshot({'path': 'screenshot.png'})

    # Close the browser
    await browser.close()

# Run the main function in an asyncio event loop
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())