from selenium.webdriver.common.by import By

class Locators:
    PROFILE_BUTTON = (By.XPATH, '//p[contains(text(), "Личный Кабинет")]') #селектор кнопки личный кабинет
    REGISTR_BUTTON = (By.XPATH,'//a[contains(text(), "Зарегистрироваться")]') #селектор кнопки зарегистрироваться
    NAME_REGISTRATION = (By.XPATH, '//label[text()="Имя"]/following-sibling::*') #селектор поля ввода имени при регистрации
    EMAIL_REGISTRATION = (By.XPATH, '//label[text()="Email"]/following-sibling::*') #селектор поля почты при регистрации
    PASSWORD_REGISTRATION = (By.XPATH, '//label[text()="Пароль"]/following-sibling::*') #селектор поля пароля при регистрации
    SUBMIT_REGISTR_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") #селектор кнопки регистрации
    INCORRECT_PASS_MESSEGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]") #селектор поп-апа неверного пароля

    PROFILE_NAME_FAKE = (By.XPATH, "//li[1]/div/div/input")
    PROFILE_EMAIL_FAKE = (By.XPATH, "//li[2]/div/div/input")

    EMAIL_LOGIN = (By.XPATH, '//label[text()="Email"]/following-sibling::*') #селектор поля почты при авторизации
    PASSWORD_LOGIN = (By.XPATH, '//input[@name="Пароль"]') #селектор поля пароля при авторизации
    PROFILE_BUTTON_ENTER = (By.XPATH, '//button[contains(text(), "Войти")]') #селектор кнопки входа в аккаунт на странице /login

    PROFILE_NAME = (By.XPATH, '//input[@value="Mikhail"]')#имя профиля в личном кабинете
    PROFILE_EMAIL = (By.XPATH, '//input[@value="teststashenok5@ya.ru"]')#email профиля в личном кабинете

    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']") #селектор кнопки "Войти в аккаунт" на главной странице

    LOGIN_BUTTON_REGISTRATION_PAGE = (By.XPATH, "//a[text()='Войти']") #селектор кнопки перехода к авторизации в форме регистрации
    RESTORE_PASS_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']") #селектор кнопки восстановления пароля
    RESTORE_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Восстановить']") #селектор кнопки подтверждения восстаглвления пароля
    RESTORE_PASS_INPUT_FIELD = (By.XPATH, '//input[@name="name"]') #селектор поля ввода почты на странице восстановления пароля
    RESTORE_PASS_HEADER_WORD = (By.XPATH, "//h2[text()='Восстановление пароля']") #селектор текста на странице восставновления пароля
    RESTORE_PASS_CONFIRM_BUTTON_END = (By.XPATH, "//button[text()='Восстановить']") #селектор кнопки восставноить после ввода email
    RESTORE_PASS_INPUT_NEW_PASS_FIELD = (By.XPATH, "//input[@name='Введите новый пароль']") #селектор поля ввода нового пароля
    RESTORE_PASS_VISIBILITY = (By.XPATH, "//div[@class='input__icon input__icon-action']") #селектор кнопки видимости пароля
    RESTORE_PASS_UNVISIBLE = (By.XPATH, '//input[@name="Введите новый пароль"]')


    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")#селектор кнопки конструктора в личном кабинете

    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")#селектор кнопки выхода из аккаунта
    INGREDIENT_BRED_MENU = (By.XPATH, "//span[text()='Булки']")#селектор раздела булки
    INGREDIENT_SOUSE_MENU = (By.XPATH, "//span[text()='Соусы']")#селектор раздела соус
    INGREDIENT_FILING_MENU = (By.XPATH, "//span[text()='Начинки']")  # селектор раздела начинка

    INGREDIENT_BRED_LIST = (By.XPATH, "//h2[text()='Булки']")#селектор булки
    INGREDIENT_SOUSE_LIST = (By.XPATH, "//h2[text()='Соусы']")#селектор соус
    INGREDIENT_FILING_LIST = (By.XPATH, "//h2[text()='Начинки']")  # селектор начинка

    PERSONAL_ACCOUNT_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']") # селектор история заказов в личном кабинете
    PERSONAL_ACCOUNT_HISTORY_LIST = (By.XPATH,"//div[@class='OrderHistory_orderHistory__qy1VB']") #список истории заказов


    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")# селектор кнопки ленты заказов
    ORDER_FEED_HEADER_TEXT = (By.XPATH, "//div/h1[text()='Лента заказов']")# селектор текста хедера ленты заказов
    ORDER_CONSTRUCTOR_HEADER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")# селектор текста хедера конструктора

    CRATOR_BUN = (By.XPATH, "//img[@alt='Краторная булка N-200i']") # селектор краторной булки
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']") # селектор текста в пап апе любой булки
    INGREDIENT_NAME = (By.XPATH, "//div/p[text()='Краторная булка N-200i']") # селектор текста краторной булки
    INGREDIENT_POP_UP_CLOSE = (By.XPATH, "//div/section[1]/div[1]/button")# селектор кнопки закрытия ингредиента
    INGREDIENT_CONTEXT_WINDOW = (By.XPATH, '//div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]') # селектор контекстоного окна

    TARGET_BASKET = (By.XPATH, "//div/main/section[2]/ul/li[1]")# селектор корзины
    INGREDIENT_TOTAL_NUMBER = (By.XPATH, "//ul[1]/a[2]/div[1]/p")# селектор поля счетчик ингредиента
    ORDER_CREATED_TEXT = (By.XPATH, "//p[text()='идентификатор заказа']")# селектор текста об успешном создании заказа
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")# селектор кнопки создать заказ
    ORDER_CONTAINER = (By.XPATH, '//*[@id="root"]/div/section/div[1]') #order container

    TOP_ORDER_IN_FEED = (By.XPATH, "//main/div/div/ul/li[1]")# селектор верхнего заказа в ленте заказов
    ORDER_DETAILS_WINDOW_FEED = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']") # селектор всплывающего окна с деталями заказа
    ORDER_NUMBER_HISTORY = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[1]/a/div[1]/p[1]')# селектор номера заказа в истории
    CLOSE_ORDER = (By.XPATH, "//div/section/div[1]/button")# селектор кнопки закрытия заказа
    ORDER_FEED_NUMBER = (By.XPATH, "//li[1]/a/div[1]/p[1]")# селектор номера заказа в ленте
    ALL_TIME_ORDERS_NUMBER = (By.XPATH, "//div/div[2]/p[2][@class='OrderFeed_number__2MbrQ text text_type_digits-large']")#заказы за все время
    TODAY_ORDERS_NUMBER = (By.XPATH, "//div[3]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")# селектор селектор заказов сегодня
    ORDER_IN_PROGRESS = (By.XPATH, "//div/div[1]/div[1]/div[1]/ul[2]/li[1][@class='text text_type_digits-default mb-2']")# селектор поля заказа в работе

    START_PAGE_OVERLAY= (By.XPATH, "//div/section/div[2]")  # селектор overlay

    PRELOADER_ANIMATION = (By.XPATH, '//*[@id="root"]/div/div/img')
    GENERAL_OVERLAY = (By.XPATH, '//*[@id="root"]/div/div/div')
    LOADING_HISTORY = (By.XPATH, "//div/main/div/div/div[text()='Загрузка...']")
    MODAL_OVERLAY = (By.XPATH, '//div/div[@class="Modal_modal_overlay__x2ZCr"]')