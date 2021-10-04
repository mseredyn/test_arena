import pytest

from helpers.random_helper import get_n_random_alphanumericals
from page.add_task_page import AddTaskPage
from page.dashboard_page import DashboardPage
from page.task_details_page import TaskDetailsPage
from page.tasks_page import TasksPage


class TestTasks:

    @pytest.fixture(scope="function")
    def navigate_to_tasks(self, webdriver_logged_in_factory):
        driver = webdriver_logged_in_factory.get()
        page = DashboardPage(driver)
        page.select_current_project_by_name("Czerwony październik")
        page.click_tasks()
        return driver

    def test_add_task_and_observe(self, navigate_to_tasks):
        random = get_n_random_alphanumericals()
        driver = navigate_to_tasks
        title = f'some_test_title_-_{random}'
        description = f'this is some test description {random}'
        environment = "nazwa"
        version = "11"

        # access add task subpage
        page = TasksPage(driver)
        page.click_add_a_task()
        page = AddTaskPage(driver)

        # fill data
        page.set_title(title)
        page.set_description(description)
        page.set_environments(environment)
        page.set_versions(version)
        page.set_deadline()
        page.set_assignment()

        page.click_submit()

        # go to tasks details page
        page = TaskDetailsPage(driver)
        page.find_task_title_by_title(title)
        page.find_task_description_by_desciption(description)

        # go to tasks and check on list
        page.click_tasks()
        page = TasksPage(driver)
        page.find_task_by_title(title)
