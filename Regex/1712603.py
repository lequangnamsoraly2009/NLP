import re
import os.path

# Trích xuất theo đầu số VN
def ValidPhoneNumber(phone_numbers):
    # Thực nghiệm trích xuất theo đầu số hiện tại của VN - các đầu số của VN nằm trong file format
    # Nguồn Phone Number VN: https://en.wikipedia.org/wiki/Telephone_numbers_in_Vietnam
     valid_phoneNumber = []
     if not os.path.isfile('VNPhone_numbers_format.txt'):
          print('File is not exist')
     else:
          with open('VNPhone_numbers_format.txt','r') as f:
               VNphone_numbers = f.read()   
          for pn in phone_numbers:
                #   Bỏ số 0 ở đầu và lấy 2 số sau 
               if pn[0] == '0' and (pn[1:3] in VNphone_numbers):
                    valid_phoneNumber.append(pn)
                # Bỏ dấu + và 84 lấy 2 số sau 84
               elif pn[0] == '+' and (pn[3:5] in VNphone_numbers):
                    valid_phoneNumber.append(pn)
     return valid_phoneNumber


def extract_data(text):
     emails = re.findall('[\w\.-]+@[\w\.-]+\.\w{2,5}', text)
     phone_numbers = re.findall('(?:\+84|0)[3|5|7|8|9]\d{8}',text)
     urls = re.findall('https?://[^\s]+', text)
     return emails, phone_numbers, urls


def main():
     ifile = input('Type input file *.txt: ')
     if not os.path.isfile(ifile):
          print('File is not exist')
     else:
          emails,phone_numbers,urls = [],[],[]
          with open(ifile,'r') as f:
               text = f.read()
          emails, phone_numbers, urls = extract_data(text)
          if not emails and not phone_numbers and not urls:
               print('File is not have emails or phone numbers or links')
          else:
               # print(emails, phone_numbers,urls,text)
               phone_numbers = ValidPhoneNumber(phone_numbers)

               list_tuple = list()
               for e in emails:
                    thistuple = list()
                    thistuple += text.find(e), len(e), e
                    list_tuple.append(tuple(thistuple))
               for pn in phone_numbers:
                    thistuple = list()
                    thistuple += text.find(pn), len(pn), pn
                    list_tuple.append(tuple(thistuple))
               for url in urls:
                    thistuple = list()
                    thistuple += text.find(url), len(url), url
                    list_tuple.append(tuple(thistuple))

               for tup in list_tuple:
                    print(tup)
                    
if __name__ == "__main__":
     main()