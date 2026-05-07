import codecs
import re

# 1. Read product_etc.html to extract bf_content
with codecs.open(r"c:\Users\kangdo\tobesmart-website\product_etc.html", 'r', 'utf-8') as f:
    etc_html = f.read()

b_match = re.search(r'<div id="tabContent-barrierfree"[^>]*>([\s\S]*?)</div>\s*<div id="tabContent-donation"', etc_html)
if not b_match:
    # try another way
    b_match = re.search(r'(<!-- Intro / Overview -->[\s\S]*?)</div>\s*<div id="tabContent-donation"', etc_html)
if not b_match:
    # Just read the whole thing
    b_match = re.search(r'<!-- Tab Contents -->\s*<div id="tabContent-barrierfree"[^>]*>\s*([\s\S]*?)\s*</div>\s*<div id="tabContent-donation"', etc_html)

# Since etc_html was updated, barrierfree is the very first tabContent.
if b_match:
    bf_content = b_match.group(1).strip()
else:
    # fallback Regex
    b_match = re.search(r'<div id="tabContent-barrierfree"[^>]*>([\s\S]*?)</div>\s*<div id="tabContent-', etc_html)
    bf_content = b_match.group(1).strip()

# 2. Modify the terminology for Study Cafe
bf_title = r'누구나 불편없이, 모두가 쉽게 이용할 수 있는<br>투비스마트 배리어프리 키오스크'
sc_title = '스터디카페와 독서실에 최적화된<br>투비스마트 스터디카페 솔루션'

bf_desc_pattern = r'장애인, 어린이, 고령층, 사회적 약자등 모두가 편리하게 사용할 수 있도록.*?기능을 제공합니다\.'
sc_desc = '스터디카페와 독서실의 무인 운영을 극대화할 수 있도록<br class="br-pc">\\n                        안정적이고 직관적인 결제 및 예약 시스템이 결합된 키오스크로,<br class="br-pc">\\n                        좌석 선택/ 시간 연장/ 입퇴실 관리/ 빈틈없는 매출 관리 기능을 제공합니다.'

sc_content = bf_content.replace(
    '누구나 불편없이, 모두가 쉽게 이용할 수 있는<br>투비스마트 배리어프리 키오스크', 
    sc_title
).replace(
    '누구나 불편없이, 모두가 쉽게 이용할 수 있는<br>\\n                        투비스마트 배리어프리 키오스크', 
    sc_title
)
sc_content = re.sub(bf_desc_pattern, sc_desc, sc_content, flags=re.DOTALL)

# 3. Read product_space.html
filename_space = r"c:\Users\kangdo\tobesmart-website\product_space.html"
with codecs.open(filename_space, 'r', 'utf-8') as f:
    space_html = f.read()

# 4. Replace the content inside #tabContent-studycafe
sc_pattern = r'(<div id="tabContent-studycafe"[^>]*>)([\s\S]*?)(</div>\s*<div id="tabContent-office")'
new_space_html = re.sub(sc_pattern, r'\1\n' + sc_content + r'\n\3', space_html)

with codecs.open(filename_space, 'w', 'utf-8') as f:
    f.write(new_space_html)

print("Updated product_space.html successfully")
