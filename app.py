# import requests
import requests

# parser html
from bs4 import BeautifulSoup
import lxml


# يستخدم الريجس لاخذ جز من جمله اوكلمه او اي شي تبحث عنه 
# ساتطرق له بموضوع اخر
# علي سبيل المثال 
# alwatan.com الى http://alwatan.com 
domain_regx = '(?: |//|^)([A-Za-z0-9]{1,}\.[A-Za-z0-9]{1,10}\.?[A-Za-z]{1,}\.?[A-Za-z]{1,})(?: |/|$)'

sites = [
 'http://alwatan.com/',
'https://www.shabiba.com/',
'https://www.omandaily.om/',
 'https://alroya.om/']

# save files names
# we want to be able to open file
files = []
for ul in sites:
    raw = requests.get(ul)
    files.append('data/raw_site__data'+ str(len(ul))+'.txt')
    with open('data/raw_site__data'+ str(len(ul))+'.txt', 'a') as a_writer:
        try:
        # توجد طرق اخرى تسرع عمليه التجميع للبيانات 
        # في هذه الحاله تحليل المقالات المرغوبه
        #قد تكون بطيئه بعض الشي لكن بشكل عام في حاله اقل ٢٠ موقع لا اتوقع تكون مشكله
            soup = BeautifulSoup(raw.content, 'lxml')
            text = []
            
            # most tags with text
            for row in soup.findAll({'h2','h3', 'p'، 'a'}):
                text.append(row.text)
                a_writer.write(row.text)
            str1 = ''.join(str(e) for e in text)
            a_writer.write(str1)
            print(text)
        except Exception as err:
            print(err.args)
        finally:
            a_writer.close()




def read_raw_text(file, dic):
    with open(file, 'r') as reader:
        try:
            dic.append(reader.readlines())
        except Exception as err:
            print(err.args)
        finally:
            reader.close()
