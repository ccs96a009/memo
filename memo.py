import os

class Memo:
    def __init__(self, filename="memo.txt"):
        self.filename = filename
        self.message = ""
        self.load_last_message()

    def load_last_message(self):
        """Load the last message from the file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.message = file.read()
                print(f"Last message loaded: {self.message}")
        else:
            print("No previous message found.")

    def save_message(self, message):
        """Save the current message to the file."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(message)
        self.message = message
        print(f"Message saved: {self.message}")

    def display_last_message(self):
        """Display the last message."""
        if self.message:
            print(f"Last message: {self.message}")
        else:
            print("No message has been saved yet.")

def main():
    questions = [
        "哪個班別需交班?",
        "危急值檢體未發：檢體編號/無?",
        "分院檢體未到：檢體編號/無?",
        "品管異常須注意：項目/無?",
        "管制類檢體：已查備/未查備?",
        "機台狀況：叫修/無異常?"
    ]
    
    template = """{0}
危急值檢體未發：{1}
分院檢體未到：{2}
品管異常須注意：{3}
管制類檢體：{4}
機台狀況：{5}"""

    memo = Memo()
    
    while True:
        print("\n1. 顯示上一次交班內容")
        print("2. 我要留言交班 (請依提示填寫回答)")
        print("3. 離開此視窗")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            memo.display_last_message()
        elif choice == '2':
            answers = []
            for i, question in enumerate(questions):
                answer = input(question + " ")
                if i == 0:  # Special formatting for the first question
                    answer = f"{answer}交班"
                answers.append(answer)

            new_message = template.format(*answers)
            memo.save_message(new_message)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
