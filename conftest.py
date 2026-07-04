import pytest
import user_data
from selenium import webdriver
from data import Url


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Url.BASE_PAGE)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(Url.BASE_PAGE)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def user():
    user = user_data.register_new_user_and_return_user_data()
    yield user
    user_data.delete_user(user['json']['accessToken'])
