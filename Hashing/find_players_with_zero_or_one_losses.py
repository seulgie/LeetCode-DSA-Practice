from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Set the initial values as 0 using defaultdict
        loss_count = defaultdict(int)

        # Populate the dictionary with losses
        for winner, loser in matches:
            loss_count[loser] += 1  
            if winner not in loss_count:
                loss_count[winner] = 0

        # Lists to store players with 0 and 1 losses
        no_loss = []
        one_loss = []

        # Separate players based on their loss count
        for player, losses in loss_count.items():
            if losses == 0:
                no_loss.append(player)
            elif losses == 1:
                one_loss.append(player)

        # Sort the lists in ascending order
        no_loss.sort()
        one_loss.sort()

        return [no_loss, one_loss]
