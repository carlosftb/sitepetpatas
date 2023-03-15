from django import forms


class CadastroForms(forms.Form):
    nome=forms.CharField(
        label= "Nome de usuário:",
        max_length=50,
        required="True",
        widget=forms.PasswordInput(
            attrs={
                "class":"input100",
                "type":"text",
                "placeholder":"Exemplo: joao.silva",
            }
        )
    )

    email=forms.EmailField(
        label="E-mail:",
        required="True",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class":"input100",
                "type":"email",
                "placeholder":"Digite seu e-mail",
            }
        )

    )

    senha_1=forms.CharField(
        label="Senha:",
        required="True",
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class":"input100",
                "type":"password",
                "placeholder":"Digite sua senha",
            }
        )
        

    )

    senha_2=forms.CharField(
        label="Repita sua senha:",
        required="True",
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class":"input100",
                "type":"password",
                "placeholder":"Digite novamente a senha",
            }
        )
        

    )


class LoginForms(forms.Form):
    nome=forms.CharField(
        label= "Nome de usuario:",
        max_length=50,
        required="True",
        widget=forms.PasswordInput(
            attrs={
                "class":"input100",
                "type":"text",
                "placeholder":"Digite seu nome de usuário",
            }
        )
    )

    senha=forms.CharField(
        label="Senha:",
        required="True",
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class":"input100",
                "type":"password",
                "placeholder":"Digite sua senha",
            }
        )
    )
