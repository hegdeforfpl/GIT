from selenium import webdriver
import unittest
class Test(unittest.TestCase):
    def test(self):
        self.driver = webdriver.Chrome("C://ChromeDriver//chromedriver.exe")
        self.driver.get("https://www.interviewbit.com/sql-interview-questions/")
        print(self.driver.title)
        if self.driver.title == "SQL Interview Questions CHEAT SHEET (2022) - InterviewBit":
            print("Passed")
        else:
            print("Failed")
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()