class postObj():
    def __init__(self, title, text):
        self.__title = title
        self.__text = text

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def set_title(self, title):
        self.__title = title

    def set_text(self, text):
        self.__text = text

class contactObj():
    def __init__(self, email, subject, message):
        self.__email = email
        self.__subject = subject
        self.__message = message

    def get_email(self):
        return self.__email

    def get_subject(self):
        return self.__subject

    def get_message(self):
        return self.__message

    def set_email(self, email):
        self.__email = email

    def set_subject(self, subject):
        self.__subject = subject

    def set_message(self, message):
        self.__message = message

class recipeObj():
    def __init__(self, name, type, prep_time, cooking_time, calories, ingredients, recipes):
        self.__name = name
        self.__type = type
        self.__prep_time = prep_time
        self.__cooking_time = cooking_time
        self.__calories = calories
        self.__ingredients = ingredients
        self.__recipes = recipes

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_prep_time(self):
        return self.__prep_time

    def get_cooking_time(self):
        return self.__cooking_time

    def get_calories(self):
        return self.__calories

    def get_ingredients(self):
        return self.__ingredients

    def get_recipes(self):
        return self.__recipes

    def set_name(self, name):
        self.__name = name

    def set_type(self, type):
        self.__type = type

    def set_prep_time(self, prep_time):
        self.__prep_time = prep_time

    def set_cooking_time(self, cooking_time):
        self.__cooking_time = cooking_time

    def set_calories(self, calories):
        self.__calories = calories

    def set_ingredients(self, ingredients):
        self.__ingredients = ingredients

    def set_recipes(self, recipes):
        self.__recipes = recipes

class announcementsObj():
    def __init__(self, announcement, content):
        self.__announcement = announcement
        self.__content = content

    def get_announcement(self):
        return self.__announcement

    def get_content(self):
        return self.__content

    def set_announcement(self, announcement):
        self.__announcement = announcement

    def set_content(self, content):
        self.__content = content
