from data_quest.questions import data
from desription.desc import user_description


class User:

    def __init__(self, res_data):
        self.ie = 0
        self.sn = 0
        self.tf = 0
        self.jp = 0

        self.user_i = 'I'
        self.user_n = 'N'
        self.user_f = 'G'
        self.user_p = 'P'

        self.all_data = data
        self.user_result = res_data

    def calculate(self):
        for res_k in list(self.user_result.keys()):

            if res_k in [ie for ie in range(1, 65, 7)]:
                if self.user_result[res_k] in self.all_data[res_k][1]:
                    self.ie += 1

            elif res_k in [sn for sn in range(2, 66, 7)]:
                if self.user_result[res_k] in self.all_data[res_k][1]:
                    self.sn += 1

            elif res_k in [sn for sn in range(3, 67, 7)]:
                if self.user_result[res_k] in self.all_data[res_k][1]:
                    self.sn += 1

            elif res_k in [tf for tf in range(4, 68, 7)]:
                if self.user_result[res_k] in self.all_data[res_k][1]:
                    self.tf += 1

            elif res_k in [tf for tf in range(5, 69, 7)]:
                if self.user_result[res_k] in self.all_data[res_k][1]:
                    self.tf += 1

            elif res_k in [jp for jp in range(6, 70, 7)]:
                if self.user_result[res_k] in self.all_data[res_k][1]:
                    self.jp += 1

            else:
                if self.user_result[res_k] in self.all_data[res_k][1]:
                    self.jp += 1

        self.user_i = 'E' if self.ie > 5 else 'I'
        self.user_n = 'S' if self.sn > 10 else 'N'
        self.user_f = 'T' if self.tf > 10 else 'F'
        self.user_p = 'J' if self.jp > 10 else 'P'

        user_code = f'{self.user_i}{self.user_n}{self.user_f}{self.user_p}'

        result_info = f'Ваши результаты: {user_code}\n\n' \
                      f'{user_description[user_code]}'

        return result_info
