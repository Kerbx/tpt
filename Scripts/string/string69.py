openToClose = {'{': '}', '[': ']', '(': ')'}
closeToOpen = {v: k for k, v in openToClose.items()}
 
text = input()
 
stack = []
for i, char in enumerate(text, 1):
    if char in openToClose:
        stack.append((i, char))
    elif char in closeToOpen:
        if len(stack):
            _, open_bracket = stack.pop()
            if open_bracket != closeToOpen[char]:
                print(i)
                break
        else:
            print(i)
            break
else:
    if stack:
        print(stack[0][0])
    else:
        print(0)