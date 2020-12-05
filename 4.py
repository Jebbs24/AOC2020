from typing import Dict, List
import re

""" Fields:
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
Passport = Dict[str, str]


def make_passport(raw: str) -> Passport:
    lines = raw.strip().split("\n")
    lines = [line.strip() for line in lines if line.strip()]
    passport = {}
    for line in lines:
        for chunk in line.split(" "):
            key, value = chunk.split(":")
            passport[key] = value
    return passport


def make_passports(raw: str) -> List[Passport]:
    chunks = raw.split('\n\n')
    return [make_passport(data) for data in chunks if data.strip()]


def is_valid(passport: Passport, required_fields: List[str] = req_fields) -> bool:
    return all(field in passport for field in required_fields)


def is_valid2(passport: Passport) -> bool:
    validation_checks = [
        1920 <= int(passport.get('byr', -1)) <= 2002,
        2010 <= int(passport.get('iyr', -1)) <= 2020,
        2020 <= int(passport.get('eyr', -1)) <= 2030,
        is_valid_height(passport.get('hgt', '')),
        re.match(r"^#[0-9a-f]{6}$", passport.get('hcl', '')),
        passport.get('ecl') in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        re.match(r"^[0-9]{9}$", passport.get('pid', '')),
        is_valid_height(passport.get('hgt', '')),
        re.match(r"^#[0-9a-f]{6}$", passport.get('hcl', '')),
        passport.get('ecl') in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        re.match(r"^[0-9]{9}$", passport.get('pid', ''))
    ]
    return all(validation_checks)


def is_valid_height(hgt: str) -> bool:
    if hgt.endswith('cm'):
        hgt = hgt.replace('cm', '')
        try:
            return 150 <= int(hgt) <= 193
        except:
            return False
    elif hgt.endswith("in"):
        hgt = hgt.replace("in", "")
        try:
            return 59 <= int(hgt) <= 76
        except:
            return False
    return False


with open('4.txt') as f:
    passports = make_passports(f.read())
    print("Part one:", sum(is_valid(passport) for passport in passports))
    print("Part two:", sum(is_valid2(passport) for passport in passports))
