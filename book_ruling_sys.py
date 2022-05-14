with open("c:/input.txt","rt",encoding='UTF8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip() #줄 끝의 줄 바꿈 문자를 제거한다.
        print(line)
        #lines는 도서목록을 담고있는 리스트가 된다.
#도서목록을 담고 있는 리스트 : lines
class bookruling_sys:
    #1. 도서목록 추가 함수    
    def add_book():
        print("\n[도서목록 추가]\n")
            #자동으로 파일을열고 닫음
    
        with open("c:/input.txt","at",encoding='UTF8') as infile:
            print("[추가할 도서명 / 저자 / 출판년도 / 출판사 / 장르] 순으로 입력.")   
            new_line = input("새로운 정보 입력: ")
            infile.write("\n")
            infile.write(new_line)

    #2. 도서검색 함수_도서명, 장르 이런것데 관계있는 것들 싹다 반환 
    # 리스트에 해당 줄을 싹다 반환하는 함수___#3 #4 함수에서호출 할 수 있도록 하자!!   
    def find_book():
        print("\n[도서검색]\n")
        with open("c:/input.txt","rt",encoding='UTF8') as infile:
            print("찾을 정보 분류\n[1.도서명, 2.저자, 3.출판년도, 4.출판사, 5.장르]")
            number = int(input("분류 번호 입력 : "))
            if number == 1:
                informat_of_book_1 = input("검색할 도서이름 :")
                infiles = infile.readlines()
                infiles = [line.rstrip("\n") for line in infiles]#리스트가 아닌 infile을 리스트인 infiles로 바꾼다
                for i in range(len(infiles)):
                    if informat_of_book_1 in infiles[i]:
                        print("실행하는중")
                        print(infiles[i])
            elif number == 2:
                informat_of_book_2 = input("검색할 저자 :")
                infiles = infile.readlines()
                infiles = [line.rstrip("\n") for line in infiles]
                for i in range(len(infiles)):
                    if informat_of_book_2 in infiles[i]:
                        print(infiles[i])
            elif number == 3:
                informat_of_book_3 = input("검색할 출판년도 :")
                infiles = infile.readlines()
                infiles = [line.rstrip("\n") for line in infiles]
                for i in range(len(infiles)):
                    if informat_of_book_3 in infiles[i]:
                        print(infiles[i])
            elif number == 4:
                informat_of_book_4 = input("검색할 출판사 :")
                infiles = infile.readlines()
                infiles = [line.rstrip("\n") for line in infiles]
                for i in range(len(infiles)):
                    if informat_of_book_4 in infiles[i]:
                        print(infiles[i])            
            elif number == 5:
                informat_of_book_5 = input("검색할 장르 :")
                infiles = infile.readlines()
                infiles = [line.rstrip("\n") for line in infiles]
                for i in range(len(infiles)):
                    if informat_of_book_5 in infiles[i]:
                        print(infiles[i])
            else:
                print("잘못된 번호 입력. 번호 재입력이 필요합니다.")
                bookruling_sys.find_book()
    

    #3. 도서 정보 수정함수
    
    #여기가 문제이다
    def change_info():
        print("\n[도서 정보 수정]\n")
        with open("c:/input.txt","rt",encoding='UTF8') as infile:
            infiles = infile.readlines()
            infiles = [line.rstrip("\n") for line in infiles]
            #infiles가 리스트 형태로 저장이 된다.
        
            for i in range(len(infiles)):
                infiles[i].split()

            book_name = input("수정할 도서제목 : ")
                
            for i in range(len(infiles)-1):
                remove_name1 = input("기존 정보 : ")
                remove_name2 = input("수정할 정보 : ")
                if remove_name1 == infiles[i][0]:
                    infiles[i].replace(infiles[i][0], remove_name2)
                else:
                    print("...\n")
                    continue

    #4. 도서 삭제 함수
    def delete_book():
        print("\n[도서 삭제]\n")
        with open("c:/input.txt","rt",encoding='UTF8') as infile:
            infiles = infile.readlines()
            infiles = [line.rstrip("\n") for line in infiles]

            book_name = input("삭제할 도서제목 : ")
            #book_name이 있는 리스트 슬라이스를 삭제한다.
            
            for k in range(len(infiles)-1):
                if book_name in infiles[k][0]:
                    infiles.remove(infiles[k])
                    print("삭제하였습니다.")
#IndexError: list index out of range 뭔데;;
        

    #5. 현재 총 도서 목록 출력 함수
    def print_all_book():
        print("\n[현재 총 도서 목록]\n")
        with open("c:/input.txt","rt",encoding='UTF8') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip() #줄 끝의 줄 바꿈 문자를 제거한다.
                print(line)
            #lines는 도서목록을 담고있는 리스트가 된다.
    #저장함수
    def saving_info():
        with open("c:/input.txt","at",encoding='UTF8') as f1:
            with open("c:/input.txt","rt",encoding='UTF8') as f:
                F = f.readlines()
                F = [line.rstrip("\n") for line in F]
                for i in F:
                    f1.writelines(i)
                    f1.write("\n")

    #main
    def main_func():
        print("[도서관리 프로그램]\n<Menu>\n[1. 도서목록추가]\n[2. 도서검색]\n[3. 도서정보수정]\n[4. 도서삭제]\n[5. 현재 총 도서 목록 출력]\n[6. 프로그램 종료]")
        while True:
            number = int(input("실행번호 입력 : "))
            if number == 1:
                bookruling_sys.add_book()
            elif number == 2:
                bookruling_sys.find_book()
            elif number == 3:
                bookruling_sys.change_info()
            elif number == 4:
                bookruling_sys.delete_book()
            elif number == 5:
                bookruling_sys.print_all_book()
            elif number == 6:
                print("도서관리 프로그램을 종료합니다\n이용해 주셔서 감사합니다.")
                exit()
            else:
                print("1번_6번까지의 메뉴를 정확히 입력해 주십시오.")
