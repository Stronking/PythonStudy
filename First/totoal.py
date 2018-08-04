from selenium import webdriver
import time
import csv

def main():
    opt = webdriver.ChromeOptions()
    opt.set_headless()
    driver = webdriver.Chrome(options=opt)
    for i in range(1,3559):
        url = 'https://etherscan.io/token/generic-tokentxns2?contractAddress=0xb53ac311087965d9e085515efbe1380b2ca4de9a&mode=&p='+str(i)
        driver.get(url)
        time.sleep(1)
        print('第'+str(i)+'页')
        for n in range(2,27):
            try:
                txhash = driver.find_element_by_xpath("//table[@class='table']//tbody//tr["+str(n)+"]//td[1]").text
                age = driver.find_element_by_xpath("//table[@class='table']//tbody//tr["+str(n)+"]//td[2]").text
                fm = driver.find_element_by_xpath("//table[@class='table']//tbody//tr["+str(n)+"]//td[3]").text
                to = driver.find_element_by_xpath("//table[@class='table']//tbody//tr["+str(n)+"]//td[5]").text
                quantity = driver.find_element_by_xpath("//table[@class='table']//tbody//tr["+str(n)+"]//td[6]").text
                with open('token_transfers.txt', 'a') as f:
                    f.write(str(txhash)+'      '+str(age)+'       '+str(fm)+'      '+str(to)+'      '+str(quantity)+'\n')
            except:
                print('程序结束')
        with open('token_transfers.txt', 'a') as f:
            f.write('第'+str(i)+'页\n'+'\n')


if __name__ =="__main__":
    main()
