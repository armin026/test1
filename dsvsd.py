import os
import time
import sys
import random

# تلاش برای گرفتن ابعاد ترمینال، در غیر این صورت مقدار پیش‌فرض
try:
    TERM_WIDTH = os.get_terminal_size().columns
    TERM_HEIGHT = os.get_terminal_size().lines
except OSError:
    TERM_WIDTH = 80  # مقدار پیش‌فرض
    TERM_HEIGHT = 24  # مقدار پیش‌فرض

# متن ASCII Art اصلی (بزرگ‌تر و زیباتر با بنفش)
ART = """
                                                            
                     ..','.        ....                     
                 .,;;;,...::.    .:;,,;;:;'.                
              .,;;,,,,,.  ;c.    'c.  .'',;::,.             
           .';;,,'',,,;:.'l,,;;;,,l;..c,,,,,,;::'.          
         .,:,,'.',.. .cl::,.......';:co'...,'.,;;:,.        
        ':',,..;.  .;;'.              .;c;...;'.';,:,.      
      .:;.;' .:...:;..';;;.        .,;;'.'c;..;'..;';:.     
     .c,..;. .';co..;:;;,;l.      .l,,;:c,.;l;,.  ';.'c.    
     'c. .',,,:lo..l:::;;;l.      .o;;;::cc.,o:,,,,'  ,c.   
     .::;;;;;,'o..l:;:::;l'        ;l;:::;cc.;o::;,'.':;.   
        ..    ;l:,l;;;;:c'          ;c;;;;;o',l'....'..     
             .cocco:;::,.            .:c:,;d:oc;.           
             .co;.,oc,..              ..:ll..lc;.           
              ,oc..:.,;::,'........';;;;'';.,cl.            
              .ll;':.  .:'',,;cc;,,':.   .;'l:c.            
               'l:c:.  .:.   .;,   .:.   .cc,l.             
                .c;:;...:.   .:'   .;'..,:,;c.              
                 .;:,;:;c'.  .:'. ..::;;'':,.               
                   .;:,'';;;;;c:;;;;,..,;,.                 
                     ..;::;,''..'',;;;,.                    
                          ...',,'...                        
                                                            
                                                            
                                                            
                                                              
"""

# محاسبه عرض و ارتفاع متن
LINES = ART.count('\n')
MAX_WIDTH = max(len(line) for line in ART.split('\n') if line.strip())
PADDING_X = (TERM_WIDTH - MAX_WIDTH) // 2
PADDING_Y = (TERM_HEIGHT - LINES) // 2

# تابع برای پر کردن فضای عمودی
def print_padding():
    for _ in range(PADDING_Y):
        print()

# نمایش اولیه متن مرکز شده
print_padding()
for line in ART.split('\n'):
    if line.strip():
        print(f"\x1b[35m{' ' * PADDING_X}{line}\x1b[0m")
print("\x1b[0m", end='')  # ریست رنگ

# لیست متن‌های هکری برای انیمیشن
HACKER_TEXTS = [
    ["[BREACH: 10%]", "0x1A B9", "*SCANNING*", "[LOCK: ON]", f"DATE: 23/10/25"],
    ["[LOAD: 30%] ==|", "XY9 87", "*DECODE*", "[FLOW: 25%]", f"TIME: 10:58 PM"],
    ["[HACK: 60%] ||", "543 21", "*BYPASS*", "[LEVEL: 3]", "CRACK: 50%"],
    ["[OWNED: 100%]", "AB0 CD", "*DOMINATE*", "[CONTROL: MAX]", "ROOT: ON"],
    ["[TRACE: 5%]", "DC98 7", "*DESTRUCT*", "[SHUT: 15%]", "EXIT: NOW"]
]

# موقعیت‌های مختلف برای متن‌ها
POSITIONS = [
    (2, 5), (4, 10), (6, 15), (8, 20),  # بالا چپ
    (2, TERM_WIDTH - 20), (4, TERM_WIDTH - 25), (6, TERM_WIDTH - 30), (8, TERM_WIDTH - 35),  # بالا راست
    (PADDING_Y + LINES + 2, 5), (PADDING_Y + LINES + 4, 10), (PADDING_Y + LINES + 6, 15),  # زیر چپ
    (PADDING_Y + LINES + 2, TERM_WIDTH - 20)  # زیر راست
]

try:
    while True:
        for texts in HACKER_TEXTS:
            for j, (pos_y, pos_x) in enumerate(POSITIONS):
                if j < len(texts):  # مطمئن می‌شیم اندیس معتبر باشه
                    os.system(f'tput cup {pos_y} {pos_x}')
                    print(f"\x1b[31m{texts[j]}\x1b[0m", end='\r')
            # متن رندوم اضافی
            rand_y = random.randint(10, TERM_HEIGHT - 10)
            rand_x = random.randint(5, TERM_WIDTH - 15)
            os.system(f'tput cup {rand_y} {rand_x}')
            print(f"\x1b[31m[CODE: {random.randint(100, 999)}]\x1b[0m", end='\r')
            time.sleep(0.2)
except KeyboardInterrupt:
    print("\x1b[0m")  # ریست رنگ در صورت خروج
