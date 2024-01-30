from django.contrib.postgres.fields import ArrayField
from django.db import models


class Department(models.Model):
    """Модель департамента"""

    name = models.CharField(max_length=100, verbose_name="Название")
    location = models.CharField(max_length=100, verbose_name="Город размещения")
    created_date = models.DateField(verbose_name="Дата основания")

    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Модель сотрудника"""

    PROGRAMMER = 0
    JOURNALIST = 1
    MANAGER = 2
    DESIGNER = 3
    INTERN = 4

    ROLES = (
        (PROGRAMMER, "Программист"),
        (JOURNALIST, "Журналист"),
        (MANAGER, "Менеджер"),
        (DESIGNER, "Дизайнер"),
        (INTERN, "Стажер"),
    )

    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    role = models.SmallIntegerField(default=4, choices=ROLES, verbose_name="Должность")
    salary = models.IntegerField(verbose_name="Зарплата")
    hire_date = models.DateField(verbose_name="Дата приема на работу")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Департамент",
    )
    tasks = ArrayField(
        base_field=models.CharField(max_length=100),
        default=list,
        blank=True,
        verbose_name="Задачи",
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
