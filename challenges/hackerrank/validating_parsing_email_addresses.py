"""
Solution for: Validating Email Addresses With a Filter

https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
"""
import os
import re
import sys


def fun(email):
    username_ptrn = r"^([a-z]|[A-Z]|[0-9]|[_-])+@"
    domain_ptrn = r"([a-z]|[A-Z]|[0-9])+\."
    tld_ptrn = r"([a-z]|[A-Z]){1,3}$"
    email_ptrn = f"{username_ptrn}{domain_ptrn}{tld_ptrn}"

    return bool(re.match(email_ptrn, email))


def filter_mail(emails):
    return list(filter(fun, emails))


def main():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)


if __name__ == "__main__":
    if os.path.exists("in.txt"):
        sys.stdin = open("in.txt")
        sys.stdout = open("out.txt", "w")

    main()
