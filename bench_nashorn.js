/*
 * Copyright (C) 2014 Katsuya Iida. All rights reserved.
 */

 "use strict";

function read(filename) {
    var reader = new java.io.BufferedReader(new java.io.FileReader(filename));
    var ret = "";
    var line;
    while ((line = reader.readLine()) !== null) {
        ret += line + "\n";
    }
    reader.close();
    return ret;
}

load("bench.js");
