import time  
import subprocess
import sys
import os
import platform
import yagmail
from getpass import getpass

def clean():
    system = platform.system().lower()
    
    if system == "windows":
        os.system('cls') 
    else:
        os.system('clear')

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    install("yagmail")
    
sender_email = input("Nhập email của bạn: ")
password = getpass("Nhập mật khẩu của bạn: ")  

try:
    yag = yagmail.SMTP(user=sender_email, password=password)
    print("Đăng nhập thành công!")
except Exception as e:
    print("Không thể đăng nhập. Kiểm tra email/mật khẩu hoặc bật quyền truy cập.")
    exit()

print("\nChọn loại gửi thư (chỉ áp dụng với gmail):")
print("1. Gửi một thư")
print("2. Spam Email")
option = input("Nhập lựa chọn (1 hoặc 2): ").strip()

if option == "1":
    receiver_email = input("Nhập email người nhận: ")
    subject = input("Nhập tiêu đề email: ")
    body = input("Nhập nội dung email: ")

    attachments = []
    add_attachment = input("Bạn có muốn đính kèm tệp? (y/n): ").lower()
    if add_attachment == 'y':
        while True:
            file_path = input("Nhập đường dẫn tệp (hoặc nhấn Enter để dừng): ")
            if file_path.strip():
                attachments.append(file_path)
            else:
                break

    try:
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=body,
            attachments=attachments if attachments else None
        )
        print("Email đã được gửi thành công!")
    except Exception as e:
        print("Không thể gửi email. Lỗi:", e)

elif option == "2":
    receiver_email = input("Nhập email người nhận: ")

    num_emails = int(input("Nhập số lượng email cần gửi: ").strip())

    delay = float(input("Nhập thời gian chờ giữa các lần gửi (giây): ").strip())

    base_subject = input("Nhập tiêu đề cơ bản của email: ")
    body = input("Nhập nội dung email: ")

    attachments = []
    add_attachment = input("Bạn có muốn đính kèm tệp? (y/n): ").lower()
    if add_attachment == 'y':
        while True:
            file_path = input("Nhập đường dẫn tệp (hoặc nhấn Enter để dừng): ")
            if file_path.strip():
                attachments.append(file_path)
            else:
                break

    success_count = 0  
    for i in range(num_emails):
        unique_subject = f"{base_subject} (#{i + 1})"

        try:
            yag.send(
                to=receiver_email,
                subject=unique_subject,
                contents=body,
                attachments=attachments if attachments else None
            )
            success_count += 1  
        except Exception as e:
            print(f"\nKhông thể gửi email thứ {i + 1}. Lỗi: {e}")

        print(f"\rSố email đã gửi: {success_count}/{num_emails}", end="")

        if i < num_emails - 1:
            time.sleep(delay)

    print("\nHoàn thành!")

else:
    print("Lựa chọn không hợp lệ. Thoát chương trình!")

if __name__ == "__main__":
    install_package("requests")
    clean()
