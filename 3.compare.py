import timeit

def boyer_moore(text, pattern):
    def preprocess_bad_character_rule(pattern):
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char

    bad_char = preprocess_bad_character_rule(pattern)
    m, n = len(pattern), len(text)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1

def knuth_morris_pratt(text, pattern):
    def preprocess_pattern(pattern):
        lps = [0] * len(pattern)
        j = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = preprocess_pattern(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1


# Завантаження текстів з файлів
with open('стаття 1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

with open('стаття 2.txt', 'r', encoding='utf-8') as file:
    text2 = file.read()

# Пошук існуючих і неіснуючих підрядків
existing_substring1 = "алгоритмів у бібліотеках"
non_existing_substring1 = "немає такого підрядка"

existing_substring2 = "рекомендаційної системи"
non_existing_substring2 = "немає такого підрядка"

# Функції для вимірювання часу виконання
def measure_time_boyer_moore(text, pattern):
    return timeit.timeit(lambda: boyer_moore(text, pattern), number=1)

def measure_time_knuth_morris_pratt(text, pattern):
    return timeit.timeit(lambda: knuth_morris_pratt(text, pattern), number=1)

def measure_time_rabin_karp(text, pattern):
    return timeit.timeit(lambda: rabin_karp(text, pattern), number=1)

# Вимірювання часу для статті 1
time_boyer_moore_exist1 = measure_time_boyer_moore(text1, existing_substring1)
time_boyer_moore_non_exist1 = measure_time_boyer_moore(text1, non_existing_substring1)

time_knuth_morris_pratt_exist1 = measure_time_knuth_morris_pratt(text1, existing_substring1)
time_knuth_morris_pratt_non_exist1 = measure_time_knuth_morris_pratt(text1, non_existing_substring1)

time_rabin_karp_exist1 = measure_time_rabin_karp(text1, existing_substring1)
time_rabin_karp_non_exist1 = measure_time_rabin_karp(text1, non_existing_substring1)

# Вимірювання часу для статті 2
time_boyer_moore_exist2 = measure_time_boyer_moore(text2, existing_substring2)
time_boyer_moore_non_exist2 = measure_time_boyer_moore(text2, non_existing_substring2)

time_knuth_morris_pratt_exist2 = measure_time_knuth_morris_pratt(text2, existing_substring2)
time_knuth_morris_pratt_non_exist2 = measure_time_knuth_morris_pratt(text2, non_existing_substring2)

time_rabin_karp_exist2 = measure_time_rabin_karp(text2, existing_substring2)
time_rabin_karp_non_exist2 = measure_time_rabin_karp(text2, non_existing_substring2)

# Виведення результатів
print(f"Стаття 1 - Існуючий підрядок:")
print(f"Бойєра-Мура: {time_boyer_moore_exist1}")
print(f"Кнута-Морріса-Пратта: {time_knuth_morris_pratt_exist1}")
print(f"Рабіна-Карпа: {time_rabin_karp_exist1}")

print(f"Стаття 1 - Неіснуючий підрядок:")
print(f"Бойєра-Мура: {time_boyer_moore_non_exist1}")
print(f"Кнута-Морріса-Пратта: {time_knuth_morris_pratt_non_exist1}")
print(f"Рабіна-Карпа: {time_rabin_karp_non_exist1}")

print(f"Стаття 2 - Існуючий підрядок:")
print(f"Бойєра-Мура: {time_boyer_moore_exist2}")
print(f"Кнута-Морріса-Пратта: {time_knuth_morris_pratt_exist2}")
print(f"Рабіна-Карпа: {time_rabin_karp_exist2}")

print(f"Стаття 2 - Неіснуючий підрядок:")
print(f"Бойєра-Мура: {time_boyer_moore_non_exist2}")
print(f"Кнута-Морріса-Пратта: {time_knuth_morris_pratt_non_exist2}")
print(f"Рабіна-Карпа: {time_rabin_karp_non_exist2}")
