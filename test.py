from DrissionPage import SessionPage

session = SessionPage()
data = session.get("https://www.baidu.com")
print(data)