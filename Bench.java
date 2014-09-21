/*
 * Copyright (C) 2014 Katsuya Iida. All rights reserved.
 */

import java.util.*;
import java.io.*;

public class Bench {

    static final int TEST_SIZE = 5000 * 100;

    static class User {
        String name;
        String email;
        LinkedList<String> messageList = new LinkedList<String>();
        User(String name, String email) {
            this.name = name;
            this.email = email;
        }
        public String toString() {
            return name + "<" + email + ">";
        }
    }

    static class TestData {
        String fromId;
        String toId;
        TestData(String fromId, String toId) {
            this.fromId = fromId;
            this.toId = toId;
        }
    }

    Map<String, User> idUserMap = new HashMap<String, User>();
    List<TestData> testDataList = new ArrayList<TestData>();
    
    String indexToId(int index) {
        return "id-" + index;
    }
    
    public void load() throws Exception {
        // No error check for brevity.
        BufferedReader reader = new BufferedReader(new FileReader("userdata.csv"));
        String line;
        int index = 0;
        while ((line = reader.readLine()) != null) {
            String[] record = line.split(",");
            String name = record[0];
            String email = record[2];
            User User = new User(name, email);
            String id = indexToId(index++);
            idUserMap.put(id, User);
        }
        reader.close();

        int numUsers = idUserMap.size();
        for (int i = 0; i < TEST_SIZE; i++) {
            String fromId = indexToId((int) (Math.random() * numUsers));
            String toId = indexToId((int) (Math.random() * numUsers));
            TestData data = new TestData(fromId, toId);
            testDataList.add(data);
        }
    }

    public void test() {
        for (TestData data : testDataList) {
            User fromUser = idUserMap.get(data.fromId);
            User toUser = idUserMap.get(data.toId);
            String message = fromUser + " to " + toUser;
            toUser.messageList.add(message);
        }
    }

    public void examine() {
        int numUsers = idUserMap.size();
        for (int i = 0; i < 3; i++) {
            String id = indexToId((int) (Math.random() * numUsers));
            User user = idUserMap.get(id);
            System.out.println("To: " + user);
            for (String message : user.messageList) {
                System.out.println(message);
            }
        }
    }

    public void run() throws Exception {
        System.out.println("loading: " + TEST_SIZE + " test items");
        load();
        long start = System.nanoTime();
        System.out.println("start");
        for (int i = 0; i < 4; i++) {
            test();
            long end = System.nanoTime();
            System.out.println("time: " + ((end - start) / 1000000.0) + "ms");
        }
        // examine();
    }

    public static void main(String[] args) throws Exception {
        new Bench().run();
    }
}
