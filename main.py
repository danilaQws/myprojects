import flet as ft
def main(page: ft.Page):
    page.title = 'bd app'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 800
    page.window_height = 400
    page.window_resizable = False
    def register_python_sq(e):
        pass
    btn_reg = ft.ElevatedButton(text='login', width=200, on_click=register_python_sq, disabled=True)
    def validate(e):
        if all([user_login.value,user_password.value]):
            btn_reg.disabled=False
        else:
            btn_reg.disabled=True
        page.update()
    user_login = ft.TextField(label='login',width=200,on_change=validate)
    user_password = ft.TextField(label='password',width=200,on_change=validate)
    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text('Register'),
                        user_login,
                        user_password,
                        btn_reg
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
ft.app(target=main)

    
