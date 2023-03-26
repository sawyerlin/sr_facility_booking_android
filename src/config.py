TIME_OUT = 50

DESIRED_CAPABILITIES = {
    'appium:platformName': 'Android',
    'appium:deviceName': 'emulator-5554',
    'appium:appPackage': 'com.fermax',
    'appium:appActivity': 'com.fermax.activities.SplashActivity',
    'appium:autoGrantPermissions': True,
    'appium:newCommandTimeout': 600
}

FACILITIY_SCROLL_MAPPING = {
    'tennis': 4
}