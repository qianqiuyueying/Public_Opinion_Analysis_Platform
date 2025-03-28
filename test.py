from DrissionPage import Chromium
from DrissionPage.common import Keys

chromium = Chromium(30333)
tab = chromium.latest_tab
ele = tab.ele('c=#sliderVideo > div.UsWJJZhB.playerContainer.hide-animation-if-not-suport-gpu.jjWFxVjy.Kk4V1N2A.dOluRUuw > div.O8onIiBq.slider-video.RgxaVMyR > div > div.MarSXdLE.YmptQEz6.positionBox > div.jkfSVWLT > div:nth-child(2) > div')
print(ele.text)