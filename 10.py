#!/usr/bin/env python3

chars = [[c for c in line.strip()]
         for line in open('input-10.txt').readlines()]


def is_corrupted(line):
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
            continue
        if c == ')' and stack[-1] == '(':
            stack.pop()
        elif c == ']' and stack[-1] == '[':
            stack.pop()
        elif c == '}' and stack[-1] == '{':
            stack.pop()
        elif c == '>' and stack[-1] == '<':
            stack.pop()
        else:
            return c
    return None


def score(line):
    return line.count(')') * 3 + \
        line.count(']') * 57 + \
        line.count('}') * 1197 + \
        line.count('>') * 25137


def completion(line):
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
            continue
        if c == ')' and stack[-1] == '(':
            stack.pop()
        elif c == ']' and stack[-1] == '[':
            stack.pop()
        elif c == '}' and stack[-1] == '{':
            stack.pop()
        elif c == '>' and stack[-1] == '<':
            stack.pop()
    m = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    return [m[l] for l in reversed(stack)]


def score2(completion):
    m = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    score = 0
    for c in completion:
        score *= 5
        score += m[c]
    return score


corrupted = [is_corrupted(l) for l in chars if is_corrupted(l)]
print("part 1:", score(corrupted))

incomplete = [l for l in chars if not is_corrupted(l)]
completions = [completion(i) for i in incomplete]
scores = sorted([score2(comp) for comp in completions])
print("part 2:", scores[len(scores)//2])
