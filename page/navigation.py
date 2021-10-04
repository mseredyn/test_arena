from page.base_page import BasePage


class Navigation(BasePage):

    TASKS_SUBPAGE = "//a[contains(text(), 'Tasks')]"
    PROJECT_SELECT = "//a[@class='chosen-single']"

    def __init__(self, driver):
        super().__init__(driver)

    # top-bar

    def click_logout(self):
        raise NotImplementedError

    def click_settings(self):
        raise NotImplementedError

    def click_details(self):
        raise NotImplementedError

    def click_messages(self):
        raise NotImplementedError

    def click_current_project(self):
        self.click_by_xpath(self.PROJECT_SELECT)

    def select_current_project_by_name(self, project_name):
        self.click_current_project()
        self.click_by_xpath(f'//li[text()="{project_name}"]')

    # left nav-bar

    def click_dashboard(self):
        raise NotImplementedError

    def click_project(self):
        raise NotImplementedError

    def click_releases(self):
        raise NotImplementedError

    def click_environments(self):
        raise NotImplementedError

    def click_versions(self):
        raise NotImplementedError

    def click_tags(self):
        raise NotImplementedError

    def click_tasks(self):
        self.click_by_xpath(self.TASKS_SUBPAGE)

    def click_defects(self):
        raise NotImplementedError

    def click_test_base(self):
        raise NotImplementedError

    def click_files(self):
        raise NotImplementedError
