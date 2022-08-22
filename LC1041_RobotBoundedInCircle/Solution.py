# Idea: As long as its direction is not north (that is 'GGGGG'), it can return.
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        turn_right = {}
        turn_right[(0,1)] = (1, 0)
        turn_right[(1,0)] = (0, -1)
        turn_right[(0,-1)] = (-1, 0)
        turn_right[(-1,0)] = (0, 1)

        turn_left = {}
        turn_left[(0,1)] = (-1, 0)
        turn_left[(1,0)] = (0, 1)
        turn_left[(0,-1)] = (1, 0)
        turn_left[(-1,0)] = (0, -1)

        pos = [0,0]
        dir = (0,1)

        for ins in instructions:
            if ins == 'G':
                pos[0] += dir[0]
                pos[1] += dir[1]
            elif ins == 'L':
                dir = turn_left[dir]
            elif ins == 'R':
                dir = turn_right[dir]
        
        if pos[0] == 0 and pos[1] == 0:
            return True
        elif dir == (0,1):
            return False
        else:
            return True
        