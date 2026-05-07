import codecs
import re

filename = r"c:\Users\kangdo\tobesmart-website\product_etc.html"
with codecs.open(filename, 'r', 'utf-8') as f:
    html = f.read()

# 1. Reorder the tabs
new_tabs = '''<ul class="page-tabs" id="pageTabs">
                    <li class="active"><a href="#barrierfree">배리어프리 키오스크</a></li>
                    <li ><a href="#donation">기부금 키오스크</a></li>
                    <li ><a href="#education">교육용 키오스크</a></li>
                </ul>'''

html = re.sub(
    r'<ul class="page-tabs" id="pageTabs">[\s\S]*?</ul>',
    new_tabs,
    html
)

# 2. Extract Barrier-free content
b_match = re.search(r'(<!-- Intro / Overview -->[\s\S]*?)</div>\s*</main>', html)
bf_content = b_match.group(1)

# Ensure bf_content is clean of trailing divs from the tab content block
bf_content = re.sub(r'</div>$', '', bf_content.strip()) # strip last </div> if captured

# Let's create new contents
donation_content = bf_content.replace('배리어프리', '기부금').replace('배리어 프리', '기부금')
education_content = bf_content.replace('배리어프리', '교육용').replace('배리어 프리', '교육용')

# Create specific descriptions using regex to avoid whitespace issues
bf_desc_pattern = r'장애인, 어린이, 고령층, 사회적 약자등 모두가 편리하게 사용할 수 있도록.*?기능을 제공합니다\.'

don_desc = '투명하고 안전하게 기부금을 관리할 수 있도록<br class="br-pc">\\n                        편리하고 직관적인 UI를 제공하는 키오스크로,<br class="br-pc">\\n                        다양한 결제 수단과 실시간 기부 내역 확인 기능을 제공합니다.'

edu_desc = '어린이부터 어르신까지 쉽게 학습하고 체험할 수 있도록<br class="br-pc">\\n                        교육 목적으로 특화된 멀티미디어 키오스크로,<br class="br-pc">\\n                        다양한 학습용 콘텐츠와 직관적인 터치 인터페이스를 제공합니다.'

donation_content = re.sub(bf_desc_pattern, don_desc, donation_content, flags=re.DOTALL)
education_content = re.sub(bf_desc_pattern, edu_desc, education_content, flags=re.DOTALL)

# Reassemble the whole Tab Contents part
new_tab_contents = f'''
        <!-- Tab Contents -->
        <div id="tabContent-barrierfree" class="tab-content-block" style="display: block; padding: 60px 0;">
            {bf_content}
        </div>
        <div id="tabContent-donation" class="tab-content-block" style="display: none; padding: 60px 0;">
            {donation_content}
        </div>
        <div id="tabContent-education" class="tab-content-block" style="display: none; padding: 60px 0;">
            {education_content}
        </div>
'''

# Replace from <!-- Tab Contents --> to </main>
html = re.sub(r'<!-- Tab Contents -->[\s\S]*?</main>', new_tab_contents + '\\n    </main>', html)

with codecs.open(filename, 'w', 'utf-8') as f:
    f.write(html)
print("Updated successfully")
