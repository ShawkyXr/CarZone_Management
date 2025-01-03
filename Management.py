import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

def get_db_connection():
    conn = sqlite3.connect("Cars_DataBase.db")
    conn.row_factory = sqlite3.Row
    return conn


def main(root):
    root.title("CarZone")
    root.geometry("700x550")
    root.config(bg="#020202")
    root.resizable(False, False)

    head_frame = tk.Frame(root,height=200, width=700, bg="#020202")
    head_frame.pack()

    header = tk.Label(head_frame, text="CarZone System Managment App", font=("jetbrains mono",18, "bold"), fg="#d6a629", bg="#020202")
    header.place(x = 180 , y = 10)

    add_car_btn = tk.Button(head_frame, text="Add Car", font=("jetbrains mono", 12, "bold"), fg="black", bg="#d6a629",
                            bd=0,width = 10 , highlightthickness=0,)
    add_car_btn.place(x = 20, y = 80)

    delete_car_btn = tk.Button(head_frame, text="Delete Car", font=("jetbrains mono", 12, "bold"), fg="black", bg="#d6a629",
                                bd=0,width=10, highlightthickness=0)
    delete_car_btn.place(x = 200, y = 80)

    sell_car_btn = tk.Button(head_frame, text="Sell Car", font=("jetbrains mono", 12, "bold"), fg="black", bg="#d6a629",
                            bd=0, width=10 , highlightthickness=0)
    sell_car_btn.place(x = 380, y = 80)

    view_car_btn = tk.Button(head_frame, text="View Car", font=("jetbrains mono", 12, "bold"), fg="black", bg="#d6a629",
                            bd=0, width= 10, highlightthickness=0)
    view_car_btn.place(x = 560, y = 80)


    # img background for main frame
    main_frame = tk.Frame(root, height=350, width=700, bg="#020202")
    main_frame.pack()
    
    
    add_car_frame = tk.Frame(main_frame, height=350, width=700, bg="#020202")

    delete_car_frame = tk.Frame(main_frame, height=350, width=700, bg="#020202")

    sell_car_frame = tk.Frame(main_frame, height=350, width=700, bg="#020202")

    view_car_frame = tk.Frame(main_frame, height=350, width=700, bg="#020202")

    def add_car():
        add_car_frame.pack()
        delete_car_frame.pack_forget()
        sell_car_frame.pack_forget()
        view_car_frame.pack_forget()

    def delete_car():
        add_car_frame.pack_forget()
        delete_car_frame.pack()
        sell_car_frame.pack_forget()
        view_car_frame.pack_forget()

    def sell_car():
        add_car_frame.pack_forget()
        delete_car_frame.pack_forget()
        sell_car_frame.pack()
        view_car_frame.pack_forget()

    def view_car():
        add_car_frame.pack_forget()
        delete_car_frame.pack_forget()
        sell_car_frame.pack_forget()
        view_car_frame.pack()

    add_car_btn.config(command=add_car)
    delete_car_btn.config(command=delete_car)
    sell_car_btn.config(command=sell_car)
    view_car_btn.config(command=view_car)

    # Add Car Frame
    def display_add_frame():
        car_name_label = tk.Label(add_car_frame, text="Car Name", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
        car_name_label.place(x = 170, y = 0)
        car_name_entry = tk.Entry(add_car_frame, font=("jetbrains mono", 12), fg="#020202", bg="white")
        car_name_entry.place(x = 300, y = 0)

        car_model_label = tk.Label(add_car_frame, text="Car Model", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
        car_model_label.place(x = 170, y = 50)
        car_model_entry = tk.Entry(add_car_frame, font=("jetbrains mono", 12), fg="#020202", bg="white")
        car_model_entry.place(x = 300, y = 50)

        car_price_label = tk.Label(add_car_frame, text="Car Price", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
        car_price_label.place(x = 170, y = 100)
        car_price_entry = tk.Entry(add_car_frame, font=("jetbrains mono", 12), fg="#020202", bg="white")
        car_price_entry.place(x = 300, y = 100)

        car_color_label = tk.Label(add_car_frame, text="Car Color", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
        car_color_label.place(x = 170, y = 150)
        car_color_entry = tk.Entry(add_car_frame, font=("jetbrains mono", 12), fg="#020202", bg="white")
        car_color_entry.place(x = 300, y = 150)

        car_image_label = tk.Label(add_car_frame, text="Car Image", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
        car_image_label.place(x = 170, y = 200)
        car_image_btn = tk.Button(add_car_frame, text="Upload", font=("jetbrains mono", 12, "bold"), fg="black", bg="white",
                                    bd=0, width=18, highlightthickness=0)
        car_image_btn.place(x = 300, y = 200)

        car_image_path = ""

        def upload_image():
            nonlocal car_image_path
            car_image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
            print("Image Path: ", car_image_path)
            car_image_btn.config(text="Image Uploaded")

        car_image_btn.config(command=upload_image)

        add_btn = tk.Button(add_car_frame, text="Add Car", font=("jetbrains mono", 12, "bold"), fg="black", bg="#d6a629",
                                    bd=0, width=25 , highlightthickness=0)
        add_btn.place(x = 210, y = 280)
        
        #add to the database
        def add_car_to_db():

            # validate the entries
            print("path: ", car_image_path)
            if not car_name_entry.get() or not car_model_entry.get() or not car_price_entry.get() or not car_color_entry.get() or not car_image_path:
                messagebox.showerror("Error", "All fields are required.")
                return
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO cars (name, model, price, color, image_path) VALUES (?, ?, ?, ?, ?)",
                (car_name_entry.get(), car_model_entry.get(), car_price_entry.get(), car_color_entry.get(), car_image_path)
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Car added successfully!")

        add_btn.config(command=add_car_to_db)
    display_add_frame()


    # Delete Car Frame
    def display_delete_frame():
        car_id_label = tk.Label(delete_car_frame, text="Car ID", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
        car_id_label.place(x = 170, y = 0)
        car_id_entry = tk.Entry(delete_car_frame, font=("jetbrains mono", 12), fg="#020202", bg="white")
        car_id_entry.place(x = 300, y = 0)

        delete_btn = tk.Button(delete_car_frame, text="Delete Car", font=("jetbrains mono", 12, "bold"), fg="black", bg="#d6a629",
                                    bd=0, width=25 , highlightthickness=0)
        delete_btn.place(x = 210, y = 280)
        
        #delete from the database
        def delete_car_from_db():
            # validate the entry
            if not car_id_entry.get():
                messagebox.showerror("Error", "Car ID is required.")
                return
            if not car_id_entry.get().isdigit():
                messagebox.showerror("Error", "Car ID must be a number.")
                return
            
            if not messagebox.askyesno("Confirmation", "Are you sure you want to delete this car?"):
                return

            car_id = car_id_entry.get()
            conn = get_db_connection()
            cursor = conn.cursor()
            # check if the car exists
            cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
            car = cursor.fetchone()
            if not car:
                messagebox.showerror("Error", f"Car with ID {car_id} does not exist.")
                return
            cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Car with ID {car_id} has been deleted.")
        delete_btn.config(command=delete_car_from_db)
    display_delete_frame()


    # Sell Car Frame
    def display_sell_frame():
        car_id_label = tk.Label(sell_car_frame, text="Car ID", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
        car_id_label.place(x = 170, y = 0)
        car_id_entry = tk.Entry(sell_car_frame, font=("jetbrains mono", 12), fg="#020202", bg="white")
        car_id_entry.place(x = 300, y = 0)

        usr_name_label = tk.Label(sell_car_frame, text="buyer Name", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
        usr_name_label.place(x = 170, y = 100)
        usr_name_entry = tk.Entry(sell_car_frame, font=("jetbrains mono", 12), fg="#020202", bg="white")
        usr_name_entry.place(x = 300, y = 100)

        usr_phone_label = tk.Label(sell_car_frame, text="buyer Phone", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
        usr_phone_label.place(x = 170, y = 150)
        usr_phone_entry = tk.Entry(sell_car_frame, font=("jetbrains mono", 12), fg="#020202", bg="white")
        usr_phone_entry.place(x = 300, y= 150)

        date_label = tk.Label(sell_car_frame, text="Date", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
        date_label.place(x = 170, y = 50)
        date_entry = tk.Entry(sell_car_frame, font=("jetbrains mono", 12), fg="#020202", bg="white")
        date_entry.place(x = 300, y = 50)

        sell_btn = tk.Button(sell_car_frame, text="Sell Car", font=("jetbrains mono", 12, "bold"), fg="black", bg="#d6a629",
                                    bd=0, width=25 , highlightthickness=0)
        sell_btn.place(x = 210, y = 280)
        
        #db section
        def sell_car():
            car_id = car_id_entry.get()
            buyer_name = usr_name_entry.get()
            buyer_phone = usr_phone_entry.get()
            sale_date = date_entry.get()
            if not car_id or not buyer_name or not buyer_phone or not sale_date:
                messagebox.showerror("Error", "All fields are required.")
                return
            if not car_id.isdigit():
                messagebox.showerror("Error", "Car ID must be a number.")
                return
            
            conn = get_db_connection()
            cursor = conn.cursor()

            # check if the car exists
            cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
            car = cursor.fetchone()
            if not car:
                messagebox.showerror("Error", f"Car with ID {car_id} does not exist.")
                return
            
            cursor.execute(
                "INSERT INTO transactions(car_id, buyer_name, buyer_phone, date) VALUES(?,?,?,?)",
                (car_id,buyer_name,buyer_phone,sale_date)
            )
            
            cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Car with ID {car_id} has been sold to {buyer_name}.")
        sell_btn.config(command=sell_car)
    display_sell_frame()


    def display_view_frame():
        car_id_label = tk.Label(view_car_frame, text="Car ID", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
        car_id_label.place(x = 170, y = 0)
        car_id_entry = tk.Entry(view_car_frame, font=("jetbrains mono", 12), fg="#020202", bg="white")
        car_id_entry.place(x = 300, y = 0)

        view_btn = tk.Button(view_car_frame, text="View Car", font=("jetbrains mono", 12, "bold"), fg="black", bg="#d6a629",
                                    bd=0, width=25 , highlightthickness=0)
        view_btn.place(x = 210, y = 280)

        def view_car():
            car_id = car_id_entry.get()
            if not car_id:
                messagebox.showerror("Error", "Car ID is required.")
                return
            if not car_id.isdigit():
                messagebox.showerror("Error", "Car ID must be a number.")
                return
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
            car = cursor.fetchone()
            conn.close()
            if not car:
                messagebox.showerror("Error", f"Car with ID {car_id} does not exist.")
                return
            # display the car details with image
            car_name = car["name"]
            car_model = car["model"]
            car_price = car["price"]
            car_color = car["color"]
            car_image_path = car["image_path"]

            car_name_label = tk.Label(view_car_frame, text=f"Car Name: {car_name}", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
            car_name_label.place(x = 170, y = 50)
            
            car_model_label = tk.Label(view_car_frame, text=f"Car Model: {car_model}", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
            car_model_label.place(x = 170, y = 100)

            car_price_label = tk.Label(view_car_frame, text=f"Car Price: {car_price}", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
            car_price_label.place(x = 170, y = 150)

            car_color_label = tk.Label(view_car_frame, text=f"Car Color: {car_color}", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
            car_color_label.place(x = 170, y = 200)

            try:
                img = Image.open(car_image_path)
                img = img.resize((200, 150))
                img = ImageTk.PhotoImage(img)
                car_image_label = tk.Label(view_car_frame, image=img, bd=0, highlightthickness=0)
                car_image_label.image = img
                car_image_label.place(x = 400, y = 50)
            except Exception as e:
                print("Failed to load image: ", e)
                car_image_label = tk.Label(view_car_frame, text="Image not found", font=("jetbrains mono", 13, "bold"), fg="#d6a629", bg="#020202")
                car_image_label.place(x = 400, y = 50)

        view_btn.config(command=view_car)

    display_view_frame()


if __name__ == '__main__':
    main()