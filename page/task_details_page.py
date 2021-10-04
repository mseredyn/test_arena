from page.navigation import Navigation


class TaskDetailsPage(Navigation):

    def __init__(self, driver):
        super().__init__(driver)

    def find_task_title_by_title(self, title):
        task_title = f'//div[contains(text(),"{title}")]'
        self.find_by_xpath(task_title)

    def find_task_description_by_desciption(self, description):
        task_description = f'//div[contains(text(), "{description}")]'
        self.find_by_xpath(task_description)