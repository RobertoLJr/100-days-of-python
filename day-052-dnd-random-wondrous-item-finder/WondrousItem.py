from selenium.webdriver.common.by import By


class WondrousItem:
    def __init__(self, name, driver):
        self.name = name.replace("'", "")
        self.source = ""
        self.snippet = ""
        self.description = ""
        self.link = ""
        self.driver = driver
        self.fetch_item_info()

    def fetch_item_info(self):
        self.driver.get(f"http://dnd5e.wikidot.com/wondrous-items:{self.name}")
        page_content = self.driver.find_elements(By.CSS_SELECTOR, value="#page-content p")
        self.source = page_content[0].text
        self.snippet = page_content[1].text

        description = [paragraph.text for paragraph in page_content[2:]]
        self.description = "\n\n".join(description)
        self.link = self.driver.current_url

    def print_info(self):
        print(
            f"""
NAME   : {self.name}
SOURCE : {self.source}
SNIPPET: {self.snippet}
            
{self.description}
            
MORE INFO: {self.link}

            """
        )
