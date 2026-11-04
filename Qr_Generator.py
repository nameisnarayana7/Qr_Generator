import qrcode
from tkinter import Tk, filedialog
from PIL import Image

while True:
    print("----QR CODE GENERATOR----")
    print('1.Link or Text')
    print('2.Contact Card')
    print('3.wifi Password')
    print('4.Image')
    print('5.Exit')
    

    try:
        choice = int(input("Choose Format:"))

        match choice:
            case 1:
                text = input('Enter your Link or text:')
                file = input('File Name:')
                img = qrcode.make(text)
                img.save(file+"_qr.png")
                print('Image saved')
                img.show()
            case 2:
                fname = input('Enter firstname:')
                lname = input('Enter Lastname:')
                phone = input('Enter Phone No:')
                email = input('Enter Email:')

                full_name = fname+" "+lname
                card = ['Begin:Vcard',"VERSION:3.0"]
                card.append(('N:'+lname+';'+fname))
                card.append("FN"+full_name)
                card.append("TEL"+phone)
                card.append('EMAIL'+email)
                card.append('END:VCARD')
                vcard = '\n'.join(card)

                img = qrcode.make(vcard)
                img.save(fname+'_qr.png')
                print('image saved!!')
                img.show()
            case 3:
                ssid = input('Enter wifi name:')
                password = input('Enter Password:')

                wifi = f"WIFI:T:WPA;S:{ssid};P:{password};;"

                img = qrcode.make(wifi)
                img.save(ssid+'_qr.png')
                print('image saved!!')
                img.show()
            case 4:
                root = Tk()
                root.withdraw()

                path = filedialog.askopenfilename(
                title="Select Image",
                filetypes=[("Images","*.png *.jpg *.jpeg")]
                )

                root.destroy()

                if path:
                    with open(path, "rb") as f:
                        image_data = f.read()

                    import base64

                    encoded_data = base64.b64encode(image_data).decode()

                    if len(encoded_data) > 2900:
                        print("Image is too large for a single QR code!")
                    else:
                        img = qrcode.make(encoded_data)
                        img.save(image_data+"_qr.png")
                        print("Image data QR generated!")
                        img.show()
                else:
                    print("No image selected!")
                
            case 5:
                print("Exited !!")
                break
    except ValueError:
        print("Error: Please enter a valid number!")
