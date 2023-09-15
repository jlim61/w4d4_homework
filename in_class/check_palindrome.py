def check_palindrome(astring):
    left_point, right_point = 0, len(astring) - 1
    while left_point < right_point:
        if astring[left_point].lower() != astring[right_point].lower():
            return False
        left_point += 1
        right_point -= 1
    return True