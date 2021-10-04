from page.navigation import Navigation


class DashboardPage(Navigation):

    def __init__(self, driver):
        super().__init__(driver)
        self.assert_sub_page_url("")
