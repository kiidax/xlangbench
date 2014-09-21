/*
 * Copyright (C) 2014 Katsuya Iida. All rights reserved.
 */

using System.Collections.Generic;
using System;

public class Bench {

    const int TEST_SIZE = 5000 * 100;

    class User {
        public string Name;
        public string Email;
        public IList<string> MessageList = new List<string>();
        public override string ToString() {
            return Name + "<" + Email + ">";
        }
    }

    struct TestData {
        public string FromId;
        public string ToId;
    }

    IDictionary<string, User> idUserMap = new Dictionary<string, User>();
    LinkedList<TestData> testDataList = new LinkedList<TestData>();
    
    string IndexToId(int index) {
        return "id-" + index;
    }
    
    public void Load()
    {
        // No error check for brevity.
        string[] lines = System.IO.File.ReadAllLines(@"userdata.csv");
        for (int index = 0; index < lines.Length; index++)
        {
            string[] record = lines[index].Split(',');
            string name = record[0];
            string email = record[2];
            string id = IndexToId(index);
            idUserMap[id] = new User {
                Name = name,
                Email = email
            };
        }

        var rnd = new Random();
        int numUsers = idUserMap.Count;
        for (int i = 0; i < TEST_SIZE; i++) {
            string fromId = IndexToId(rnd.Next(numUsers));
            string toId = IndexToId(rnd.Next(numUsers));
            TestData data = new TestData {
                FromId = fromId,
                ToId = toId
            };
            testDataList.AddLast(data);
        }
    }

    public void Test() {
        foreach (var data in testDataList) {
            var fromUser = idUserMap[data.FromId];
            var toUser = idUserMap[data.ToId];
            string message = fromUser + " to " + toUser;
            toUser.MessageList.Add(message);
        }
    }

    public void Examine() {
        int numUsers = idUserMap.Count;
        var rnd = new Random();
        for (int i = 0; i < 3; i++) {
            string id = IndexToId(rnd.Next(numUsers));
            var user = idUserMap[id];
            Console.WriteLine("To: " + user);
            foreach(string message in user.MessageList) {
                Console.WriteLine(message);
            }
        }
    }

    public void Run() {
        Console.WriteLine("loading: " + TEST_SIZE + " test items");
        Load();
        long start = Environment.TickCount;
        Console.WriteLine("start");
        for (int i = 0; i < 4; i++) {
            Test();
            long end = Environment.TickCount;
            Console.WriteLine("time: " + (end - start) + "ms");
        }
        // examine();
    }

    static void Main(string[] args)
    {
        new Bench().Run();
    }
}
