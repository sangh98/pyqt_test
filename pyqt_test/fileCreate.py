import os

# 폴더 경로 설정
folder_path = "txt"
os.makedirs(folder_path, exist_ok=True)  # 폴더가 없는 경우 생성합니다.

for i in range(1, 11):
    for j in range(1, 11):
        number1 = str(i).zfill(2)  # 숫자를 2자리로 만들기 위해 zfill() 함수를 사용합니다.
        number2 = str(j).zfill(2)
        filename = f"test{number1}{number2}.txt"
        filepath = os.path.join(folder_path, filename)  # 폴더 경로와 파일 이름을 결합합니다.

        with open(filepath, "w", encoding=("UTF-8")) as file:
            # 파일 작성 내용
            match number1:
                case "01":
                    file.write(f"fileName : {filename}\n")
                    file.write(f"입출력 {number2}번 문제")
                case "02":
                    file.write(f"fileName : {filename}\n")
                    file.write(f"조건문 {number2}번 문제")
                case "03":
                    file.write(f"fileName : {filename}\n")
                    file.write(f"반복문 {number2}번 문제")
                case "04":
                    file.write(f"fileName : {filename}\n")
                    file.write(f"배열 {number2}번 문제")
                case "05":
                    file.write(f"fileName : {filename}\n")
                    file.write(f"문자열 {number2}번 문제")

