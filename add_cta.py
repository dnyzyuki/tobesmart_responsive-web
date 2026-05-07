import os
import re

target_dir = r"c:\Users\kangdo\tobesmart-website"
files_to_check = ['product_space.html', 'index.html', 'space_cube.html']

cta_html = '''
            <!-- CTA Button -->
            <div style="text-align: center; margin-top: 80px; margin-bottom: 20px;" class="reveal">
                <a href="https://smartstore.naver.com/tobesmart2014/category/ALL?cp=1" target="_blank" class="btn btn-primary" style="padding: 18px 50px; font-size: 20px; border-radius: 50px; box-shadow: 0 10px 25px rgba(0, 136, 203, 0.3);">
                    <i class="fas fa-shopping-cart" style="margin-right: 10px;"></i> 바로 구매하기
                </a>
            </div>
'''

for file in files_to_check:
    filepath = os.path.join(target_dir, file)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the section containing "1,500개 이상의 매장"
    # The structure starts around <section> or <section class="..."> and ends at </section>
    
    # Let's match from "1,500개 이상의 매장" to the very next </section>
    # To replace, we can insert our cta_html right before that </section>
    
    # We use a trick: match the start string up to </section>, and capture it.
    pattern = r'(1,500개 이상의 매장[\s\S]*?)(</section>)'
    
    # Check if we already inserted it
    if "https://smartstore.naver.com/tobesmart2014/category/ALL?cp=1" in content:
        print(f"Skipped {file} - CTA already exists")
        continue

    def replacer(match):
        return match.group(1) + cta_html + match.group(2)

    new_content, count = re.subn(pattern, replacer, content, count=1)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"Pattern not found in {file}")
