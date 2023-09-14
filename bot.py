import asyncio
import pyppeteer

async def scrape_webpages():
    try:
        # Launch a headless browser
        browser = await pyppeteer.launch()
        page = await browser.newPage()

        # Navigate to the Google search results page
        search_query = input("Enter key word or phrase: ")
        search_query = search_query.replace(' ', '+')

        search_url = f"https://www.google.com/search?q={search_query}"
        await page.goto(search_url)

        # Retrieve the first three search result links
        result_links = await page.querySelectorAll(".g .rc .r a")
        result_links = result_links[:3]  # Limit to the first three links

        for i, link in enumerate(result_links):
            try:
                # Click on the link
                await link.click()

                # Wait for the page to load (you can adjust the timeout)
                await page.waitForSelector("body", timeout=5000)

                # Retrieve the title of the page
                title = await page.evaluate("document.title")

                # Retrieve the content of the <h1> tag
                h1_content = await page.evaluate(
                    'document.querySelector("h1").textContent'
                )

                # Retrieve the content of the <body> tag
                body_content = await page.evaluate(
                    'document.querySelector("body").textContent'
                )

                # Create and write the retrieved data to a text file for each link
                with open(f"/Users/jpdesilva/home/disrupt/bot-test-1/webpage_data_{i+1}.txt", "w") as file:
                    file.write("Title: " + title + "\n")
                    file.write("H1 Content: " + h1_content + "\n")
                    file.write("Body Content: " + body_content + "\n")

                # Go back to the search results page
                await page.goBack()
            except Exception as e:
                print(f"Error while processing link {i+1}: {str(e)}")

        # Close the browser
        await browser.close()
    except Exception as e:
        print(f"Error during scraping: {str(e)}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(scrape_webpages())
