TIME_OUT = 25

DESIRED_CAPABILITIES = {
    'appium:platformName': 'Android',
    'appium:deviceName': 'emulator-5554',
    # 'appium:deviceName': '5JPDU17531000393',
    'appium:appPackage': 'com.fermax',
    'appium:appActivity': 'com.fermax.activities.SplashActivity',
    'appium:autoGrantPermissions': True,
    'appium:newCommandTimeout': 600,
}

FACILITIY_SCROLL_MAPPING = {
    'fr': 0,
    'tennis': 4
}

FACILITIY_NAME_MAPPING = {
    'fr': 'Function Room',
    'tennis': 'Tennis Court'
}