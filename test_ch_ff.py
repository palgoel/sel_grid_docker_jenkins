import allure
import pytest

@pytest.mark.usefixtures("driver_init")
class BasicTestchrome:
    pass

class Test_URL_Chrome(BasicTestchrome):
    @allure.description("Testcase to add num")
    @allure.severity(severity_level="CRITICAL")
    def test_lambdatest_blog_load(self):
        self.driver.get('https://www.lambdatest.com/blog/')
        expected_title = "LambdaTest | A Cross Browser Testing Blog"
        print(f"EXPECTED Title of the browser passed thru command line =", expected_title)
        assert expected_title == self.driver.title

