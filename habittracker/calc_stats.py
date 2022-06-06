"""Модуль предоставляет функции, необходимые для подсчета статистики."""

import numpy as np


def calc_ticks_numbers(ticks_matrix):
    """Считает суммы по строкам и столбцам матрицы отметок о выполненных делах.

    :param ticks_matrix: матрица (список списков) M x N, M - количество дел, N - количество дней
    :type ticks_matrix: numpy.ndarray

    :return: кортеж из двух списков (суммарные количества сделанных дел по каждому из дел за весь период времени и суммарные количества
    сделанных дел в каждый день соответственно), если входной массив непуст (иначе кортеж (-1, -1))
    :rtype: tuple
    """
    ticks_matrix = np.array(ticks_matrix)
    if len(ticks_matrix.shape) == 2 and ticks_matrix.shape[0] > 0 and ticks_matrix.shape[1] > 0:
        return list(np.sum(ticks_matrix, axis=1)), list(np.sum(ticks_matrix, axis=0))
    else:
        return (-1, -1)


def calc_most_popular(ticks_matrix):
    """Считает максимальные значения по строкам и столбцам матрицы отметок о выполненных делах.

    :param ticks_matrix: матрица (список списков) M x N, M - количество дел, N - количество дней
    :type ticks_matrix: numpy.ndarray

    :return: кортеж из двух списков (индексы дел которые были сделаны в наибольшее число дней, и индексы дней, в которые было сделано
    наибольшее количество дел соответственно), если входной массив непуст (иначе кортеж (-1, -1))
    :rtype: tuple
    """
    ticks_matrix = np.array(ticks_matrix)
    if len(ticks_matrix.shape) == 2 and ticks_matrix.shape[0] > 0 and ticks_matrix.shape[1] > 0:
        tasks_sums, days_sums = calc_ticks_numbers(ticks_matrix)
        maximum_tasks_per_day = np.max(tasks_sums)
        maximum_days_with_task_done = np.max(days_sums)
        idxs_of_maximum_tasks_per_day = np.where(tasks_sums == maximum_tasks_per_day)
        idxs_of_maximum_days_with_task_done = np.where(days_sums == maximum_days_with_task_done)
        return list(idxs_of_maximum_tasks_per_day[0]), list(idxs_of_maximum_days_with_task_done[0])
    else:
        return (-1, -1)


def calc_least_popular(ticks_matrix):
    """Считает минимальные значения по строкам и столбцам матрицы отметок о выполненных делах.

    :param ticks_matrix: матрица (список списков) M x N, M - количество дел, N - количество дней
    :type ticks_matrix: numpy.ndarray

    :return: кортеж из двух списков (индексы дел которые были сделаны в наименьшее число дней, и индексы дней, в которые было сделано
    наименьшее количество дел соответственно), если входной массив непуст (иначе кортеж (-1, -1))
    :rtype: tuple
    """
    ticks_matrix = np.array(ticks_matrix)
    if len(ticks_matrix.shape) == 2 and ticks_matrix.shape[0] > 0 and ticks_matrix.shape[1] > 0:
        tasks_sums, days_sums = calc_ticks_numbers(ticks_matrix)
        minimum_tasks_per_day = np.min(tasks_sums)
        minimum_days_with_task_done = np.min(days_sums)
        idxs_of_minimum_tasks_per_day = np.where(tasks_sums == minimum_tasks_per_day)
        idxs_of_minimum_days_with_task_done = np.where(days_sums == minimum_days_with_task_done)
        return list(idxs_of_minimum_tasks_per_day[0]), list(idxs_of_minimum_days_with_task_done[0])
    else:
        return (-1, -1)
