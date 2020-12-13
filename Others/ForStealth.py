contest_name = ""
problem_num = 6
for i in range(problem_num):
    print("----- INPUT FOR {}{} -----".format(contest_name, chr(i+65)))
print("----- OTHER INPUTS -----")
for i in range(problem_num):
    print("input()")
    print("print('----- OUTPUT FOR {}{} -----')".format(contest_name, chr(i+65)))
    print("# {}{}".format(contest_name, chr(i+65)))
    print()
    print()
print("input()")
print("print('----- OTHER OUTPUTS -----')")
print("# OTHER CODE")
