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
            infile.write(new_line)
            infile.write("\n")

    #2. 도서검색 함수_도서명, 장르 이런것데 관계있는 것들 싹다 반환 
    # 리스트에 해당 줄을 싹다 반환하는 함수___#3 #4 함수에서호출 할 수 있도록 하자!!   
    def find_book():
        print("\n[도서검색]\n")
        with open("c:/input.txt","rt",encoding='UTF8') as infile:
            infiles = infile.readlines()
            infiles = [line.rstrip("\n") for line in infiles]    
            
            splitline = []
            for i in range(len(infiles)):
                splitline.append(infiles[i].split()) #스플릿 한 걸 할당해준다.
            #print(splitline)

            print("찾을 정보 분류\n[1.도서명, 2.저자, 3.출판년도, 4.출판사, 5.장르]")
            number = int(input("분류 번호 입력 : "))
            
            if number == 1:
                informat_of_book_1 = input("검색할 도서이름 :")

                for kvalue in range(len(infiles)):
                    if ((informat_of_book_1) == (splitline[kvalue][0])):
                        print(infiles[kvalue])
                    else:
                        continue
            elif number == 2:
                informat_of_book_2 = input("검색할 저자 :")
                
                for kvalue in range(len(infiles)):
                    if ((informat_of_book_2) in (splitline[kvalue][1])):
                        print(infiles[kvalue])
                    else:
                        continue
            elif number == 3:
                informat_of_book_3 = input("검색할 출판년도 :")
                for kvalue in range(len(infiles)):
                    if ((informat_of_book_3) in (splitline[kvalue][2])):
                        print(infiles[kvalue])
                    else:
                        continue
            elif number == 4:
                informat_of_book_4 = input("검색할 출판사 :")
                for kvalue in range(len(infiles)):
                    if ((informat_of_book_4) in (splitline[kvalue][3])):
                        print(infiles[kvalue])
                    else:
                        continue            
            elif number == 5:
                informat_of_book_5 = input("검색할 장르 :")
                for kvalue in range(len(infiles)):
                    if ((informat_of_book_5) in (splitline[kvalue][4])):
                        print(infiles[kvalue])
                    else:
                        continue
            else:
                print("잘못된 번호 입력. 번호 재입력이 필요합니다.")
                bookruling_sys.find_book()
    

    #3. 도서 정보 수정함수
    def change_info():
        while(1):
            print("\n[도서 정보 수정]\n")
            with open("c:/input.txt","rt",encoding='UTF8') as infile:
                infiles = infile.readlines()
                infiles = [line.rstrip("\n") for line in infiles]
                #infiles가 리스트 형태로 저장이 된다.
            
                splitline = []
                for i in range(len(infiles)):
                    splitline.append(infiles[i].split()) #스플릿 한 걸 할당해준다.
                
                print("수정할 요소\n[1.도서명, 2.저자, 3.출판년도, 4.출판사, 5.장르, 6.수정종료]")
                number = int(input("분류 번호 입력 : "))
                
                if(number == 1):
                    remove_name1 = input("수정할 도서제목 : ")
                    remove_name2 = input("새로운 도서제목 : ")
                    for i in range(len(infiles)):
                    #print(remove_name1)
                    #print(splitline[i][0],"\n")
                        if remove_name1 == splitline[i][0]:#if문 안에 들어가긴 한다.

                            with open("c:/input.txt","at",encoding='UTF8') as infile:
                                #라인삭제
                                #del infiles[i]
                                #라인에 0번째 요소를 바꿔서 입력한다.
                                splitline[i][0] = remove_name2
                                #print(splitline)
                                infiles = list(splitline)
                        else:
                            continue
                    with open("c:/input.txt","w",encoding='UTF8') as infile:
                        for i in range(len(infiles)):
                            for j in range(5):
                                infile.write(splitline[i][j])
                                infile.write(" ")
                            infile.write("\n")
                elif(number == 2):
                    remove_name1 = input("수정할 도서제목 : ")
                    remove_name2 = input("새로운 저자 : ")
                    for i in range(len(infiles)):
                    #print(remove_name1)
                    #print(splitline[i][0],"\n")
                        if remove_name1 == splitline[i][0]:#if문 안에 들어가긴 한다.

                            with open("c:/input.txt","at",encoding='UTF8') as infile:
                                #라인삭제
                                #del infiles[i]
                                #라인에 0번째 요소를 바꿔서 입력한다.
                                splitline[i][1] = remove_name2
                                #print(splitline)
                                infiles = list(splitline)
                        else:
                            continue
                    with open("c:/input.txt","w",encoding='UTF8') as infile:
                        for i in range(len(infiles)):
                            for j in range(5):
                                infile.write(splitline[i][j])
                                infile.write(" ")
                            infile.write("\n")
                elif(number == 3):
                    remove_name1 = input("수정할 도서제목 : ")
                    remove_name2 = input("새로운 출판년도 : ")
                    for i in range(len(infiles)):
                    #print(remove_name1)
                    #print(splitline[i][0],"\n")
                        if remove_name1 == splitline[i][0]:#if문 안에 들어가긴 한다.

                            with open("c:/input.txt","at",encoding='UTF8') as infile:
                                #라인삭제
                                #del infiles[i]
                                #라인에 0번째 요소를 바꿔서 입력한다.
                                splitline[i][2] = remove_name2
                                #print(splitline)
                                infiles = list(splitline)
                        else:
                            continue
                    with open("c:/input.txt","w",encoding='UTF8') as infile:
                        for i in range(len(infiles)):
                            for j in range(5):
                                infile.write(splitline[i][j])
                                infile.write(" ")
                            infile.write("\n")
                elif(number == 4):
                    remove_name1 = input("수정할 도서제목 : ")
                    remove_name2 = input("새로운 출판사 : ")
                    for i in range(len(infiles)):
                    #print(remove_name1)
                    #print(splitline[i][0],"\n")
                        if remove_name1 == splitline[i][0]:#if문 안에 들어가긴 한다.

                            with open("c:/input.txt","at",encoding='UTF8') as infile:
                                #라인삭제
                                #del infiles[i]
                                #라인에 0번째 요소를 바꿔서 입력한다.
                                splitline[i][3] = remove_name2
                                #print(splitline)
                                infiles = list(splitline)
                        else:
                            continue
                    with open("c:/input.txt","w",encoding='UTF8') as infile:
                        for i in range(len(infiles)):
                            for j in range(5):
                                infile.write(splitline[i][j])
                                infile.write(" ")
                            infile.write("\n")
                elif(number == 5):
                    remove_name1 = input("수정할 도서제목 : ")
                    remove_name2 = input("새로운 장르 : ")
                    for i in range(len(infiles)):
                    #print(remove_name1)
                    #print(splitline[i][0],"\n")
                        if remove_name1 == splitline[i][0]:#if문 안에 들어가긴 한다.

                            with open("c:/input.txt","at",encoding='UTF8') as infile:
                                #라인삭제
                                #del infiles[i]
                                #라인에 0번째 요소를 바꿔서 입력한다.
                                splitline[i][4] = remove_name2
                                #print(splitline)
                                infiles = list(splitline)
                        else:
                            continue
                    with open("c:/input.txt","w",encoding='UTF8') as infile:
                        for i in range(len(infiles)):
                            for j in range(5):
                                infile.write(splitline[i][j])
                                infile.write(" ")
                            infile.write("\n")
                elif(number == 6):
                    print("[수정 완료!]")
                    break
                else:
                    print(".")
                    continue

        

    #4. 도서 삭제 함수
    def delete_book():
        print("\n[도서 삭제]\n")
        with open("c:/input.txt","rt",encoding='UTF8') as infile:
            infiles = infile.readlines()
            infiles = [line.rstrip("\n") for line in infiles]

            splitline = []
            for i in range(len(infiles)):
                splitline.append(infiles[i].split())

            book_name = input("삭제할 도서제목 : ")
            #book_name이 있는 리스트 슬라이스를 삭제한다.
            
            for k in range(len(infiles)):
                if book_name == splitline[k][0]:
                    infiles.remove(infiles[k])
                    print("삭제하였습니다.")
                    
            with open("c:/input.txt","w",encoding='UTF8') as infile:
                for i in range(len(infiles)):
                    infile.write(infiles[i])
                    infile.write("\n")

    #5. 현재 총 도서 목록 출력 함수
    def print_all_book():
        print("\n[현재 총 도서 목록]\n")
        with open("c:/input.txt","rt",encoding='UTF8') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip() #줄 끝의 줄 바꿈 문자를 제거한다.
                print(line)
            #lines는 도서목록을 담고있는 리스트가 된다.
   
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
