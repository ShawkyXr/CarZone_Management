import tkinter as tk
from PIL import Image, ImageTk
from Management import get_db_connection

def login(username,password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        tk.messagebox.showinfo("Login Success", "Welcome!")
        tk.root.destroy()  
        import Management  
    else:
        tk.messagebox.showerror("Login Failed", "Invalid email or password.")
        

def main():

    root = tk.Tk()
    root.title("CarZone")
    root.geometry("700x550")
    root.resizable(False, False)
    root.config(bg="#020202")
    img = Image.open("C:\car_managment\CarZone_Management\images\Background.png")
    bcg = img.resize((680, 500))
    bcg = ImageTk.PhotoImage(bcg)
    bcg_label = tk.Label(root, image=bcg, bd=0, highlightthickness=0)
    bcg_label.pack()

    header = tk.Label(root, text="CarZone System Managment App", font=("jetbrains mono",25, "bold"), fg="#d6a629", bg="#020202")
    header.place(x = 100 , y = 60)


    # user login
    usr_label = tk.Label(root, text="Username", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
    usr_label.place(x = 192, y = 380)
    usr_entry = tk.Entry(root, font=("jetbrains mono", 12), fg="#020202", bg="white")
    usr_entry.place(x = 280, y = 380)

    # password login
    pwd_label = tk.Label(root, text="Password", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
    pwd_label.place(x = 190, y = 430)
    pwd_entry = tk.Entry(root, font=("jetbrains mono", 12), fg="#020202", bg="white")
    pwd_entry.place(x = 280, y = 430)

    # login button
    login_btn = tk.Button(root, text="Login", font=("jetbrains mono", 12, "bold"), fg="black", bg="#d6a629", bd=0, highlightthickness=0,command=lambda: login(usr_entry.get(), pwd_entry.get()))
    login_btn.place(x = 310, y = 480)

    root.mainloop()


if __name__ == '__main__':
    main()