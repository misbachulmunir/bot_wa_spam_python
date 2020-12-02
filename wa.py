from selenium import webdriver
import os
import time
def banner():
 print('''
  BOOM WHATSAP By Munir
  ''')
def main():
 driver = webdriver.Chrome()
 driver.get('https://web.whatsapp.com/')
 inputan(driver)
 
 lagi = input('lagi? y/n : ')
 while lagi == 'y':
 	inputan(driver)
 else:
 	print('Thank you')

def inputan(driver):
 name = input('Masukan Nama atau Nama Group : ')
 msg = input('Pesan : ')
 count = int(input('Jumlah: '))

 input('Masuk ke mangsa lalu enter..,')

 user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
 user.click()
 
 # The classname of message box may vary.
 msg_box = driver.find_element_by_class_name('DuUXI')
  
 for i in range(count):
  msg_box.send_keys(msg)
  # The classname of send button may vary.
  # time.sleep(0.3)
  try:
  	button = driver.find_element_by_class_name('_2Ujuu')
  	button.click()
  except Exception as e:
  	pass
  else:
  	pass
  finally:
  	pass
 
 print('Success!!')
 time.sleep(1)	
banner()
main()
