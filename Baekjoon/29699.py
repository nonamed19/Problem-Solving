words = 'WelcomeToSMUPC'

label = []
for word in words:
    label.append(word)

N = int(input()) % 14

print(label[N - 1])