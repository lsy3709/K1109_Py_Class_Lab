from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
def func_open() :
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    print("사진의 크기 가로 세로 크기 : %d x %d" %(photo.width(),photo.height()))
    print("사진의 0,0 의 좌표의 RGB 값을 튜플로 보자.  :" )
    print(photo.get(0,0))
    a = photo.get(0,0)
    # print(a)
    # b = list(a)
    # print(b)
    # for i in range(0,3):
    #     c=int(b[i]/3)
    #     b.append(c)
    # print(b)        
    for i in range(0,photo.width()) :
        imgList =[]
        for k in range(0,photo.height()) :
            tmpList=[]
            a = photo.get(i,k)
            b = list(a)
            for j in range(0,3):
                b[j] = int((b[0]+b[1]+b[2])/3)
            a = tuple(b)
            tmpList.append(a)
        imgList.append(tmpList)

        #imgList 담아진 , 사진 파일의 RGB 의 값을 다시, 해당 photo 객체에 다시 담는 과정.
    
            
    
    pLabel.configure(image = photo)
    pLabel.image = photo
    
    

def func_exit() :
    window.quit()
    window.destroy()

## 메인 코드  부분 ##
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()
