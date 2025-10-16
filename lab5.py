import regex as re

def match_a_to_b(s):
    pattern = r"ab*"
    if re.findall(pattern, s):
        return True
    else:
        return False
print(match_a_to_b("ab"))
print(match_a_to_b("aba"))
print(match_a_to_b("abbb"))

def match_a_to_b2(s):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, s):
        return True
    else:
        return False

print(match_a_to_b2("ab"))
print(match_a_to_b2("abb"))
print(match_a_to_b2("abbb"))

def lowercase_letters(s):
    pattern = r'[a-z]+_[a-z]+'
    print(" ", re.findall(pattern, s))

print(lowercase_letters("qw abcdef_ghijkl mnopqrst_uvwx yz"))

def uppercase_letters(s):
    pattern = r'[A-Z][a-z]+'
    print(" ", re.findall(pattern, s))

print(uppercase_letters("HelloWorld, pipotam"))

def a_followed_by_b(s):
    pattern = r'a.*b$'
    if re.fullmatch(pattern, s):
        return True
    else:
        return False

print(a_followed_by_b("afgbfbgfgb"))
print(a_followed_by_b("abbbbbbbbbbbbvc"))

text = "qwe,trhe pewp. ertq,qwet"
print(" ", re.sub(r'[ ,.]', ':', text))

def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
print(" ", snake_to_camel("pipotam_hello_world"))

text = "mitsubishigalant"
print(" ", re.split(r'(?=[A-Z])', text))

text = "obshiy salam"
print(" ", re.sub(r'(?=[A-Z])', ' ', text).strip())

def camel_to_snake(name):
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
print(" ", camel_to_snake("chetam"))