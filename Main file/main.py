import time
import string
import random
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.baseclass import Baseclass


class TestTELock(Baseclass):
    def test_Login(self):
        wait=WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.EditText")))
        self.driver.find_element(By.XPATH, "//android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.EditText").send_keys("9585905265")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.EditText").send_keys("12345")
        time.sleep(3)
        self.driver.find_element(By.ID, "com.telocks.te:id/ctaSigniIn").click()
        time.sleep(9)
        allure.attach(self.driver.get_screenshot_as_png(), name="Lock Page",
                      attachment_type=AttachmentType.PNG)
        time.sleep(3)

#def test_unlock(self):
 #       self.driver.find_element(By.ID, "com.telocks.te:id/ivGetCode").click()
  #      time.sleep(3)
   #     self.driver.find_element(By.ID, "android:id/button1").click()
    #    time.sleep(3)
     #   allure.attach(self.driver.get_screenshot_as_png(), name="unlock page",
      #                attachment_type=AttachmentType.PNG)
       # self.driver.find_element(By.ID, "com.telocks.te:id/cbnUnlock").click()
       # time.sleep(3)"""


#def test_addlock(self):
       # d = random.sample(range(100000000, 999999999), 1)
        #k = "1"
        #for i in d:
         #   i = str(i)
         #   Replaced = i.replace('0', '1')
         #   l = k + Replaced
         #   serial_number = int(l)
        #    print(serial_number)
       # Letter1 = random.choice(string.ascii_letters)
       # Letter2 = random.choice(string.ascii_letters)
        #Letter3 = random.choice(string.ascii_letters)
        #Letter4 = random.choice(string.ascii_letters)
        #lock_name = Letter1 + Letter2 + Letter3 + Letter4
        #print(lock_name)
        #self.driver.find_element(By.ID, "com.telocks.te:id/ivAddLock").click()
        #time.sleep(3)
        #self.driver.find_element(By.ID, "com.telocks.te:id/etSerialNumber").send_keys(serial_number)
        #time.sleep(3)
        #self.driver.find_element(By.ID, "com.telocks.te:id/etLockName").send_keys(lock_name)
        #time.sleep(3)
        #allure.attach(self.driver.get_screenshot_as_png(), name="Add lock",
         #             attachment_type=AttachmentType.PNG)
        #self.driver.find_element(By.ID, "com.telocks.te:id/cbAddLock").click()
       # time.sleep(3)

    #def test_changelock(self):
        #time.sleep(5)
        #self.driver.find_element(By.ID, "com.telocks.te:id/ivSearch").click()
        #time.sleep(3)
        #self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]").click()
        #time.sleep(3)
        #allure.attach(self.driver.get_screenshot_as_png(), name="change Lock",
                     #attachment_type=AttachmentType.PNG)
        #time.sleep(3)


#    def test_virtualkey(self):
#       self.driver.find_element(By.ID, "com.telocks.te:id/ivMenu").click()
#        time.sleep(3)
#        self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[3]/android.widget.CheckedTextView").click()
#        time.sleep(3)
#        self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.EditText").send_keys("Alex")
#       time.sleep(3)
#        self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.EditText").send_keys("9578261722")
#        time.sleep(3)
#        self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.EditText").send_keys("herbertrajalex@gmail.com")
#        time.sleep(3)
#        self.driver.find_element(By.ID, "com.telocks.te:id/rbTemporary").click()
#        time.sleep(3)
#        self.driver.find_element(By.ID, "com.telocks.te:id/pwStartDate").click()
#        time.sleep(3)
#        self.driver.find_element(By.XPATH, "//android.view.View[@content-desc='30 May 2022']").click()
#        time.sleep(3)
#        self.driver.find_element(By.ID, "android:id/button1").click()
#        time.sleep(3)
#        self.driver.find_element(By.ID, "com.telocks.te:id/pwEndDate").click()
#        time.sleep(3)
#        self.driver.find_element(By.XPATH, "//android.view.View[@content-desc='31 May 2022']").click()
#        time.sleep(3)
#        self.driver.find_element(By.ID, "android:id/button1").click()
#        time.sleep(3)
#        self.driver.find_element(By.ID, "com.telocks.te:id/ctaAssign").click()
#        time.sleep(3)

    def test_myactivity(self):
        self.driver.find_element(By.ID, "com.telocks.te:id/ivGetCode").click()
        time.sleep(6)
        self.driver.find_element(By.ID, "android:id/button1").click()
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(), name="Unlock page" ,
                       attachment_type=AttachmentType.PNG)
        self.driver.find_element(By.ID, "com.telocks.te:id/cbnUnlock").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "com.telocks.te:id/ivMenu").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[4]/android.widget.CheckedTextView").click()
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="Present Lock Activity",
                      attachment_type=AttachmentType.PNG)
        time.sleep(3)
        self.driver.find_element(By.ID, "com.telocks.te:id/ivSearch").click()
        time.sleep(3)
        Locks = self.driver.find_elements(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView")
        i= -1
        for Locks1 in Locks:
            i = i+1
            Names=Locks1.text
            print(Names)
            if Names == "Gh - 1986565994":
                time.sleep(4)
                self.driver.find_elements(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[@id='android:id/tex1']")[i].click()
                time.sleep(10)
                break
        time.sleep(3)
        allure.attach(self.driver.get_screenshot_as_png(), name="Next Lock",
                      attachment_type=AttachmentType.PNG)
        time.sleep(3)




#    def test_deletelock(self):
#
#       self.driver.find_element(By.ID, "com.telocks.te:id/ivMenu").click()
#      time.sleep(3)
#     self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[8]/android.widget.CheckedTextView").click()
    #    time.sleep(3)
     #   self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.ImageView[2]").click()
      #  time.sleep(3)
       # self.driver.find_element(By.ID, "android:id/button1").click()
        #time.sleep(3)