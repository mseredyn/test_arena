from page.navigation import Navigation


class AddTaskPage(Navigation):
    TITLE = "//input[@name='title']"
    DESCRIPTION = "//textarea[@name='description']"
    ENVIRONMENTS = "//input[@id='token-input-environments']"
    VERSIONS = "//input[@id='token-input-versions']"
    DEADLINE = "//input[@id='dueDate']"
    DATEPICKER = '//div[@id="ui-datepicker-div" and contains(@style,"display: block")]'
    DATE_TO_SELECT = "//td[not(contains(@class, 'ui-datepicker-unselectable'))][last()]"

    ASSIGN_TO_ME = "//a[text()='Assign to me']"

    SUBMIT = "//input[@id='save']"

    def __init__(self, driver):
        super().__init__(driver)
        self.assert_sub_page_url("task_add")

    def set_title(self, title):
        self.fill_with_value_by_xpath(self.TITLE, title)

    def set_description(self, description):
        self.fill_with_value_by_xpath(self.DESCRIPTION, description)

    def set_environments(self, environment):
        environments_option_dropdown = f'//li[b[text()="{environment}"]][1]'
        self.fill_with_value_by_xpath(self.ENVIRONMENTS, environment)
        self.click_by_xpath(environments_option_dropdown)

    def set_versions(self, version):
        versions_option_dropdown = f'//li[@class="token-input-dropdown-item2-facebook" or @class="token-input-dropdown-item-facebook"][1]'
        self.fill_with_value_by_xpath(self.VERSIONS, version)
        self.click_by_xpath(versions_option_dropdown)

    def set_deadline(self):
        self.click_by_xpath(self.DEADLINE)
        self.click_by_xpath(self.DATE_TO_SELECT)

    def set_assignment(self):
        self.click_by_xpath(self.ASSIGN_TO_ME)

    def click_submit(self):
        self.click_by_xpath(self.SUBMIT)

    def click_cancel(self):
        raise NotImplementedError
