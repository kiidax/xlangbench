#
# Copyright (C) 2014 Katsuya Iida. All rights reserved.
#

import bisect
import random
import sys

class GenealogyData:
    
    def __init__(self):
        self.cum_freqs = []
        self.names = []
        self.last_freq = 0.0

    def load(self, filename):
        f = open(filename)
        for line in f:
            record = line.split()
            name = record[0]
            cum_freq = float(record[2])
            self.names.append(name)
            self.cum_freqs.append(cum_freq)
            self.last_freq = cum_freq

    def find_gt(self, x):
        i = bisect.bisect_right(self.cum_freqs, x)
        if i != len(self.cum_freqs):
            return self.names[i]
        raise ValueError

def genrandom():
    return random.random()

def generate_one():
    while True:
        if genrandom() * (1.0 + sex_ratio) > 1.0:
            sex = "male"
            first_data = male_data
        else:
            sex = "female"
            first_data = female_data

        x = genrandom() * first_data.last_freq
        raw_first_name = first_data.find_gt(x)
        x = genrandom() * last_data.last_freq
        raw_last_name = last_data.find_gt(x)

        domain = domain_data[int(genrandom() * len(domain_data))]
        first_name = raw_first_name.capitalize()
        last_name = raw_last_name.capitalize()
        email = ("%s.%s@%s" % (raw_first_name, raw_last_name, domain)).lower()
        name = " ".join((first_name, last_name))

        # Make sure email is uniq.
        if not email in email_sets:
            break

    email_sets[email] = True
    return (name, sex, email)
    
def generate(num):
    for i in range(num):
        one = generate_one()
        print ','.join(one)

def usage():
    print >> sys.stderr, '''%s: [NUM] [SEED]
Generate fake personal identifiable information.

NUM is the number of entries to generate.
SEED is a string used for the random seed to generate data.''' % (sys.argv[0])

try:
    if len(sys.argv) == 3:
        num = int(sys.argv[1])
        seed = sys.argv[2]
    elif len(sys.argv) == 2:
        num = int(sys.argv[1])
        seed = None
    else:
        raise "less arguments"
except:
    usage()
    exit(1)

last_data = GenealogyData()
last_data.load("dist.all.last")
male_data = GenealogyData()
male_data.load("dist.male.first")
female_data = GenealogyData()
female_data.load("dist.female.first")

sex_ratio = 0.95 # US has 0.95 male for every 1 female

domain_data = [ "example.com", "example.net", "example.org", "example.edu" ]

email_sets = {}

random.seed(seed)
generate(num)

exit(0)
