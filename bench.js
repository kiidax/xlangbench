/*
 * Copyright (C) 2014 Katsuya Iida. All rights reserved.
 */

"use strict";

var TEST_SIZE = 5000 * 100;

function User(name, email) {
    this.name = name;
    this.email = email;
    this.messageList = [];
}

User.prototype.toString = function () {
    return this.name + " <" + this.email + ">";
}

function TestData(fromId, toId) {
    this.fromId = fromId;
    this.toId = toId;
}

var idUserMap = {};
var testDataList = [];

function indexToId(index) {
    return "id-" + index;
}

function load() {
    var buf = read("userdata.csv");
    var index = 0;
    buf.split(/[\r\n]+/).forEach(function (line) {
	var record = line.split(/,/)
        var id = indexToId(index++);
        idUserMap[id] = new User(record[0], record[2]);
    });
    
    var numUsers = Object.keys(idUserMap).length;
    for (var i = 0; i < TEST_SIZE; i++) {
        var fromId = indexToId(Math.floor(Math.random() * numUsers));
        var toId = indexToId(Math.floor(Math.random() * numUsers));
        testDataList.push(new TestData(fromId, toId));
    }
}

function test() {
    var len = testDataList.length;
    for (var i = 0; i < len; i++) {
        var data = testDataList[i];
        var fromId = data.fromId;
        var toId = data.toId;
        var fromUser = idUserMap[fromId];
        var toUser = idUserMap[toId];
        var message = fromUser + " to " + toUser;
        toUser.messageList.push(message);
    }
}

function examine() {
    var numUsers = Object.keys(idUserMap).length;
    for (var i = 0; i < 3; i++) {
        var id = indexToId(Math.floor(Math.random() * numUsers));
        var user = idUserMap[id];
        print("To: " + user);
        for (var j = 0; j < user.messageList.length; j++) {
            print(user.messageList[j]);
        }
    }
}

print("loading: " + TEST_SIZE + " test items");
load();
var start = new Date().getTime();
print("start");
for (var i = 0; i < 4; i++) {
    test();
    var end = new Date().getTime();
    print("time: " + (end - start));
}
// examine();
