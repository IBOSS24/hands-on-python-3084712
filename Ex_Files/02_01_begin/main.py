RUN_INDENTED = False

message = "running unindented"

if RUN_INDENTED:
    message = "running indented"

print(message)


def my_function():
    greet = "Hello IBOSS"
    return greet
print(my_function())
