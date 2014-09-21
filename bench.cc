/*
 * Copyright (C) 2014 Katsuya Iida. All rights reserved.
 */

#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace::std;

#define TEST_SIZE (5000 * 100)

class User
{
public:
    string name;
    string email;
    vector<string> messageList;
    User() {}
    User(const string& name_, const string& email_) : name(name_), email(email_) {}
    operator string() const {
        return name + "<" + email + ">";
    }
};

class TestData
{
public:
    string fromId;
    string toId;
    TestData(const string& fromId_, const string& toId_) : fromId(fromId_), toId(toId_) {}
};

typedef map<string, User> UserMap;
typedef vector<TestData> TestDataList;

UserMap userMap;
TestDataList testDataList;

string indexToId(int index)
{
    char buf[32];
    sprintf(buf, "id-%d", index);
    return buf;
}

void load()
{
    ifstream ifs("userdata.csv");
    string line;
    getline(ifs, line); // Skip the first line.
    int index = 0;
    while (!ifs.eof()) {
        string line;
        getline(ifs, line);
        int p1 = line.find(',', 0);
        int p2 = line.find(',', p1 + 1);
        int p3 = line.find(',', p2 + 1);
        string name = line.substr(0, p1);
        string email = line.substr(p2 + 1, p3 - p2 - 1);
        string id = indexToId(index++);
        userMap[id] = User(name, email);
    }
    ifs.close();

    int numUsers = userMap.size();
    for (int i = 0; i < TEST_SIZE; i++) {
        string fromId = indexToId(rand() % numUsers);
        string toId = indexToId(rand() % numUsers);
        testDataList.push_back(TestData(fromId, toId));
    }
}

void test()
{
    for (TestDataList::iterator iter = testDataList.begin(); iter != testDataList.end(); ++iter) {
        const User& fromUser = userMap[(*iter).fromId];
        User& toUser = userMap[(*iter).toId];
        string message = static_cast<string>(fromUser) + " to " + static_cast<string>(toUser);
        toUser.messageList.push_back(message);
    }
}

void examine()
{
    int numUsers = userMap.size();
    for (int i = 0; i < 3; i++) {
        string id = indexToId(rand() % numUsers);
        const User& user = userMap[id];
        cout << "To: " << static_cast<string>(user) << endl;
        for (vector<string>::const_iterator iter = user.messageList.begin(); iter != user.messageList.end(); ++iter) {
            cout << *iter << endl;
        }
    }
}

int main(int argc, char *argv[])
{
    cout << "loading: " << TEST_SIZE << " test items" << endl;
    load();
    clock_t start = clock();
    cout << "start" << endl;
    for (int i = 0; i < 4; i++) {
        test();
        clock_t end = clock();
        cout << "time: " << ((end - start) * 1000.0 / CLOCKS_PER_SEC) << "ms" << endl;
    }
    // examine();
    return 0;
}
