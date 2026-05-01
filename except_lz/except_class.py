import pandas as pd
import os


class ClassExcept:
    def load_and_check(self, file_name):
        error_found = False
        if not os.path.exists(file_name):
            print('Возникла следующая ошибка: [Errno 2] No such file or directory: "{}"'.format(file_name))
            error_found = True
        if not error_found:
            try:
                df = pd.read_csv(file_name)
                if df.empty:
                    print('Возникла следующая ошибка: Датафрейм пуст')
                    error_found = True
                if not error_found:
                    expected_cols = ['A', 'B', 'C']
                    actual_cols = list(df.columns)
                    type_b = str(df['B'].dtype) if 'B' in df.columns else 'Object'
                    type_c = str(df['C'].dtype) if 'C' in df.columns else 'Object'
                    cols_match = (actual_cols == expected_cols)
                    is_b_ok = (type_b == 'str')
                    is_c_ok = ('float' in type_c)
                    if not cols_match or not is_b_ok or not is_c_ok:
                        error_found = True
                        print('Структура датафрейма НЕ соответствует ожидаемой:')
                        if not cols_match:
                            print(' - Названия столбцов не совпадают.')
                            print('Ожидаемые:', expected_cols)
                            print('Фактические:', actual_cols)
                        if not is_b_ok:
                            print(' - В столбце "B" тип данных не соответствует ожидаемому.')
                            print('Ожидается: str, Фактически:', type_b)
                        if not is_c_ok:
                            print(' - В столбце "C" тип данных не соответствует ожидаемому.')
                            print('Ожидается: float, Фактически:', type_c)
            except Exception as e:
                print('Возникла следующая ошибка:', e)
                error_found = True
        if not error_found:
            print('Чтение датафрейма завершено успешно.')
