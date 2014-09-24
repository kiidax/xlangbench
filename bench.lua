--
-- Copyright (C) 2014 Katsuya Iida. All rights reserved.
--

local TEST_SIZE = 5000 * 100

User = {}
User.__index = User

function User:new(o)
    local o = o or {}
    setmetatable(o, User)
    self.__index = self
    if not o.messageList then
        o.messageList = {}
    end
    return o
end

function User.__tostring(user)
    return user.name .. " <" .. user.email .. ">"
end

function indexToId(index)
    return "id-" .. index
end

local idUserMap = {}
local testDataList = {}
local numUsers = 0

function load()
    local index = 0
    for line in io.lines("userdata.csv") do
        local p1 = line:find(",")
        local p2 = line:find(",", p1 + 1)
        local name = line:sub(1, p1 - 1)
        local email = line:sub(p2 + 1)
        local user = User:new{name = name, email = email}
        local id = indexToId(index)
        idUserMap[id] = user
        index = index + 1
    end

    numUsers = index
    for i = 1, TEST_SIZE do
        local toId = indexToId(math.random(0, numUsers - 1))
        local fromId = indexToId(math.random(0, numUsers - 1))
        local data = { fromId = fromId, toId = toId }
        testDataList[#testDataList + 1] = data
    end
end

function test()
    for i, data in ipairs(testDataList) do
        local fromUser = idUserMap[data.fromId]
        local toUser = idUserMap[data.toId]
        toUser.messageList[#toUser.messageList + 1] = tostring(fromUser) .. " to " .. tostring(toUser)
    end
end

function examine()
    for i = 1, 3 do
        local id = indexToId(math.random(0, numUsers - 1))
        local user = idUserMap[id]
        print("To: " .. tostring(user))
        for i, message in ipairs(user.messageList) do
            print(message)
        end
    end
end

print("loading " .. TEST_SIZE .. " test items")
load()
collectgarbage()
print("start")
local start = os.clock()
for i = 1, 4 do
    test()
    local endTime = os.clock()
    print("time: " .. (endTime - start))
end
-- examine()
