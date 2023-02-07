languages = ['python', 'java', 'swift', 'c', 'c++']
skip_languages = [languages[2], languages[4]]

for i in languages:
    if i  in skip_languages:
        continue
    print(i)