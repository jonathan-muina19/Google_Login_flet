import flet as ft
from flet import TextField,Checkbox,ElevatedButton,Row,Column,ControlEvent,Text,ButtonStyle,RoundedRectangleBorder


def main(page : ft.Page):
    page.title = "Signnup"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window_width = 800
    page.window_height = 600
    
    google_img = ft.Image(src=f"img\googlelogo_color_160x56dp.png",width=100)
    label_txt  = ft.Text(value="        Create a strong password",size=20,text_align=ft.TextAlign.CENTER,font_family="Verdana",)
    sous_label1 = ft.Text(value="               Create a strong password with a mix of the letters",size=10,text_align=ft.TextAlign.CENTER,font_family="Verdana")
    sous_label2 = ft.Text(value="                                   numbers and symbols",size=10,text_align=ft.TextAlign.CENTER,font_family="Verdana")
    text_username : TextField = TextField(label="Password", text_align = ft.TextAlign.LEFT,width=350)
    text_password : TextField = TextField(label="Confirm", text_align = ft.TextAlign.LEFT,width=350)
    checkbox_signup : Checkbox = Checkbox(label="Show password",value=False)
    button_submit : ElevatedButton = ElevatedButton(text="Next",width=100,disabled=False,bgcolor="blue",
                                                    color="white",tooltip="Cliquez pour vous connecter",
                                                    adaptive=True,style=ButtonStyle(shape=RoundedRectangleBorder(radius=5),
                                                                                    ))
    next_btn = Row([button_submit],alignment=ft.MainAxisAlignment.END,width=350)
    
    
    def validate(e: ControlEvent) -> None:
        if all([text_password.value, text_username.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        
        page.update()
        
    def submit(e: ControlEvent):
        print("Username :",text_username.value)
        print("Password :",text_password.value)
        
        page.clean()
        page.add(Row(
            controls=[Text(value=f"Welcome , Your password is {text_username.value}",size=40)],
            alignment=ft.MainAxisAlignment.CENTER
        ))
        
    page.add(ft.Row(
        [
            google_img,
            
        ],alignment=ft.MainAxisAlignment.CENTER
    ))
    
    page.add(Row(
        controls=[
            Column(
                [
                    label_txt,
                    sous_label1,
                    sous_label2,
                    text_username,
                    text_password,
                    checkbox_signup,
                    next_btn
                ],spacing=20
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
        
    ))
    

    text_password.on_change = validate
    text_username.on_change = validate
    checkbox_signup.on_change = validate
    button_submit.on_click = submit
    
if __name__ == '__main__':
    ft.app(target=main)