text="Klaos is practicing the python for writing files and wheter the Anroid(?) can achieve it or just prctice to just get the slight of hand down"
file_path="D:/NeuroCosmos/file.txt"
with open(file_path,'w') as f:
    f.write(text)
print(f"Text file'{file_path}'is created")


def learning_note_manager():
    note_file = 'learning_notes.txt'
    
    while True:
        print("\n=== 学习笔记管理器 ===")
        print("1. 查看笔记")
        print("2. 添加笔记") 
        print("3. 退出")
        
        choice = input("请选择操作 (1-3): ")
        
        if choice == '1':
    
            try:
                with open(note_file, 'r', encoding='utf-8') as file:
                    print("\n--- 你的学习笔记 ---")
                    for line_num, line in enumerate(file, 1):
                        print(f"{line_num}. {line.strip()}")
            except FileNotFoundError:
                print("还没有笔记，请先添加！")
                
        elif choice == '2':
            # 添加笔记 - 使用追加模式
            note = input("请输入学习笔记: ")
            with open(note_file, 'a', encoding='utf-8') as file:
                file.write(f"{note}\n")
            print("笔记已保存！")
            
        elif choice == '3':
            print("再见！")
            break
        else:
            print("请输入有效选项！")

