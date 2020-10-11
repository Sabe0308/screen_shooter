#ライブラリのインポート
from selenium import webdriver
import time
import os

# Chromeを設定,準備
options= webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver_path = os.getcwd() + '\chromedriver.exe'

#変数の初期化
counter = 1
filename = input('保存するファイル名を指定してください（複数の場合は連番で取得します）：')

#処理部
with open('links.csv', 'r') as f:
    print("links.csvファイルに記入されているURLを読み込みます")
    for line in f:
        # ブラウザ起動
        driver = webdriver.Chrome(driver_path, options=options)
        driver.execute_script("document.body.style.overflow = 'hidden';")
        driver.get(line)
        #１秒待機
        time.sleep(1)

        #画像取得
        page_width = driver.execute_script('return document.body.scrollWidth')
        page_height = driver.execute_script('return document.body.scrollHeight')
        driver.set_window_size(page_width, page_height)
        driver.save_screenshot(filename +'_'+ str(counter) + '.png')
        driver.close()
        print(str(counter) + 'ファイル目の取得が正常終了しました')
        counter = counter + 1

driver.quit()
exit()
