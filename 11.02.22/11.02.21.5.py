def calc(num, form):
    return ('{0:%s}'%form).format(num)

print(calc(8, 2))