from typing import List
from collections import Counter


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        tokens = list(corpus)
        merges = []

        for _ in range(num_merges):
            # Count frequencies of adjacent token pairs
            pair_counts = Counter(
                (tokens[i], tokens[i + 1])
                for i in range(len(tokens) - 1)
            )

            # Stop if no adjacent pairs exist
            if not pair_counts:
                break

            # Find the most frequent pair; break ties lexicographically
            max_freq = max(pair_counts.values())
            best_pair = min(
                pair for pair, freq in pair_counts.items()
                if freq == max_freq
            )

            a, b = best_pair
            merges.append([a, b])

            # Merge all non-overlapping occurrences from left to right
            new_tokens = []
            i = 0

            while i < len(tokens):
                if (
                    i + 1 < len(tokens)
                    and tokens[i] == a
                    and tokens[i + 1] == b
                ):
                    new_tokens.append(a + b)
                    i += 2
                else:
                    new_tokens.append(tokens[i])
                    i += 1

            tokens = new_tokens

        return merges