#
# Copyright (C) 2014 Katsuya Iida. All rights reserved.
#

import codecs
import random
import time

id_user_map = {}
test_data_list = []

TEST_SIZE = 5000 * 100

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.message_list = []
    def __str__(self):
        return self.name + " <" + self.email + ">";
        
class TestData:
    def __init__(self, from_id, to_id):
        self.from_id = from_id
        self.to_id = to_id

def index_to_id(index):
    return "id-%d" % index
        
def load():
    file = codecs.open("dummy.csv", "r", "shift-jis")
    index = 0
    file.readline() # Skip the first line.
    for line in file:
        record = line.split(",")
        id = index_to_id(index);
        user = User(record[0], record[2])
        id_user_map[id] = user
        index = index + 1

    num_users = len(id_user_map)
    for i in range(TEST_SIZE):
        from_id = index_to_id(int(random.random() * num_users))
        to_id = index_to_id(int(random.random() * num_users))
        data = TestData(from_id, to_id)
        test_data_list.append(data)

def test():
    for data in test_data_list:
        from_user = id_user_map[data.from_id];
        to_user = id_user_map[data.to_id];
        message = "%s to %s" % (from_user, to_user);
        to_user.message_list.append(message);

def examine():
    num_users = len(id_user_map)
    for i in range(3):
        id = index_to_id(int(random.random() * num_users))
        user = id_user_map[id];
        print "To: %s" % (user);
        for message in user.message_list:
            print message

print "loading: %d test items" % TEST_SIZE
load()
print "start"
start = time.time()
for i in range(4):
    test()
    end = time.time()
    print "time: %dms" % ((end - start) * 1000)
# examine()