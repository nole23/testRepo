import os
import shutil
from selenium import webdriver
from django.test import LiveServerTestCase
import time
import subprocess
import signal
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class UserTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()  # Osiguraj da se osnovne postavke izvrše

        command = 'python manage.py runserver &'

        # Pokrenite komandu u Bash okruženju
        cls.cmd_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        time.sleep(10)  # Povećaj ovo vreme ako je potrebno

        # Inicijalizuj WebDriver

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')  # Opcionalno, za rad bez GUI-a

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)  # Sačekaj 10 sekundi za elemente

        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        print("Tearing down class...")
        super().tearDownClass()
        cls.driver.quit()

        # Pokušaj da zaustaviš CMD proces
        if cls.cmd_process.poll() is None:  # Ako je proces još uvek aktivan
            cls.cmd_process.send_signal(signal.CTRL_C_EVENT)
            time.sleep(5)  # Sačekaj da se proces zaustavi

        # Izvrši `flush` komandu za brisanje baze
        try:
            command = 'python manage.py flush --noinput'
            cls.cmd_process1 = subprocess.run(command, shell=True, text=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(f"Flush command failed: {e}")

    def test_1_setuser(self):
        print("Start 1. test...")
        self.driver.get('http://localhost:8000/test')

        pre_elements = self.driver.find_elements(By.TAG_NAME, 'pre')

        for pre in pre_elements:
            print(pre.text)  # Prikazivanje sadržaja svakog <pre> elementa
        time.sleep(50)  # Sačekaj da se proces zaustavi

        print("End 1. test...")