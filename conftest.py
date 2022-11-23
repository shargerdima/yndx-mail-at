import pytest
import requests
from selenium import webdriver
import pathlib
import urllib3
from webdriver_manager.chrome import ChromeDriverManager

urllib3.disable_warnings()


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="ch_chrome")
    parser.addoption('--bv',
                     action='store',
                     default='99.0')


@pytest.fixture(scope="module")
def session():
    return requests.Session()


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        capabilities = options.to_capabilities()
        capabilities['acceptInsecureCerts'] = True
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser.maximize_window()
        browser.implicitly_wait(1)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference('browser.download.folderList', 2)
        fp.set_preference('browser.download.manager.showWhenStarting', False)
        fp.set_preference('browser.download.dir', str(pathlib.Path(__file__).parent.absolute()))
        fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
        browser = webdriver.Firefox(firefox_profile=fp,
                                    executable_path="C:\\geckodriver\\geckodriver.exe",
                                    firefox_binary='C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
                                    )
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser...")


