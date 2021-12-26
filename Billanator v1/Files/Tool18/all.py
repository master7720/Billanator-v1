from multiprocessing.pool import ThreadPool
import requests
red = '\x1b[91m'
green = '\x1b[92m'
white = '\x1b[00m'

def cms(url):
    try:
        url = url.replace('\n', '').replace('\r', '')
        if url.startswith('http://'):
            url = url.replace('http://', '')
        elif url.startswith('https://'):
            url = url.replace('https://', '')
        op = requests.get('http://' + url + '/admin/', timeout=10)
        op2 = requests.get('http://' + url + '/administrator/index.php', timeout=10)
        op3 = requests.get('http://' + url + '/wp-login.php', timeout=10)
        op4 = requests.get('http://' + url + '/user/login', timeout=10)
        op5 = requests.get('http://' + url, timeout=5)
        op6 = requests.get('http://' + url + '/vendor/phpunit/phpunit/phpunit.xml', timeout=10)
        op7 = requests.get('http://' + url + '/admin/images/cal_date_over.gif', timeout=10)
        op8 = requests.get('http://' + url + '/application/configs/application.ini', timeout=10)
        op9 = requests.get('http://' + url, timeout=10)
        op10 = requests.get('http://' + url, timeout=10)
        op11 = requests.get('http://' + url + '/wp-admin/install.php?step=1', timeout=10)
        op12 = requests.get('http://' + url + '/wp/wp-admin/install.php?step=1', timeout=10)
        op13 = requests.get('http://' + url + '/blog/wp-admin/install.php?step=1', timeout=10)
        if ('dashboard' or 'opencart') in op.text:
            print(green + '[>>] OpenCart http://' + url + white + '\033[0m\n')
            open('Cms/opencart-cms.txt', 'a').write('http://' + url + '\n')
        elif 'Joomla' in op2.text:
            print(green + '[>>] Joomla http://' + url + white + '\033[0m\n')
            open('Cms/joomla-cms.txt', 'a').write('http://' + url + '\n')
        elif 'WordPress' in op3.text:
            print(green + '[>>] Wordpress http://' + url + white + '\033[0m\n')
            open('Cms/wordpress-cms.txt', 'a').write('http://' + url + '\n')
        elif 'sites/default' in op4.text:
            print(green + '[>>] Drupal http://' + url + white + '\033[0m\n')
            open('Cms/drupal-cms.txt', 'a').write('http://' + url + '\n')
        elif 'PrestaShop' in op5.text:
            print(green + '[>>] Prestashop http://' + url + white + '\033[0m\n')
            open('Cms/prestashop-cms.txt', 'a').write('http://' + url + '\n')
        elif 'PHPUNIT_TESTSUITE' in op6.text:
            print(green + '[>>] Laravel Site http://' + url + white + '\033[0m\n')
            open('Cms/laravel-fm.txt', 'a').write('http://' + url + '\n')
        elif 'GIF89a' in op7.text:
            print(green + '[>>] OsCommerce http://' + url + white + '\033[0m\n')
            open('Cms/oScommerce-cms.txt', 'a').write('http://' + url + '\n')
        elif 'APPLICATION_PATH' in op8.text:
            print(green + '[>>] ZenCms http://' + url + white + '\033[0m\n')
            open('Cms/zen-cms.txt', 'a').write('http://' + url + '\n')
        elif 'Magento' in op9.text:
            print(green + '[>>] Magento http://' + url + white + '\033[0m\n')
            open('Cms/magento-cms.txt', 'a').write('http://' + url + '\n')
        elif 'vBulletin' in op10.text:
            print(green + '[>>] vBulletin http://' + url + white + '\033[0m\n')
            open('Cms/vbulletin-cms.txt', 'a').write('http://' + url + '\n')
        elif 'First Step' in op11.text:
            print(green + '[>>] Wp Install http://' + url + white + '\033[0m\n')
            open('Cms/wp-install.txt', 'a').write('http://' + url + '/wp-admin/install.php?step=1\n')
        elif 'First Step' in op12.text:
            print(green + '[>>] Wp Install http://' + url + white + '\033[0m\n')
            open('Cms/wp-install.txt', 'a').write('http://' + url + '/wp/wp-admin/install.php?step=1\n')
        elif 'First Step' in op13.text:
            print(green + '[>>] Wp Install http://' + url + white + '\033[0m\n')
            open('Cms/wp-install.txt', 'a').write('http://' + url + '/blog/wp-admin/install.php?step=1\n')
        else:
            print('[xx] Cms Not Found >>> http://' + red + url + '\033[0m\n')
            open('Cms/cms-not-found.txt', 'a').write('http://' + url + '\n')
    except:
        pass


banner =  '''
  ____  _ _ _                   _             
 |  _ \(_) | |   DavidBilla    | |            
 | |_) |_| | | __ _ _ __   __ _| |_ ___  _ __ 
 |  _ <| | | |/ _` | '_ \ / _` | __/ _ \| '__|
 | |_) | | | | (_| | | | | (_| | || (_) | |   
 |____/|_|_|_|\__,_|_| |_|\__,_|\__\___/|_|   
                                              
   CMS Scanner + Laravel Site Scanner + Wp Install Scanner 
'''
print(banner)

DavidBilla = open(input('root@DavidBilla:~# Give list : '), 'r').readlines()
DB = input('root@DavidBilla:~# thread : ')
pool = ThreadPool(int(DB))
pool.map(cms, DavidBilla)
pool.close()
pool.join()
if __name__ == '__main__':
    print('\x1b[97mSuccess Scan !! Check Folder /Cms')
