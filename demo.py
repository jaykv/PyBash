# PYBASH DEMO
def cp_test():
    >cp test.txt test_copy.txt

cp_test()

print((>cat test.txt).decode('utf-8').strip())

# simple bash command execution with output
>python --version
>echo \\nthis is an echo

# set output to python variable directly
out = >cat test.txt
test_data = out.decode('utf-8').strip()
print(test_data.replace("HELLO", "HOWDY"))
# TODO:
#>echo "hello" >> test.txt