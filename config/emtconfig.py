from selenium.webdriver.common.by import By

# 页面元素
ELEMENT = {
    # 首页元素
    '首页右侧登录按钮': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div/div[3]/a[1]'),

    # 登录界面元素
    '账号输入框': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div[2]/div/div[3]/form/div[1]/div/div/input'),
    '密码输入框': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div[2]/div/div[3]/form/div[2]/div/div/input'),
    '登录按钮': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div'),
    '确认按钮': (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span'),

    # 管理中心元素
    '首页管理中心按钮': (By.XPATH, "//*[@id='jmod_topbar']//*/a[text()='管理中心']"),
    '应用管理中心更新安装包按钮': (By.XPATH, "/html/body//*/a[text()='更新安装包']"),

    # 应用详情页元素
    '点击上传按钮': (By.XPATH, "//*[@id='j-apk-box']//*/p[text()='更新安装包']"),
    '应用更新说明文本框': (By.XPATH, "//*[@id='j-apk-box']//*/textarea"),
    '提交审核按钮': (By.ID, "j-submit-btn"),
    '确认提交审核': (By.ID, "j-confirm-yes"),
}
