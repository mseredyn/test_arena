from page.navigation import Navigation


class TasksPage(Navigation):
    ADD_A_TASK_BUTTON = "//a[contains(text(), 'Add a task')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.assert_sub_page_url("tasks")

    def click_add_a_task(self):
        self.click_by_xpath(self.ADD_A_TASK_BUTTON)

    def find_task_by_title(self, title):
        task = f'//a[contains(text(),"{title}")]'
        self.find_by_xpath(task)