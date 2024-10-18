
def alphabeta(node, depth, alpha, beta, maximizingPlayer, game_tree):
    if depth == 0 or node not in game_tree:
        return node  # Return node as the terminal value (for simplicity)

    if maximizingPlayer:
        max_eval = float('-inf')
        for child in game_tree[node]:
            eval = alphabeta(child, depth - 1, alpha, beta, False, game_tree)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in game_tree[node]:
            eval = alphabeta(child, depth - 1, alpha, beta, True, game_tree)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
