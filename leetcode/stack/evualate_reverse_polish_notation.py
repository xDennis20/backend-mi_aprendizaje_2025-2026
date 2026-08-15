def eval_rpn(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        match token:
            case "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            case "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            case "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            case "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            case _:
                if token.isalnum() or token.startswith("-"):
                    stack.append(int(token))

    return stack[0]

print(eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))