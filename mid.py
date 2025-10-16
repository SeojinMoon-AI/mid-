import tkinter as tk

# 기본 윈도우 생성
window = tk.Tk()

# 윈도우 제목 설정
window.title("메모장")

# 윈도우 크기 설정 (가로 800, 세로 600)
window.geometry("800x600")

# "메모장을 만들어봐요" 텍스트를 표시할 라벨(Label) 위젯 생성
label = tk.Label(window, text="메모장을 만들어봐요", font=("Arial", 24))

# 라벨을 창의 중앙에 배치합니다. expand=True 옵션은 위젯이 가질 수 있는 모든 공간을 차지하도록 합니다.
label.pack(expand=True)

# 윈도우가 화면에 표시되고 사용자 입력을 기다립니다.
window.mainloop()
