def substring_pattern_match(string_to_search, pattern):
  if len(pattern) < 1:
    return 0
  
  for i in range(len(string_to_search)):
    search_idx = i
    pattern_idx = 0

    while pattern_idx < len(pattern) and string_to_search[search_idx] == pattern[pattern_idx]:
      search_idx += 1
      pattern_idx += 1
    
    if pattern_idx == len(pattern):
      return i
    
  return -1