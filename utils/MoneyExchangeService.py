import ast

a = """['127.0.0.1', '172.16.165.46', '172.16.165.47']"""
b = ast.literal_eval(a)
for i in b:
    print(i)
print(b, type(b))