import tkinter as tk

# 기본 윈도우 생성
window = tk.Tk()

# 윈도우 제목 설정
window.title("메모장")

# 윈도우 크기 설정 (가로 800, 세로 600)
window.geometry("800x600")

# 메뉴바 생성
menubar = tk.Menu(window)

# '파일' 메뉴 생성
file_menu = tk.Menu(menubar, tearoff=0)
# '파일' 메뉴를 메뉴바에 추가
menubar.add_cascade(label="파일", menu=file_menu)

# '파일' 메뉴에 항목 추가
file_menu.add_command(label="새로 만들기")
file_menu.add_command(label="열기")
file_menu.add_command(label="저장")
file_menu.add_command(label="다른 이름으로 저장")
file_menu.add_separator()  # 구분선 추가
file_menu.add_command(label="종료", command=window.destroy)

# 윈도우의 메뉴로 menubar를 설정
window.config(menu=menubar)

# 텍스트를 입력하고 편집할 수 있는 Text 위젯 생성
text_area = tk.Text(window)
text_area.pack(expand=True, fill='both') # 창의 크기가 변경될 때 텍스트 영역도 함께 조절되도록 설정

# 윈도우가 화면에 표시되고 사용자 입력을 기다립니다.
window.mainloop()
