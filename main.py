
import os
if __name__ == '__main__':
    print("Welcome to RObospeaker 1.1 Created by shivam")
    while(True):
        x=input("Enter what you want me to speakh")
        if x=="quit":
            os.system("say 'bye bye human'")
        command=f"say {x}"
        os.system(command)
