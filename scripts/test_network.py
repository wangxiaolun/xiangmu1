import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.network_page import NetworkPage


class TestNetwork:
    def setup(self):
        self.driver = init_driver()
        self.network_page = NetworkPage(self.driver)

    def test_mobile_network_2g(self):
        # xxxx
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_2g_network()

    def test_mobile_network_3g(self):
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_3g_network()
        
        
    def test_mobile_network_4g(self):
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_4g_network()
        
    def test_mobile_network_5g(self):
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_5g_network()

    def test_mobile_network_6g(self):
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_6g_network()

    def test_mobile_network_7g(self):
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_7g_network()

    def test_mobile_network_8g(self):
        self.network_page.click_more()
        self.network_page.click_network()
        self.network_page.click_first_network()
        self.network_page.click_8g_network()



