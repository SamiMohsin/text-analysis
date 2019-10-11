'''
The MIT License (MIT)

Copyright (c) 2019 Ayoob Alshahri

Permission is hereby granted, free of charge, to any person obtaining a copy of this 
software and associated documentation files (the "Software"), to deal in the Software 
without restriction, including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO 
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''

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

sites = []

'''

فقط كمثال

sites = [
'http://alwatan.com/',
'https://www.shabiba.com/',
'https://www.omandaily.om/',
 'https://alroya.om/']
 
'''

# الخطوه الاولى حفظ البيانات الى ملف من امتداد تكست
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
                # قم باضافتها الى المصفوفه تيكست
                text.append(row.text)
                #   يجب تحويل المصوفه الى من هيكل بياني الى نوع يسمى سترينج او نوع مدخلات رسوميه
                # ، الحل اسفل هذا الكود  مباشره
                #a_writer.write(row.text)
                # تحويل المصفوفه الى سترينج
            str1 = ''.join(str(e) for e in text)
            # قم بكتابه البيانات الى الملف 
            a_writer.write(str1)
            print(text)
        except Exception as err:
           # في حاله ظهور خطأ قم باظهار نوع الخطأ
            print(err.args)
        finally:
         # تاكد من اغلاق الامر رايتر
            a_writer.close()



# قراه ملف التكست
# لتفعيل ذلك يجب ان تقوم بصنع مصفوفه كمثال لذلك 
# example = []
# اكتب اسم الملف ثم اضف المصفوفه التس قمت بعملها كمثال ذلك 
# output = read_raw_text('data/example.txt', example)
def read_raw_text(file, dic):
    with open(file, 'r') as reader:
        try:
            dic.append(reader.readlines())
        except Exception as err:
            print(err.args)
        finally:
            reader.close()
