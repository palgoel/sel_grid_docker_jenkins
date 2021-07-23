import allure
import pytest

@pytest.mark.usefixtures("driver_init_chrome")
class BasicTestChrome:
    pass

class Test_URL_Chrome(BasicTestChrome):
    @allure.description("Testcase to add num")
    @allure.severity(severity_level="CRITICAL")
    def test_lambdatest_blog_load(self):
        self.driver.get('https://www.lambdatest.com/blog/')
        expected_title = "LambdaTest | A Cross Browser Testing Blog"
        print(f"EXPECTED Title of Chrome=", expected_title)
        assert expected_title == self.driver.title