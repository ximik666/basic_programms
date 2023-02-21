class Phone:

    # Статические поля (переменные класса)
    default_color = 'Grey'
    default_model = 'C385'
    self.dd = "1"
    def create_phone(self,color):
        self.color = color
a = Phone()
a.create_phone("red")
Phone.default_color = "black"
a.default_color = "white"
print(1)