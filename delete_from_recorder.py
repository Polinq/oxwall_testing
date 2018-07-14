# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://127.0.0.1/oxwall/")
    wd.find_element_by_css_selector("span.ow_signin_label").click()
    wd.find_element_by_id("input_oty8ogyb").click()
    wd.find_element_by_id("input_oty8ogyb").clear()
    wd.find_element_by_id("input_oty8ogyb").send_keys("ad")
    wd.find_element_by_id("input_oty8ogyb").click()
    wd.find_element_by_id("input_oty8ogyb").clear()
    wd.find_element_by_id("input_oty8ogyb").send_keys("admin")
    wd.find_element_by_id("input_482hyzyp").click()
    wd.find_element_by_id("input_482hyzyp").clear()
    wd.find_element_by_id("input_482hyzyp").send_keys("pass")
    wd.find_element_by_id("input_ylozeweg").click()
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@class='ow_page_container']/div/div")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.ow_newsfeed_body")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.ow_newsfeed_context_menu_wrap")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.ow_newsfeed_body")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.ow_newsfeed_context_menu_wrap")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("span.ow_context_more")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//li[@id='action-feed1-130']/div[1]/div[2]/div[1]/div[2]")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.ow_newsfeed_context_menu_wrap")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_id("feed1")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.ow_newsfeed_context_menu_wrap")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.ow_context_action")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("span.ow_context_more")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.ow_context_action")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_link_text("Delete post")).perform()
    wd.find_element_by_link_text("Delete post").click()
    ActionChains(wd).move_to_element(wd.find_element_by_id("input_t4byj4r4")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_id("input_t4byj4r4")).perform()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
