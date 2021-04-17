def lengthOfLongestSubstring(string):
    subStringSet = set()
    slidingWindowLeft = 0
    slidingWindowRight = 0
    maxDiscoveredSubstringLength = 0
    while slidingWindowRight < len(string):
        if string[slidingWindowRight] not in subStringSet:
            subStringSet.add(string[slidingWindowRight])
            slidingWindowRight = slidingWindowRight + 1
        else:
            maxDiscoveredSubstringLength = max(maxDiscoveredSubstringLength, len(subStringSet))
            subStringSet.remove(string[slidingWindowLeft])
            slidingWindowLeft += 1
    return max(maxDiscoveredSubstringLength, len(subStringSet))


if __name__ == '__main__':
    print(lengthOfLongestSubstring(" "))
