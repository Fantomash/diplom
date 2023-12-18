from selenium.webdriver.common.by import By


class BasePageLocators:
    MAIN_LOGO = 'c13cw3wj' #class
    ROOMS_ICON = '//*[@id="categoryScroller"]/div/div/div/div[3]/div/div/div/div/label[1]/div'
    VIEWS_ICON = '//*[@id="categoryScroller"]/div/div/div/div[3]/div/div/div/div/label[2]/div'
    CABIN_ICON = '//*[@id="categoryScroller"]/div/div/div/div[3]/div/div/div/div/label[3]/div'
    FILTER = 'bocjyl3' #class
    LANG_ICON = '/html/body/div[5]/div/div/div[1]/div/div[3]/div[2]/div/div/div/header/div/div[3]/nav/div[1]/div/button'
    NEW_LANG = '//*[@id="panel--language_region_and_currency--0"]/section[2]/div/ul/li[5]'
    MAIN_NAVIGATION_MENU = 'cnky2vc'  # class
    MENU_EXPANDED = "//div[@id='simple-header-profile-menu']"
    GIFT_CARD_MENU_ITEM = "//*[contains(text(), 'Gift cards')]"
    LOGIN_MENU_ITEM = "//*[contains(text(), 'Log in')]"
    SUPPORT_TITLE = '//*[@id="site-content"]/div[3]/div[2]/footer/div/div/div[1]/section[1]/h3'
    INSPIRATION_TABS = './/div[@role="tablist"]/button'
    CROSS_POPUP_BUTTON = '/html/body/div[10]/div/section/div/div/div[2]/div/div[4]/div'
    TABLIST = './/div[@role="tablist"]/button'
    FILTER_HEADER = 'h11o5x9p' #class


class LoginLocators:
    LOGIN_WITH_GOOGLE = '/html/body/div[11]/section/div/div/div[2]/div/div[2]/div/div[3]/div/div[2]/form/button'
    EMAIL_INPUT = 'identifierId' #id
    NEXT_BUTTON_LOGIN = 'identifierNext' #id
    NEXT_BUTTON_PASSWORD = '//*[@id="passwordNext"]/div/button/span'
    PASSWORD_INPUT = '//*[@id="password"]/div[1]/div/div[1]/input'
    PERSONAL_DATA = '_184uai1' #class

