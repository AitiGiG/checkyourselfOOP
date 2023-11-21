"""1) Создайте класс ToDo, с аттрибутом экземпляра класса, в виде словаря todos = {}.

У класса должен быть один метод set_deadline, который принимает дату дедлайна (в виде "31/12/2021") и возвращает количество дней оставшихся до дедлайна.

Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin, DeleteMixin, UpdateMixin, ReadMixin:

в классе CreateMixin определите метод create, который принимет в себя задачу todo и ключ key по которому нужно добавить задачу в словарь todos, если ключ уже существует верните "Задача под таким ключём уже существует".

класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу key, который передается как аргумент, и возвращает сообщение 'удалили название задачу', где вместо слова название должно быть название задачи.

класс UpdateMixin должен содержать метод update, который принимает в себя ключ key и новое значение new_value и заменяет задачу под данным ключом на новое значение.

класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач.

2) Напишите класс Person, который будет хранить информацию о пользователе. У объекта будут следующие защищенные атрибуты экземпляра класса: имя(name), фамилия(last_name), возраст(age), почта (email).
При инициализации объекта, передавать аргументы классу не нужно, все его атрибуты по умолчанию будут равны None и также все они будут приватными.
Поэтому реализуйте для каждого атрибута методы доступа get и set с использованием декораторов property и setter. У вас будут такие методы: name (getter, setter), last_name (getter, setter), age (getter, setter) , email (getter, setter)
Создайте экземпляр john класса Person выедите все его атрибуты, затем измените их как показано ниже и после снова выведите на экран.
Пример:

john = Person()
print(john.name) # None
print(john.last_name) # None
print(john.age) # None
print(john.email) # None
john.name = 'John'
john.last_name = 'Snow'
john.age = 30
john.email = 'johnsnow@gmail.com'
print(john.name) # John
print(john.last_name) # Snow
print(john.age) # 30
print(john.email) # johnsnow@gmail.com

3) Создайте классы Dog и Cat с одинаковым методом voice.
Для собак он должен печатать "Гав", для кошек "Мяу".
Объявите для каждого из классов по экземпляру, для класса Cat экземпляр в переменной barsik, а для Dog экземпляр rex.
Затем, вне класса объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice().
Ввод:
to_pet(barsik)
to_pet(rex)
Вывод:

Мяу
Гав
"""

'===========Task-1============'
# from datetime import datetime

# class CreateMixin:
#     def create(self, todo, key):
#         if key in self.todos:
#             return 'Задача с таким ключом уже существует'
#         self.todos[key] = todo
#         return self.todos

# class DeleteMixin:
#     def delete(self, key):
#         if key in self.todos:
#             deleted_task = self.todos.pop(key)
#             return f'удалили {deleted_task} задачу'
#         else:
#             return 'Такого ключа нет'

# class UpdateMixin:
#     def update(self, key, new_value):
#         if key in self.todos:
#             self.todos[key] = new_value
#             return self.todos
#         else:
#             return 'Такого ключа нет'

# class ReadMixin:
#     def read(self):
#         return dict(sorted(self.todos.items()))

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}

#     def set_deadline(self, deadline: str):
#         deadline_date = datetime.strptime(deadline, '%d/%m/%Y')
#         today = datetime.now()
#         difference = deadline_date - today
#         return difference.days


# task = ToDo()

# print(task.create('Do housework', 1))
# print(task.create('Go for a walk', 2))
# print(task.create('Do homework', 3))
# print(task.update(1, 'Clean the house'))
# print(task.delete(2))
# print(task.read())
# print(task.set_deadline('31/12/2021'))


"===============Task-2==============="
# class Person:
#     __name = None
#     __last_name = None
#     __age = None
#     __email = None
#     def get_name(self):
#         return self.__name
#     def set_name(self, new):
#         self.__name = new
#     def get_last_name(self):
#         return self.__last_name
#     def set_last_name(self, new):
#         self.__last_name = new
#     def get_age(self):
#         return self.__age
#     def set_age(self, new):
#         self.__age = new
#     def get_email(self):
#         return self.__email
#     def set_email(self,new):
#         self.__email = new

# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com

"=============task-3=============="

# class Cat:
#     def voice(self):
#         print("Мяу")
# class Dog:
#     def voice(self):
#         print("Гав")

# rex = Dog()
# barsik = Cat()

# def to_pet(cls):
#     cls.voice()

# to_pet(barsik)
# to_pet(rex)