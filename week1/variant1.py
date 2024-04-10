class MultiplicationTable:
    @classmethod
    def print_table(cls):
        for row in range(1, 13):
            for col in range(1, 13):
                print(f'{row * col:4}', end='')  # 4文字幅で右揃えで出力
            print()  # 各行の最後で改行

# 掛け算表の出力
MultiplicationTable.print_table()