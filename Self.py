import unittest
from LoginTest import LoginTest
from EditProfileTest import ProfileEditionTest
from EditAddressTest import EditAddressTest
from CreatePostTest import CreatePostTest
from HTMLTestRunner import HTMLTestRunner

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LoginTest))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ProfileEditionTest))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(EditAddressTest))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(CreatePostTest))
    runner = HTMLTestRunner(title='Test report',open_in_browser=True,description='This is a demo report')
    runner.run(suite)
if ____name____ == "____main___":
    suite()