from test_custom_runner import generate_pytest_args


def dump_pytest_args():
    pytest_args = generate_pytest_args()
    with open("pytest_config.txt", "w") as f1:
        f1.write("[pytest] \n")
        writestring = "addopts="
        for argument in pytest_args:
            writestring += " " + argument
        f1.write(writestring)

if __name__ == '__main__':
    dump_pytest_args()
