def shopping(accumulated_points, bill):
    res = ''
    
    if accumulated_points < 0 or bill < 0:
        return 'Invalid input'

    if bill > 100:
        res = '+1 accumulated point'
        accumulated_points += 1
    if accumulated_points >= 5 and bill <= 1000:
        res = 'You got a 10% bill discount'
    
    return res