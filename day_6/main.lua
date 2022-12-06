print("Hello World!")

local function verify_if_marker(marker, marker_len)
    local s = {}
    for i = 1, marker:len() do
        if not s[marker:sub(i, i)] then
            s[marker:sub(i, i)] = true
        end
    end
    local s_len = 0
    for _ in pairs(s) do s_len = s_len + 1 end
    if s_len ~= marker_len then
        return false
    end
    return true
end

local function detect_marker(input, marker_len)

    local curr_marker = input:sub(0, marker_len)
    for i = marker_len, input:len() do
        if verify_if_marker(curr_marker, marker_len) then
            return i
        else
            curr_marker = curr_marker:sub(2, curr_marker:len())
            curr_marker = curr_marker .. input:sub(i + 1, i + 1)
        end
    end
    return -1
end

local function main()
    local file = "input.txt"
    local f = assert(io.open(file, "r"))
    local content = f:read("*all")
    f:close()
    print(detect_marker(content, 14))

end

-- verify_if_marker("gsml", 4)
main()
